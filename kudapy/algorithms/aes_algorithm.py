import hashlib
import json
import sys
from base64 import b64encode, b64decode
if sys.platform == 'darwin':
    from Cryptodome.Cipher import AES
else:
    from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(data, password):
    data = bytes(data, 'UTF-8')
    password = bytes(password, 'UTF-8')
    derived_key = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=32)
    iv = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=16)
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv': iv, 'ciphertext': ct})
    return result


def aes_decrypt(encrypted_data, password):
    derived_key = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=32)
    iv = hashlib.pbkdf2_hmac('sha1', password, b'randomsalt', 1000, dklen=16)
    ct = b64decode(encrypted_data)
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt