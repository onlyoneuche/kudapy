import pytest
from kudapy.base_api import kuda
import math
import random
from kudapy.utils import generate_id, load_private_key, load_public_key



def test_user_can_fetch_bank_list():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = math.floor(random.random() * 1000000000000 + 1)
    response = kuda(public_key, private_key, client_key)("BANK_LIST", request_ref)
    #response = response.json()

    assert response["Message"] == "Completed Successfully"