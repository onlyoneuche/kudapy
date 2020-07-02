from kuda_api import kuda
import math
import random
from utils import generate_id, load_private_key, load_public_key



client_key = "7QuX12xfmSpFl8d3a54b"

# load private and public keys
private_key = load_private_key()
public_key = private_key.public_key()

#generate a random request_reference id
request_ref = math.floor(random.random() * 1000000000000 + 1)

#generate a random tracking_reference id
short_ref_id = generate_id(5)
tracking_reference = f"vAcc{short_ref_id}"
print(tracking_reference)


kuda(public_key, private_key, client_key)("BANK_LIST", request_ref)
# kuda(public_key, private_key, client_key)("CREATE_VIRTUAL_ACCOUNT", request_ref, {
#     "email": "darlington@cowrywise.com",
#     "phoneNumber": "09068514310",
#     "firstName": "Uchechukwu",
#     "lastName": "Emmanuel",
#     "trackingReference": tracking_reference
# })
