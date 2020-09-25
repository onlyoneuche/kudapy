import math
import random
import string
import os


def generate_transaction_reference():
    """
    Generate transaction reference
    """
    return str(math.floor(random.random() * 1000000000000 + 1))


def generate_id(n, is_alphanum=True):
    """
    generate a random id of length n
    is_alphanum gives a random string of alphanumerals by default
    set is_alphanum to False for a random string of numbers

    """
    _id = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
    if is_alphanum:
        letters_and_digits = string.ascii_letters + string.digits
        _id = ''.join(random.choice(letters_and_digits) for i in range(0, n))
    return _id


def load_private_key(filepath):
    """
    load RSA private key in pem format
    """
    if not os.path.exists(filepath):
        raise ValueError("Private key file not found")
    with open(filepath, "rb") as key_file:
        private_key = key_file.read()
    return private_key


def load_public_key(filepath):
    """
    load RSA public key in pem format
    """
    if not os.path.exists(filepath):
        raise ValueError("Public key file not found")
    with open(filepath, "rb") as key_file:
        public_key = key_file.read()
    return public_key


def get_tracking_reference():
    return f"vAcc{generate_id(5)}"
