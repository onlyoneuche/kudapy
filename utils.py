from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

import random
import string


def generate_id(n, is_alphanum=True):
    """
    >>generate a random short_id of length n
    >>is_letters gives a random string of letters by default
    >>set is_letters to False for a random string of numbers

    """
    _id = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
    if is_alphanum:
        letters_and_digits = string.ascii_letters + string.digits
        _id = ''.join(random.choice(letters_and_digits) for i in range(0, n))
    return _id


# load private key
def load_private_key():
    with open("./private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

# load public key 
# with open("./public.pem", "rb") as key_file:
#     public_key = load_pem_public_key(key_file.read(), backend=default_backend())