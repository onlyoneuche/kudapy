from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def rsa_encrypt(data, public_key):
    public_key = RSA.import_key(public_key)
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(data)
    return binascii.hexlify(encrypted)

# msg = b'A message for encryption'
# encryptor = PKCS1_OAEP.new(pubKey)
# encrypted = encryptor.encrypt(msg)
# print("Encrypted:", binascii.hexlify(encrypted))


def rsa_decrypt(encypted_data, private_key):
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(encypted_data)
    decrypted_str = str(decrypted, "utf-8")
    return decrypted_str


# decryptor = PKCS1_OAEP.new(keyPair)
# decrypted = decryptor.decrypt(encrypted)
# print('Decrypted:', decrypted)
