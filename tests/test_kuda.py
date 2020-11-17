import pytest
import random
from kudapy import Kuda
from kudapy.exceptions import KudaAPIException

test_private_key = 'tests/test_c_private.pem'
test_public_key = 'tests/test_c_public.pem'
test_client_key = "7QuX12xfmSpFl8d3a54b"


@pytest.fixture(scope="module")
def kuda_instance():
    k_instance = Kuda(test_public_key, test_private_key, test_client_key)
    return k_instance


def test_initialization(kuda_instance):
    assert kuda_instance is not None


def test_initialization_exception_no_parameters():
    with pytest.raises(KudaAPIException):
        Kuda(None, None, None)


def test_fetch_bank_list(kuda_instance):
    status, response = kuda_instance.bank_list()
    assert status
    assert response["Message"] == "Completed Successfully"


def test_create_virtual_account(kuda_instance):
    random_email = "dao{}@gmail.com".format(random.randint(100, 5000))
    random_phone = "080{}".format(random.randint(1000000, 9999999))
    status, response = kuda_instance.create_virtual_account(random_email,
                                                            random_phone, "kelechechukwu", "Imman")
    assert status
    assert response["Message"] == "Successful"


def test_name_enquiry(kuda_instance):
    status, response = kuda_instance.name_enquiry("1100000734", "999129")
    assert status


"""
def test_create_account_with_nuban():
    k_instance = Kuda(test_public_key, test_private_key, test_client_key)
    random_email = "dao{}@gmail.com".format(random.randint(100, 5000))
    random_phone = "080{}".format(random.randint(1000000, 9999999))
    status, response = k_instance.create_account_with_nuban(random_email,
        random_phone, "kelechechukwu", "Imman", "James", "Male", "Ikeja",
        "10 Aso Rock Street, Lagos", "Lagos", "234")
    assert status

def test_user_can_make_single_fund_transfer():
    k_instance = Kuda(test_public_key, test_private_key, test_client_key)
    status, response = k_instance.transfer_funds("100", "1100000734", "999129", "1", "tests")
    assert status
       
"""
