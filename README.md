# kudapy

Python wrapper for making secure requests to Kuda API

## Getting started
> - register on kuda bank website to recieve public and private keys in xml format
> - paste your private and public keys (both in PEM format) in your project directory
	- both keys come in XML format(YOU NEED TO CONVERT FROM XML TO PEM)
> - Your client key is the name of your private key file sent after registration on kuda bank website.

## Installation

 `pip install kudapy`

### Library setup

```py
from kudapy.base_api import kuda
import math
import random
from kuda.utils import generate_id, load_private_key, load_public_key



client_key = "name-of-private-key-file"

# load private and public keys

"""
kuda.utils contains 3 utility functions: generate_id, load_private_key and load_public_key
these are not required but would make life easier
"""

private_key = load_private_key() #you have to rename your private key .pem file to private.pem
public_key = load_public_key()	#you have to rename your public key .pem file to public.pem

```

### Making a request

```py

#the kuda function expects at most 3 parameters: service_type, request_ref and data
#not all requests require the last parameter (data). see sample request below.


kuda(service_type, request_ref, data)
```
> Refer to the Kuda Bank API documentation for respective SERVICE TYPES and DATA TYPES

### Sample requests

```py
# Bank List

#generate a random request_reference
request_ref = math.floor(random.random() * 1000000000000 + 1)

kuda(public_key, private_key, client_key)("BANK_LIST", request_ref)


#-------------------------------------------------------------------

#Create a Virtual Account

#generate a random request_reference
request_ref = math.floor(random.random() * 1000000000000 + 1)

#generate a random tracking_reference id
short_ref_id = generate_id(5)
tracking_reference = f"vAcc{short_ref_id}"


kuda(public_key, private_key, client_key)("CREATE_VIRTUAL_ACCOUNT", request_ref, {
    "email": "okonkwo_yusuf@kudabank.com",
    "phoneNumber": "07011111111",
    "firstName": "Okonkwo",
    "lastName": "Yusuf",
    "trackingReference": tracking_reference
})


## expected response is decrypted data from Kuda API in JSON

```

## Contribution & Issues

- Simply **fork the repo**, make changes and **make a pull request**
- You can open an issue for support or suggestions

## Author

- [Uchechukwu Darlington Emmanuel](https://github.com/daleentontech)

# Acknowledgements

- Kuda Bank Team
- Cowrywise Team
