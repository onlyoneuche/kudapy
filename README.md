# kudapy

Python wrapper for making secure requests to Kuda API

## Getting started
> - register on kuda bank website to recieve public and private keys in xml format
> - paste your private and public keys (both in PEM format) in your project directory
	- both keys come in XML format(YOU NEED TO CONVERT FROM XML TO PEM)
> - Your client key is the name of your private key file sent after registration on kuda bank website.

## Installation

 `pip install kudapy`


### Making a request

```py
from kudapy import kuda

"""
Save your public and private pem file somewhere on the filesystem. Specify the full path to your keys
then create a Kuda Object instance. Also provide a client key string and base url (for production).
"""

kuda_instance = Kuda(path_to_public_key, path_to_private_key, client_key_string, base_url)


#Use the kuda instance to call the appropiate methods of the 
#action you want to perform.

#For available actions run help(kuda)

```

### Sample requests

```py

# List of banks
kuda_instance.bank_list()

-------------------------

# Name enquiry
kuda_instance.name_enquiry("1100000734", "999129")

-------------------------

# Create a virtual account 
# (Provide email, phone, lastname, firstname)

kuda_instance.create_virtual_account(
    "okonkwo_yusuf@kudabank.com", 
    "07011111111",
    "Okonkwo",
    "Yusuf"
)
--------------

## Expected response is decrypted data from Kuda API in JSON

"""
You get back two values from the method calls, status and data. If status is true, there is a valid response data else
the status will be False - with data being the error message.
"""

status, data = kuda_instance.bank_list()
(True, {'Status': True, 'Message': 'Completed Successfully', ...})

or
status, data = kuda_instance.name_enquiry('0000000000', 999000')
(False, 'Cannot validate account number at this time, Please try again')

```

## Contribution & Issues

- Simply **fork the repo**, make changes and **make a pull request**
- You can open an issue for support or suggestions

## Author

- [Uchechukwu Darlington Emmanuel](https://github.com/daleentontech)

## Contributor

- [Edward Popoola](https://github.com/erdypee)

# Acknowledgements

- Kuda Bank Team
- Cowrywise Team
