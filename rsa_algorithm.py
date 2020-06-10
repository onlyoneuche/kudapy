from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def rsa_encrypt(message, public_key):
	ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
        )
    )


def rsa_decrypt(ciphertext, private_key):
	plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )



# def rsa_encrypt(data, public_key):
#     public_key = RSA.import_key(public_key)
#     encryptor = PKCS1_OAEP.new(public_key)
#     encrypted = encryptor.encrypt(data)
#     return binascii.hexlify(encrypted)


# def rsa_decrypt(encypted_data, private_key):
#     decryptor = PKCS1_OAEP.new(private_key)
#     decrypted = decryptor.decrypt(encypted_data)
#     decrypted_str = str(decrypted, "utf-8")
#     return decrypted_str