import requests
import random
import string
import json
from aes_algorithm import encrypt_AES_GCM, decrypt_AES_GCM
from rsa_algorithm import rsa_encrypt, rsa_decrypt
from Crypto.PublicKey import RSA

from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization



def kuda(public_key, private_key, client_key):
    # generate a random short_id
    letters = string.ascii_letters
    short_id = ''.join(random.choice(letters) for i in range(0, 5))

    def make_kuda_request(service_type, request_ref, data):
        password = f"{client_key}-{short_id}"

        endpoint = "https://kudaopenapi.azurewebsites.net/v1"

        payload = {
                "service_type": service_type,
                "request_ref": request_ref,
                "data": data
                }
        
        mypass = f"Password: {password}"
        print(mypass)
        # aes encryption of payload with password
        payload = str(payload)
        payload_to_bytes = bytes(payload, "utf-8")
        encrypted_payload = encrypt_AES_GCM(payload_to_bytes, password)
        print("encrypted_payload: ", encrypted_payload)


        # rsa encryption of password wih public key
        password_to_bytes = bytes(password, "utf-8")
        print("--------------------------------------------------------")
        print("password_to_bytes: ", password_to_bytes)
        print('----------')
        print("public_key: ", public_key)
        print('----------')
        print("private_key: ", private_key)
        print("--------------------------------------------------------")
        encrypted_password = rsa_encrypt(password_to_bytes, public_key)
        print("--------------------------------------------------------")
        print("encrypted_password: ", encrypted_password)
        print("--------------------------------------------------------")

        headers = {
            "password": encrypted_password,
        }
        encrypted_response = requests.post(
            endpoint, json=str(encrypted_payload),
            headers=headers
            )

        # RSA decrypt password with our privateKey
        print("encrypted_response: ", encrypted_response.text)
        print("encrypted_headers: ", encrypted_response.headers)

        # decrypted_password = rsa_decrypt(
        #     encrypted_response.password, private_key)

        # decrypted_password_str = str(decrypted_password, "utf-8")

        # # AES decrypt data with plaintext
        # data = decrypt_AES_GCM(encrypted_response.data, decrypted_password_str)
        # data_str = str(data, "utf-8")
        # parsed_data = json.loads(data)
        # return parsed_data
    return make_kuda_request




# load parameters
client_key = "7QuX12xfmSpFl8d3a54b"

# load public key 
with open("./public.pem", "rb") as key_file:
    public_key = load_pem_public_key(key_file.read(), backend=default_backend())

# load private key
with open("./private.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )


#generate a random tracking_reference and request reference
n = 11
request_ref = ''.join(["{}".format(random.randint(0, 9))
                       for num in range(0, n)])
short_ref_id = ''.join(["{}".format(random.randint(0, 9))
                        for num in range(0, 5)])

tracking_reference = f"vAcc{short_ref_id}"

# pub_key_bytes = bytes(public_key, "utf-8")
# priv_key_bytes = bytes(private_key, "utf-8")

kuda(public_key, private_key, client_key)("CREATE_VIRTUAL_ACCOUNT", request_ref, {
    "email": "darlington@cowrywise.com",
    "phoneNumber": "09068514310",
    "firstName": "Uchechukwu",
    "lastName": "Emmanuel",
    "trackingReference": tracking_reference
})