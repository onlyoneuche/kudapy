from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import base64


def rsa_encrypt(message, public_key):
    """
    encrypt message with RSA public key
    """
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
        )
    )
    return base64.b64encode(ciphertext)
    #return ciphertext

def rsa_decrypt(ciphertext, private_key):
    """
    decrypt encrypted message with RSA private key
    """
    plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
