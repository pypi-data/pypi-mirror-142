from .client import CHStorageDelegate
from .errors import (
    ImproperlyConfigured,
    DelegateStateError
)
import sqlite3
import os
import time
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def requires_initialization(func):
    def wrapped_func(*args, **kwargs):
        is_initialized = args[0].is_initialized
        if not is_initialized:
            raise ImproperlyConfigured("Must call initialize first")
        return func(*args, **kwargs)

    return wrapped_func

class EmptyLogger():

    def __init__(self):
        pass

    def exception(self, msg):
        pass

    def info(self, msg):
        pass

    def debug(self, msg):
        pass

# Default delegate class that wraps a sqlite file
# Suitable for development or small projects where the CH client
# is running on a single host.

# The SQLite schema is a key<>value store, with values encrypted under a key
# derived by the db_passphrase value. Encrypted values are b64 encoded before written
# to the DB.
class SQLiteDelegate(CHStorageDelegate):

    def __init__(self, **kwargs):
        self.path_to_db_file = kwargs.pop('path_to_db_file')
        self.db_passphrase = kwargs.pop('db_passphrase')
        self.db_passphrase_salt = kwargs.pop('db_passphrase_salt')

        if 'logger' in kwargs:
            self.logger = kwargs.pop('logger')
        else:
            self.logger = EmptyLogger()

        self.is_initialized = False

    def initialize(self):
        self.fernet_key = self._get_encryption_key(self.db_passphrase)
        self._migrate()
        self.is_initialized = True
        self.logger.info("Initialization complete")

    def _get_encryption_key(self, passphrase):
        salt = self.db_passphrase_salt.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key_bytes = kdf.derive(passphrase.encode("utf8"))
        key_material = base64.b64encode(key_bytes)
        return Fernet(key_material)

    def _db_cursor_and_connection(self):
        try:
            con = sqlite3.connect(self.path_to_db_file)
        except Exception as e:
            self.logger.exception("Exception getting DB connection")
            raise ImproperlyConfigured(f'Cannot connect to SQLite database at {self.path_to_db_file}')

        try:
            cursor = con.cursor()
        except Exception as e:
            self.logger.exception("Exception getting DB cursor")
            raise ImproperlyConfigured(f'Cannot get cursor from SQLite DB connnection')

        return con, cursor

    def _migrate(self):
        con, cursor = self._db_cursor_and_connection()
        cursor.execute('CREATE TABLE IF NOT EXISTS key_value (key TEXT NOT NULL, enc_value TEXT NOT NULL, date INTEGER NOT NULL, CONSTRAINT unique_key UNIQUE (key));')
        con.commit()
        con.close()

    @requires_initialization
    def _encrypt_value(self, value):
        value_bytes = value.encode("utf8")
        encrypted_bytes = self.fernet_key.encrypt(value_bytes)
        b64_encrypted_string = base64.b64encode(encrypted_bytes)
        return b64_encrypted_string

    @requires_initialization
    def _decrypt_value(self, value):
        encrypted_bytes = base64.b64decode(value)
        decrypted_bytes = self.fernet_key.decrypt(encrypted_bytes)
        decrypted_string = decrypted_bytes.decode("utf8")
        return decrypted_string

    @requires_initialization
    def get_secure_value(self, key):
        con, cursor = self._db_cursor_and_connection()
        cursor.execute("SELECT * FROM key_value WHERE key=:key LIMIT 1", {"key": key})
        row = cursor.fetchone()
        con.close()

        self.logger.debug(f'Retrieved row: f{row}')

        if not row:
            return None

        value = row[1]
        decrypted_value = self._decrypt_value(value)
        return decrypted_value

    @requires_initialization
    def set_secure_value(self, key, value):
        self.logger.debug(f'Setting secure value for key {key}')
        epoch_seconds = time.time()
        encrypted_value = self._encrypt_value(value)
        con, cursor = self._db_cursor_and_connection()
        cursor.execute("INSERT INTO key_value VALUES (?, ?, ?) ON CONFLICT(key) DO UPDATE SET enc_value=excluded.enc_value", (key, encrypted_value, epoch_seconds))
        con.commit()
        con.close()

    @requires_initialization
    def clear_value(self, key):
        con, cursor = self._db_cursor_and_connection()
        cursor.execute("DELETE FROM key_value WHERE key=:key", {"key": key})
        con.commit()
        con.close()

    @requires_initialization
    def clear_all_values(self):
        con, cursor = self._db_cursor_and_connection()
        cursor.execute("DELETE FROM key_value")
        con.commit()
        con.close()
