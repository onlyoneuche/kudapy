import os
import requests
import json
from .algorithms.aes_algorithm import aes_encrypt, aes_decrypt
from .algorithms.rsa_algorithm import rsa_encrypt, rsa_decrypt
from .exceptions import KudaAPIException
from .utils import load_private_key, generate_id, \
    load_public_key, generate_transaction_reference


class BaseAPI:
    """
    Specify the full path to your public and private keys to
    create a Kuda object instance. Also provide a client key string
    and base url (for tests or production).

    params:
        - public_keyfile: Full path to your public key pem file
        - private_keyfile: Full path to your private key pem file
        - client_key: Your client key
        - base_url for production else, its tests
    """

    _BASE_URL = "https://kudaopenapi.azurewebsites.net/v1"

    def __init__(self, public_keyfile, private_keyfile, client_key, base_url=None):

        if None in (public_keyfile, private_keyfile, client_key):
            raise KudaAPIException("Public, private and client keys are required.")
        if not os.path.exists(private_keyfile):
            raise KudaAPIException("Missing private key file")
        if not os.path.exists(public_keyfile):
            raise KudaAPIException("Missing public key file")

        self._private_key = load_private_key(private_keyfile)
        self._public_key = load_public_key(public_keyfile)

        self._client_key = client_key
        self._password = "{}-{}".format(self._client_key, generate_id(5, is_alphanum=True))
        self._base_url = base_url if base_url else BaseAPI._BASE_URL

    def _make_request(self, service_name, data=None):

        payload = {
            "serviceType": service_name,
            "requestRef": generate_transaction_reference(),
            "data": data
        }

        # aes encryption of payload with password
        payload = json.dumps(payload)
        print(payload)
        encrypted_payload = aes_encrypt(payload, self._password)
        encrypted_payload_json = json.loads(encrypted_payload)
        ciphertext = encrypted_payload_json['ciphertext']

        # rsa encryption of password wih public key
        encrypted_password = rsa_encrypt(self._password, self._public_key)

        headers = {
            "password": encrypted_password,
        }
        payload_ = {
            "data": ciphertext
        }
        encrypted_response = requests.post(
            self._base_url, json=payload_,
            headers=headers
        )

        # RSA decrypt password with our privateKey
        encrypted_response = encrypted_response.text
        encrypted_response = json.loads(encrypted_response)

        try:
            encrypted_password = encrypted_response["password"]
            encrypted_data = encrypted_response["data"]
        except KeyError as ke:
            raise KudaAPIException("Invalid Credentials", ke)

        decrypted_password = rsa_decrypt(encrypted_password, self._private_key)

        # AES decrypt data with password
        decrypted_data = aes_decrypt(encrypted_data, decrypted_password)
        decrypted_data = str(decrypted_data, 'utf-8')

        response = json.loads(decrypted_data)
        print(response)
        if response["Status"]:
            return response["Status"], response
        return False, response["Message"]
