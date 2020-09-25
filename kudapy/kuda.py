from .base_api import BaseAPI
from .utils import get_tracking_reference


class Kuda(BaseAPI):

    def bank_list(self):
        """
        Get a list of supported banks you can transfer to
        """
        service_name = "BANK_LIST"
        status, response = self._make_request(service_name)
        return status, response

    def create_virtual_account(self, email, phone_number, last_name,
                               first_name):
        """
        Create a Kuda virtual account for a user.
        params:
            - email: user email
            - phonenumber: user phone number
            - lastname: user's surname
            - firstname: user's firstname
        """
        service_name = "CREATE_VIRTUAL_ACCOUNT"
        data = {
            "email": email,
            "phoneNumber": phone_number,
            "lastName": last_name,
            "firstName": first_name,
            "trackingReference": get_tracking_reference()
        }
        status, response = self._make_request(service_name, data)
        return status, response

    def create_account_with_nuban(self, email, phone_number, last_name,
                                  first_name, other_names, gender,
                                  city, address, state, country_code):
        """
        Create a Kuda virtual account for a user.
        params:
            - email: user email
            - phone_number: user phone number
            - lastname: user's surname
            - firstname: user's firstname
            - other_names: Middle name
            - gender: Gender
            - city: City
            - address: Full address
            - state: State
            - country_code: Country Code
        """
        service_name = "ONBOARDING"
        data = {
            "email": email,
            "phoneNumber": phone_number,
            "lastName": last_name,
            "firstName": first_name,
            "otherNames": other_names,
            "gender": gender,
            "city": city,
            "address": address,
            "state": state,
            "countryCode": country_code
        }
        status, response = self._make_request(service_name, data)
        return status, response

    def name_enquiry(self, account_number, bank_code):
        """
        Resolve an account number into an account name
        params:
            - account_number: Nuban account number
            - bank code: refer to bank list for appropiate bank codes
        """
        service_name = "NAME_ENQUIRY"
        data = {
            "beneficiaryAccountNumber": account_number,
            "bankCode": bank_code,
            "senderTrackingReference": None
        }
        status, response = self._make_request(service_name, data)
        return status, response

    def transfer_funds(self, amount, account_number, bank_code,
                       name_enquiry_id, description=None):
        """
        Transfer funds to an account number
        params:
            - amount: Amount to transfer
            - account_number: Account number to credit
            - bank_code: refer to bank list for appropiate bank codes
            - name_enquiry_id: id of the name enquiry action
            - description: optional description of transfer
        """
        service_name = "SINGLE_FUND_TRANSFER"
        data = {
            "beneficiaryAccount": account_number,
            "beneficiarybankCode": bank_code,
            "nameEnquiryID": name_enquiry_id,
            "description": description,
            "tran_amount": amount,
        }
        status, response = self._make_request(service_name, data)
        return status, response
