# kudapy

Python wrapper for making secure request to Kuda API

## Getting started

> - paste your private and public key (both in PEM format) in your project directory
	- both keys come in XML format(YOU NEED TO CONVERT FROM XML TO PEM)
> - Your client key is the name of your private key file

## Using the library

While the repo is not yet on pypi, simply clone this repo and run `pipenv install`

### Library setup

```py
from base_api import kuda
import math
import random
from utils import generate_id, load_private_key, load_public_key



client_key = "name-of-private-key-file"

# load private and public keys
private_key = load_private_key()
public_key = load_public_key()


kuda = kuda(public_key, private_key, client_key) # this initializes the Kuda function
```

### Making a request

```py
kuda(service_type, request_ref, data)
```

### Sample request

```py
# Bank List

#generate a random request_reference
request_ref = math.floor(random.random() * 1000000000000 + 1)

kuda(public_key, private_key, client_key)("BANK_LIST", request_ref)

# expected response is decrypted data from Kuda API


```


> Refer to the Kuda Bank API documentation for respective SERVICE TYPES and DATA TYPES

## Contribution & Issues

- Simply **fork the repo**, make changes and **make a pull request**
- You can open an issue for support or suggestions

## Author

- [Uchechukwu Darlington Emmanuel](https://github.com/daleentontech)

# Acknowledgements

- Kuda Bank Team
- Cowrywise Team
