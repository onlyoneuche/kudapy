import requests
import json
from aes_algorithm import  aes_encrypt, aes_decrypt #encrypt_AES_GCM, decrypt_AES_GCM
from rsa_algorithm import rsa_encrypt, rsa_decrypt
from Crypto.PublicKey import RSA
from utils import generate_id
import base64



def kuda(public_key, private_key, client_key):
    def make_kuda_request(service_type, request_ref, data=None):
        short_id = generate_id(5, is_alphanum=True)
        password = f"{client_key}-{short_id}"

        endpoint = "https://kudaopenapi.azurewebsites.net/v1"

        payload = {
                "serviceType": service_type,
                "requestRef": request_ref,
                "data": data
                }

        # aes encryption of payload with password
        payload = json.dumps(payload)
        print("payload: ", payload)
        #payload_to_bytes = bytes(payload, "utf-8")
        encrypted_payload = aes_encrypt(payload, password)
        print("encrypted_payload", encrypted_payload)
        encrypted_payload_json = json.loads(encrypted_payload)
        iv = encrypted_payload_json['iv']
        print("iv", iv)
        ciphertext = encrypted_payload_json['ciphertext']
        print("ciphertext",ciphertext)


        # rsa encryption of password wih public key
        print("--------------------------------------------------------")
        print("password: ", password)
        print('----------')
        print("public_key: ", public_key)
        print('----------')
        print("private_key: ", private_key)
        print("--------------------------------------------------------")
        encrypted_password = rsa_encrypt(password, public_key)
        print("--------------------------------------------------------")
        print("encrypted_password: ", encrypted_password)
        print("--------------------------------------------------------")



        headers = {
            "password": encrypted_password,
        }
        payload_ = {
            "data":ciphertext
        }
        encrypted_response = requests.post(
            endpoint, json=payload_,
            headers=headers
            )

        # RSA decrypt password with our privateKey
        print("------------------------------------------")
        print("encrypted_json", encrypted_response)
        print("encrypted_headers: ", encrypted_response.headers)


        


        encrypted_response = encrypted_response.text
        encrypted_response = json.loads(encrypted_response)
        encrypted_password = encrypted_response["password"]
        encrypted_data = encrypted_response["data"]

        print("encrypted_response", encrypted_response)
        print("encrypted_password", encrypted_password)
        print("encrypted_data", encrypted_data)

        decrypted_password = rsa_decrypt(encrypted_password, private_key)
        print("decrypted_password", decrypted_password)

        # decrypted_password_str = str(decrypted_password, "utf-8")

        #AES decrypt data with password
        decrypted_data = aes_decrypt(encrypted_data, decrypted_password)
        print("decrypted_data", decrypted_data)
        # data_str = str(data, "utf-8")
        # parsed_data = json.loads(data)
        # return parsed_data

    return make_kuda_request