import pytest
from kudapy.base_api import kuda
from kudapy.exceptions import KudaAPIException
from kudapy.utils import generate_id, get_request_reference, get_tracking_reference, load_private_key, load_public_key


def test_api_raises_exception_for_invalid_credentials():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()
    with pytest.raises(KudaAPIException):
        kuda(public_key, private_key, client_key)("Invalid Service Type", request_ref)

def test_user_can_fetch_bank_list():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()
    response = kuda(public_key, private_key, client_key)("BANK_LIST", request_ref)
    #response = response.json()

    assert response["Message"] == "Completed Successfully"

def test_user_can_create_virtual_account():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()
    tracking_reference = get_request_reference()

    with pytest.raises(KudaAPIException) as e:
        kuda(public_key, private_key, client_key)("CREATE_VIRTUAL_ACCOUNT", request_ref, {
        "email": "daon@gmail.com",
        "phoneNumber": "09034514310",
        "firstName": "kelechechukwu",
        "lastName": "Imman",
        "trackingReference": tracking_reference
        }) 

        assert e.value.args[0] == "You have signed up a customer with this phone number."