import tink
from tink import cleartext_keyset_handle
import io
import hashlib
import json

from tink import tink_config
tink_config.register()


ALGORITHM_ECDSA_P256 = "ECDSA_P256"
ALGORITHM_ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM = "ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM"

LIBRARY_TINK = "TINK"

SERIALIZATION_MODE_JSON = "JSON"

class SerializedKey():

    def __init__(
        self,
        material,
        algorithm,
        library,
        serialization_mode
    ):
        self.material = material
        self.algorithm = algorithm
        self.library = library
        self.serialization_mode = serialization_mode

    def hash_value(self):
        hashable_string = f'{self.material}.{self.algorithm}.{self.library}.{self.serialization_mode}'
        return hashlib.sha256(hashable_string.encode()).hexdigest()

    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        return SerializedKey(
            data['material'],
            data['algorithm'],
            data['library'],
            data['serialization_mode']
        )

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

def tink_ECDSA_P256_json_key(material):
    return SerializedKey(
        material,
        ALGORITHM_ECDSA_P256,
        LIBRARY_TINK,
        SERIALIZATION_MODE_JSON
    )

def tink_hybrid_encryption_key(material):
    return SerializedKey(
        material,
        ALGORITHM_ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM,
        LIBRARY_TINK,
        SERIALIZATION_MODE_JSON
    )

def keyset_handle_to_json(keyset_handle):
    stream = io.StringIO()
    cleartext_keyset_handle.write(
        tink.JsonKeysetWriter(stream),
        keyset_handle
    )
    return stream.getvalue()

def keyset_handle_from_json(json_keyset):
    reader = tink.JsonKeysetReader(json_keyset)
    return cleartext_keyset_handle.read(reader)

def keyset_handle_from_bytes(keyset_handle_bytes):
    reader = tink.BinaryKeysetReader(keyset_handle_bytes)
    return cleartext_keyset_handle.read(reader)

def tink_signing_primitive(keyset_handle):
    return keyset_handle.primitive(tink.signature.PublicKeySign)

def tink_hybrid_decryption_primitive(private_keyset_handle):
    return private_keyset_handle.primitive(tink.hybrid.HybridDecrypt)

def tink_aead_primitive(private_keyset_handle):
    return private_keyset_handle.primitive(tink.aead.Aead)

def generate_tink_signing_key():
    keyset_handle = tink.new_keyset_handle(tink.signature.signature_key_templates.ECDSA_P256)
    public_keyset_handle = keyset_handle.public_keyset_handle()

    keyset_handle_json = keyset_handle_to_json(keyset_handle)
    public_keyset_handle_json = keyset_handle_to_json(public_keyset_handle)

    public_key = SerializedKey(
        public_keyset_handle_json,
        ALGORITHM_ECDSA_P256,
        LIBRARY_TINK,
        SERIALIZATION_MODE_JSON
    )

    key = SerializedKey(
        keyset_handle_json,
        ALGORITHM_ECDSA_P256,
        LIBRARY_TINK,
        SERIALIZATION_MODE_JSON
    )

    return (public_key, key)

def generate_tink_encryption_key():
    keyset_handle = tink.new_keyset_handle(tink.hybrid.hybrid_key_templates.ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM)
    public_keyset_handle = keyset_handle.public_keyset_handle()

    keyset_handle_json = keyset_handle_to_json(keyset_handle)
    public_keyset_handle_json = keyset_handle_to_json(public_keyset_handle)

    public_key = SerializedKey(
        public_keyset_handle_json,
        ALGORITHM_ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM,
        LIBRARY_TINK,
        SERIALIZATION_MODE_JSON
    )

    key = SerializedKey(
        keyset_handle_json,
        ALGORITHM_ECIES_P256_HKDF_HMAC_SHA256_AES128_GCM,
        LIBRARY_TINK,
        SERIALIZATION_MODE_JSON
    )

    return (public_key, key)
