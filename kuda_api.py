import requests
import json
from aes_algorithm import  aes_encrypt #encrypt_AES_GCM, decrypt_AES_GCM
from rsa_algorithm import rsa_encrypt, rsa_decrypt
from Crypto.PublicKey import RSA
from utils import generate_id
import base64



def kuda(public_key, private_key, client_key):
    def make_kuda_request(service_type, request_ref, data):
        short_id = generate_id(5, is_alphanum=True)
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
        payload = json.dumps(payload)
        print("payload: ", payload)
        #payload_to_bytes = bytes(payload, "utf-8")
        encrypted_payload = aes_encrypt(payload, password)
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
        print("encrypted_json", encrypted_response)
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