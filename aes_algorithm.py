from Crypto.Cipher import AES
import scrypt
import os
import binascii


import hashlib
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes




# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization



def aes_encrypt(data, password):
    data = bytes(data, 'UTF-8')
    password = bytes(password, 'UTF-8')
    derived_key = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=32)
    iv = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=16)
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ##>>> iv = b64encode(cipher.iv).decode('utf-8')
    return b64encode(ct_bytes).decode('utf-8')
    #result = json.dumps({'iv':iv, 'ciphertext':ct})
    #print(ct)










# def encrypt_AES_GCM(data, password):
#     """
#     Encrypt data with password
#     password is public_key object
#     convert public_key to bytes
#     """
#     kdf_salt = os.urandom(16)
#     derived_key = scrypt.hash(password, kdf_salt, N=16384, r=8, p=1, buflen=32)
#     aesCipher = AES.new(derived_key, AES.MODE_GCM)
#     ciphertext, authTag = aesCipher.encrypt_and_digest(data)
#     return (base64.b64encode(kdf_salt), base64.b64encode(ciphertext), base64.b64encode(aesCipher.nonce), base64.b64encode(authTag))


# def decrypt_AES_GCM(encrypted_data, password):
#     """
#     Decrypt encrypted data with password
#     password is a combination of client_key and public key.
#     """
#     (kdfSalt, ciphertext, nonce, authTag) = encrypted_data
#     secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
#     aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
#     plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
#     plaintext_str = str(plaintext, "utf-8")
#     return plaintext_str