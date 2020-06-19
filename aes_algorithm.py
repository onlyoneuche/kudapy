from Crypto.Cipher import AES
import scrypt
import os
import binascii

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def encrypt_AES_GCM(data, password):
    """
    Encrypt data with password
    password is public_key object
    convert public_key to bytes
    """
    kdf_salt = os.urandom(16)
    derived_key = scrypt.hash(password, kdf_salt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(derived_key, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(data)
    return (kdf_salt, ciphertext, aesCipher.nonce, authTag)


def decrypt_AES_GCM(encrypted_data, password):
    """
    Decrypt encrypted data with password
    password is a combination of client_key and public key.
    """
    (kdfSalt, ciphertext, nonce, authTag) = encrypted_data
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    plaintext_str = str(plaintext, "utf-8")
    return plaintext_str