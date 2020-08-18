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
    tracking_reference = get_tracking_reference()

    with pytest.raises(KudaAPIException) as e_info:
        kuda(public_key, private_key, client_key)("CREATE_VIRTUAL_ACCOUNT", request_ref, {
        "email": "daon@gmail.com",
        "phoneNumber": "09034514310",
        "firstName": "kelechechukwu",
        "lastName": "Imman",
        "trackingReference": tracking_reference
        }) 

        assert e_info.value.args[0] == "You have signed up a customer with this phone number."

def test_user_can_create_account_with_nuban():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()
    response = kuda(public_key, private_key, client_key)("ONBOARDING", request_ref, {
        "gender": "Male",
        "address": "321 Hakeem Ipsum Street, Lagos Nigeria",
        "countryCode": "234",
        "email": "deleguwanemeka@gmail.com",
        "phoneNumber": "09090099999",
        "state": "Lagos",
        "city": "Ikeja",
        "lastName": "Emeka",
        "otherNames": "Igbondo"
    })

    assert response["Status"] == True

def test_user_can_make_name_enquiry():
    private_key = load_private_key()
    public_key = load_public_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()

    response = kuda(public_key, private_key, client_key)("NAME_ENQUIRY", request_ref, {
        "beneficiaryAccountNumber": "1100000734",
        "bankCode": "999129"
    })

    assert response["Status"] == True

def test_user_can_make_single_fund_transfer():
    public_key = load_public_key()
    private_key = load_private_key()
    client_key = "7QuX12xfmSpFl8d3a54b"
    request_ref = get_request_reference()
    #tracking_reference = get_tracking_reference()

    with pytest.raises(KudaAPIException) as e_info:
        kuda(public_key, private_key, client_key)("SINGLE_FUND_TRANSFER", request_ref, {
            "beneficiarybankCode": "999129",
            "tran_amount": "100",
            "beneficiaryAccount": "1100000734",
            "description": "test",
            "nameEnquiryID": 1
            })

    assert e_info.value.args[0] == "Initializing"