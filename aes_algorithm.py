from Crypto.Cipher import AES
import scrypt
import os
import binascii


def encrypt_AES_GCM(data, password):
    kdf_salt = os.urandom(16)
    derived_key = scrypt.hash(password, kdf_salt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(derived_key, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(data)
    return (kdf_salt, ciphertext, aesCipher.nonce, authTag)


def decrypt_AES_GCM(encrypted_data, password):
    (kdfSalt, ciphertext, nonce, authTag) = encrypted_data
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    plaintext_str = str(plaintext, "utf-8")
    return plaintext_str


# msg = b'Message for AES-256-GCM + Scrypt encryption'
# password = b's3kr3tp4ssw0rd'
# encryptedMsg = encrypt_AES_GCM(msg, password)
# print("encryptedMsg", {
#     'kdfSalt': binascii.hexlify(encryptedMsg[0]),
#     'ciphertext': binascii.hexlify(encryptedMsg[1]),
#     'aesIV': binascii.hexlify(encryptedMsg[2]),
#     'authTag': binascii.hexlify(encryptedMsg[3])
# })


# decryptedMsg = decrypt_AES_GCM(encryptedMsg, password)
# print("decryptedMsg", decryptedMsg)

