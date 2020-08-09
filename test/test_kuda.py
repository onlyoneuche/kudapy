import pytest
from kudapy.base_api import kuda
from kudapy.utils import generate_id, get_request_reference, get_tracking_reference, load_private_key, load_public_key



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
    response = kuda(public_key, private_key, client_key)("CREATE_VIRTUAL_ACCOUNT", request_ref, {
        "email": "daon@gmail.com",
        "phoneNumber": "09034514310",
        "firstName": "kelechechukwu",
        "lastName": "Imman",
        "trackingReference": tracking_reference
        })

    assert response["Status"] == False


def test_user_can_make_name_enquiry():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()
    #tracking_reference = get_request_reference()
    response = kuda(public_key, private_key, client_key)("NAME_ENQUIRY", request_ref, {
        "beneficiaryAccountNumber": "2070527575",
        "bankCode": "033",
        # "senderTrackingReference": None
        })

    assert response["Status"] == True