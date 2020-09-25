from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


def rsa_encrypt(message, public_key):
    message = str.encode(message)
    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_v1_5.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    encrypted_text = base64.b64encode(encrypted_text)
    return encrypted_text


def rsa_decrypt(encrypted_text, private_key):
    encrypted_text = base64.b64decode(encrypted_text)
    sentinel = "an rsa_decryption error occured"
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_v1_5.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text, sentinel)
    return decrypted_text
