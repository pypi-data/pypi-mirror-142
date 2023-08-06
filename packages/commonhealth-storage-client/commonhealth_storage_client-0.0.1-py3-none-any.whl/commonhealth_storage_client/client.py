import uuid
import hashlib
import requests
from requests.exceptions import HTTPError as requestsHTTPError
import datetime
from urllib.parse import urlunsplit, urlencode
import abc
import secrets
import base64
import logging
import json
from typing import Callable, Dict, Any, Optional, List

from .errors import (
    ImproperlyConfigured,
    UserNotConsented,
    DelegateStateError
)
from .jwt import (
    build_jwt
)
from .crypto import (
    SerializedKey,
    tink_ECDSA_P256_json_key,
    tink_hybrid_encryption_key,
    keyset_handle_to_json,
    keyset_handle_from_json,
    keyset_handle_from_bytes,
    tink_signing_primitive,
    tink_hybrid_decryption_primitive,
    tink_aead_primitive,
    generate_tink_signing_key,
    generate_tink_encryption_key,
    LIBRARY_TINK,
    SERIALIZATION_MODE_JSON,
    ALGORITHM_ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM
)
import jwt

logger = logging.getLogger("CommonHealth Storage Client")

AUTH_REQUEST_JWT_CLAIM_SCOPE = "scope"
AUTH_REQUEST_JWT_CLAIM_EXP = "exp"
AUTH_REQUEST_JWT_CLAIM_IAT = "iat"
AUTH_REQUEST_JWT_CLAIM_USER_ID = "user_id"
AUTH_REQUEST_JWT_CLAIM_ISSUER = "iss"
AUTH_REQUEST_JWT_CLAIM_NONCE = "nonce"
AUTH_REQUEST_JWT_CLAIM_REQUEST_ID = "request_id"
AUTH_REQUEST_JWT_CLAIM_ENCRYPTION_PUBLIC_KEY = "encryption_public_key"

AUTH_REQUEST_JWT_DEFAULT_EXPIRATION_CEILING_SECONDS = 60 * 60 * 24 * 30 # 30 days
AUTH_REQUEST_JWT_NONCE_BYTES_SIZE = 32


class CHStorageDelegate():

    @abc.abstractmethod
    def get_secure_value(self, key):
        raise NotImplementedError()

    @abc.abstractmethod
    def set_secure_value(self, key, value):
        raise NotImplementedError()

    @abc.abstractmethod
    def clear_value(self, key):
        raise NotImplementedError()

    @abc.abstractmethod
    def clear_all_values(self):
        raise NotImplementedError()

class ResourceHolder():

    def __init__(
        self,
        json_content,
        resource_type
    ):
        self.json_content = json_content
        self.resource_type = resource_type

class CHClient():

    def __init__(
        self,
        client_id,
        client_secret,
        partner_id,
        storage_delegate,
        ch_authorization_deeplink,
        ch_host=None,
        ch_port=None,
        ch_scheme=None,
        logging_enabled=True
    ):
        if storage_delegate is None:
            raise ImproperlyConfigured("Must pass storage delegate object")

        self.client_id = client_id
        self.client_secret = client_secret
        self.partner_id = partner_id
        self.storage_delegate = storage_delegate
        self.ch_authorization_deeplink = ch_authorization_deeplink
        self.ch_host = ch_host
        self.ch_port = ch_port
        self.ch_scheme = ch_scheme
        self.logging_enabled = logging_enabled

    @property
    def _host_with_port(self):
        return f'{self.ch_host}:{self.ch_port}'

    @property
    def _partner_detail_url(self):
        path = f'/api/v1/sharing-partners/{self.partner_id}'
        return urlunsplit((self.ch_scheme, self._host_with_port, path, None, ""))

    @property
    def _partner_detail_signing_keys_url(self):
        path = f'/api/v1/sharing-partners/{self.partner_id}/signing_keys'
        return urlunsplit((self.ch_scheme, self._host_with_port, path, None, ""))

    @property
    def _storage_delegate_key_signing_key(self):
        return "private_signing_key"

    def _storage_delegate_key_patient_encryption_key(self, patient_id):
        return f'patient_encryption_key/patient/{patient_id}'

    def _get_patient_id_mapping(self, patient_id):
        delegate_key = f'patient_id_mapping/{patient_id}'
        stored_mapped_key = self.storage_delegate.get_secure_value(delegate_key)
        if stored_mapped_key:
            if self.logging_enabled:
                logger.debug(f'Found mapped patient ID {stored_mapped_key}')

            return stored_mapped_key

        mapped_id = str(uuid.uuid4())
        if self.logging_enabled:
            logger.debug(f'No stored patient ID found; created new one {mapped_id}')

        self.storage_delegate.set_secure_value(delegate_key, mapped_id)
        return mapped_id

    def get_configuration(self):
        url = self._partner_detail_url
        resp = self._get(url)
        return resp

    def update_configuration(self, new_configuration):
        url = self._partner_detail_url
        resp = self._post(url, new_configuration)
        return resp

    def update_signing_keys(self, signing_key_data):
        url = self._partner_detail_signing_keys_url
        try:
            return self._post(url, signing_key_data)
        except Exception as e:
            if self.logging_enabled:
                logger.exception("Exception updating signing keys")

    def perform_initialization(
        self,
        name,
        logo_uri,
        clear_existing_signing_keys=False # Should only be used for debugging
    ):
        existing_config = self.get_configuration()

        # check if signing key needs to be bootstrapped
        if not existing_config['signing_keys'] or clear_existing_signing_keys:
            if self.logging_enabled:
                logger.debug("Generating new signing keys")

            public_key, private_key = generate_tink_signing_key()
            updated_keys = [ vars(public_key) ]
            if self.logging_enabled:
                logger.debug(f'Updating signing keys with: {updated_keys}')
            resp = self.update_signing_keys(updated_keys)

            if resp:
                self.storage_delegate.set_secure_value(self._storage_delegate_key_signing_key, private_key.to_json())

        # check if name or logo needs to be updated
        update = { }
        if name != existing_config["name"]:
            update['name'] = name
        if logo_uri != existing_config["logo_uri"]:
            update["logo_uri"] = logo_uri

        if update:
            self.update_configuration(update)

    def construct_authorization_request_deeplink(
        self,
        patient_id: str,
        scope: str,
        duration_seconds: int,
        expiration_seconds: int,
        rotate_encryption_key=False
    ):
        now = datetime.datetime.now()
        expiration = now + datetime.timedelta(seconds=expiration_seconds)
        nonce = base64.b64encode(secrets.token_bytes(AUTH_REQUEST_JWT_NONCE_BYTES_SIZE)).decode()
        request_id = str(uuid.uuid4())
        mapped_patient_id = self._get_patient_id_mapping(patient_id)

        # Note: JWT signing support is not out of the box supported in Tink, and I haven't found
        # a good way to generate a Tink signing key for use in PyJWT. As a workaround, we
        # generate a JWT using a bogus symmmetric key, strip off the signature and sign it using Tink.
        header = {
            "alg": "TinkES256", # TODO - change this to be a JWKS?
            "typ": "JWT"
        }

        # Get signing key
        try:
            private_signing_key = SerializedKey.from_json(self.storage_delegate.get_secure_value(self._storage_delegate_key_signing_key))
        except Exception as e:
            if self.logging_enabled:
                logger.exception("Must have signing key to generate deeplink")
            raise DelegateStateError("Must have signing key to generate deeplink")

        # Generate encryption key if needed
        storage_delegate_key_for_encryption_key = self._storage_delegate_key_patient_encryption_key(patient_id)
        if rotate_encryption_key:
            self.storage_delegate.clear_value(storage_delegate_key_for_encryption_key)
            existing_private_key = None
        else:
            try:
                existing_private_key = SerializedKey.from_json(self.storage_delegate.get_secure_value(storage_delegate_key_for_encryption_key))
            except:
                existing_private_key = None

        if existing_private_key is None:
            _, existing_private_key = generate_tink_encryption_key()
            self.storage_delegate.set_secure_value(storage_delegate_key_for_encryption_key, existing_private_key.to_json())

        keyset_handle = keyset_handle_from_json(existing_private_key.material)
        public_keyset_handle = keyset_handle.public_keyset_handle()
        public_keyset_handle_json = keyset_handle_to_json(public_keyset_handle)

        public_key = SerializedKey(
            public_keyset_handle_json,
            ALGORITHM_ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM,
            LIBRARY_TINK,
            SERIALIZATION_MODE_JSON
        )

        payload = {
            AUTH_REQUEST_JWT_CLAIM_SCOPE: scope,
            AUTH_REQUEST_JWT_CLAIM_EXP: int(expiration.timestamp()),
            AUTH_REQUEST_JWT_CLAIM_IAT: int(now.timestamp()),
            AUTH_REQUEST_JWT_CLAIM_USER_ID: mapped_patient_id,
            AUTH_REQUEST_JWT_CLAIM_NONCE: nonce,
            AUTH_REQUEST_JWT_CLAIM_ISSUER: self.partner_id,
            AUTH_REQUEST_JWT_CLAIM_REQUEST_ID: str(uuid.uuid4()),
            AUTH_REQUEST_JWT_CLAIM_ENCRYPTION_PUBLIC_KEY: vars(public_key)
        }

        signing_keyset_handle = keyset_handle_from_json(private_signing_key.material)
        signer_primitive = tink_signing_primitive(signing_keyset_handle)
        signer = lambda x: signer_primitive.sign(x)

        signed_token = build_jwt(header, payload, signer)

        return self.ch_authorization_deeplink + "?authorization_request=" + signed_token

    def needs_request_consent(self, patient_id) -> bool:
        # check if an encryption key is stored for that user
        # if not, return False
        mapped_patient_id = self._get_patient_id_mapping(patient_id)
        storage_delegate_key_for_encryption_key = self._storage_delegate_key_patient_encryption_key(patient_id)
        if not self.storage_delegate.get_secure_value(storage_delegate_key_for_encryption_key):
            return False

        # Next, check whether the user has opted into sharing on the backend
        url = self._get_user_data_url(mapped_patient_id)
        try:
            json_response = self._get(url)
            return True
        except requestsHTTPError as e:
            status_code = e.response.status_code
            if status_code == 404:
                return False
            else:
                raise HTTPError(status_code)

    def fetch_data(self, patient_id) -> List[ResourceHolder]:
        mapped_patient_id = self._get_patient_id_mapping(patient_id)
        url = self._get_user_data_url(mapped_patient_id)
        try:
            json_response = self._get(url)
        except requestsHTTPError as e:
            status_code = e.response.status_code
            if status_code == 404:
                raise UserNotConsented()
            else:
                raise HTTPError(status_code)

        storage_delegate_key_for_encryption_key = self._storage_delegate_key_patient_encryption_key(patient_id)
        encryption_key_json = self.storage_delegate.get_secure_value(storage_delegate_key_for_encryption_key)
        if not encryption_key_json:
            raise DelegateStateError(f'No stored encryption key for patient found')

        try:
            encryption_key = SerializedKey.from_json(encryption_key_json)
        except Exception as e:
            if self.logging_enabled:
                logger.exception("Exception getting encryption key to read patient data")

        private_keyset_handle = keyset_handle_from_json(encryption_key.material)

        if isinstance(json_response, dict):
            json_response = [json_response]

        resources = []
        for each in json_response:
            try:
                decrypted_resource = self._decrypt_resource(each, private_keyset_handle)
            except Exception as e:
                if self.logging_enabled:
                    logger.debug(e, "Exception decrypting resource")
                continue

            resource_type = each['data_type']
            resource = ResourceHolder(decrypted_resource, resource_type)
            resources.append(resource)

        if self.logging_enabled:
            logger.debug(f'Decrypted {len(resources)} resources')

        return resources

    def _get_user_data_url(self, mapped_patient_id):
        path = f'/api/v1/sharing-partners/{self.partner_id}/users/{mapped_patient_id}'
        return urlunsplit((self.ch_scheme, self._host_with_port, path, None, ""))

    def _get(self, url):
        r = requests.get(url, auth=(self.client_id, self.client_secret))
        r.raise_for_status()
        return r.json()

    def _post(self, url, data):
        r = requests.post(url, json=data, auth=(self.client_id, self.client_secret))
        r.raise_for_status()
        return r.json()

    def _decrypt_resource(self, payload, private_keyset_handle):
        decryption_primitive = tink_hybrid_decryption_primitive(private_keyset_handle)
        encrypted_content = payload['encrypted_content']
        encrypted_dek = payload['encrypted_dek']

        client_record_id = payload['client_record_id']
        client_datagroup_id = payload['client_datagroup_id']

        associated_data_for_data_decryption = client_record_id.encode('utf8')
        associated_data_for_dek_decryption = f'{client_record_id}{client_datagroup_id}'.encode('utf8')

        encrypted_dek_bytes = base64.b64decode(payload['encrypted_dek'])
        decrypted_dek = decryption_primitive.decrypt(encrypted_dek_bytes, associated_data_for_dek_decryption)

        dek_keyset = keyset_handle_from_bytes(decrypted_dek)
        dek_primitive = tink_aead_primitive(dek_keyset)

        decrypted_payload = dek_primitive.decrypt(base64.b64decode(payload['encrypted_content']), associated_data_for_data_decryption).decode('utf8')
        return json.loads(decrypted_payload)
