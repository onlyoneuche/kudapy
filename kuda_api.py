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
        #payload_json = json.loads(encrypted_payload)
        #iv = encrypted_payload['iv']
        #ciphertext = payload_json['ciphertext']
        #ciphertext = json.dumps(ciphertext)
        #print("ciphertext",encrypted_payload)
        print("encrypted_payload: ", encrypted_payload)


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
        #decrypted_password = rsa_decrypt(encrypted_password, private_key)
        # print("decrypted_password", decrypted_password)

        # decrypted_payload = aes_decrypt(encrypted_payload, decrypted_password)
        # print("decrypted_payload", decrypted_payload)



        headers = {
            "password": encrypted_password,
        }
        payload_ = {
            "data":encrypted_payload
        }
        encrypted_response = requests.post(
            endpoint, json=payload_,
            headers=headers
            )

        # RSA decrypt password with our privateKey
        print("encrypted_response: ", encrypted_response.text)
        print("encrypted_json", encrypted_response)
        print("encrypted_headers: ", encrypted_response.headers)




        encrypted_response = 
        iv = encrypted_payload['iv']
        ciphertext = payload_json['ciphertext']
        ciphertext = json.dumps(ciphertext)
        print("ciphertext",encrypted_payload)

        #decrypted_password = rsa_decrypt(
        #    "npMPnhFFnV4j/tDiUAs/jir4zVbueoXZMHiug3Re+dIyrnBedElFn9auQhGEx+LmTrzuy1+6Sr7t7ZRzVUDCmRvXWBujtwAE1ngpZz/5DPiWxiuv4VFlVF19UQXSTeh4BRkP633zuE40fPX5fQUWaMXbQ6A3qrK+CQv3XzsqPQo=", private_key)

        #print("decrypted_password", decrypted_password)

        # decrypted_password_str = str(decrypted_password, "utf-8")

        # # AES decrypt data with plaintext
        #data = aes_decrypt("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", b'TCn6Ap0foM')
        # data_str = str(data, "utf-8")
        # parsed_data = json.loads(data)
        # return parsed_data

    return make_kuda_request