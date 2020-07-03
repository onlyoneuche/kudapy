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

        mypass = f"Password: {password}"
        print(mypass)
        # aes encryption of payload with password
        payload = json.dumps(payload)
        print("payload: ", payload)
        #payload_to_bytes = bytes(payload, "utf-8")
        encrypted_payload = aes_encrypt(payload, password)
        payload_json = json.loads(encrypted_payload)
        #iv = encrypted_payload['iv']
        ciphertext = payload_json['ciphertext']
        ciphertext = json.dumps(ciphertext)
        print("ciphertext",ciphertext)
        print("encrypted_payload: ", ciphertext)


        # rsa encryption of password wih public key
        #password_to_bytes = bytes(password, "utf-8")
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

        # encrypted_password = base64.b64decode(encrypted_password)
        # print("decoded passord", encrypted_password)
        # decrypted_password = rsa_decrypt(encrypted_password, private_key)
        # print("decrypted_password", decrypted_password)

        # decrypted_payload = aes_decrypt(encrypted_payload, decrypted_password)
        # print("decrypted_payload", decrypted_payload)



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