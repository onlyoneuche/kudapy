import requests
import json
from kudapy.algorithms.aes_algorithm import  aes_encrypt, aes_decrypt
from kudapy.algorithms.rsa_algorithm import rsa_encrypt, rsa_decrypt
from kudapy.utils import generate_id



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
        encrypted_payload = aes_encrypt(payload, password)
        encrypted_payload_json = json.loads(encrypted_payload)
        iv = encrypted_payload_json['iv']
        ciphertext = encrypted_payload_json['ciphertext']


        # rsa encryption of password wih public key
        encrypted_password = rsa_encrypt(password, public_key)

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
        encrypted_response = encrypted_response.text
        encrypted_response = json.loads(encrypted_response)
        encrypted_password = encrypted_response["password"]
        encrypted_data = encrypted_response["data"]

        decrypted_password = rsa_decrypt(encrypted_password, private_key)

        #AES decrypt data with password
        decrypted_data = aes_decrypt(encrypted_data, decrypted_password)
        print("decrypted_data", decrypted_data)

    return make_kuda_request