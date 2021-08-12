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

    def create_virtual_account(self, **kwargs):
        """
        Create a Kuda virtual account for a user.
        params:
            - email: user email
            - phonenumber: user phone number
            - lastname: user's surname
            - firstname: user's firstname
        """
        service_name = "CREATE_VIRTUAL_ACCOUNT"
        kwargs.update({'trackingReference': get_tracking_reference()})
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def create_account_with_nuban(self, **kwargs):
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
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def name_enquiry(self, **kwargs):
        """
        Resolve an account number into an account name
        params:
            - account_number: Nuban account number
            - bank code: refer to bank list for appropiate bank codes
        """
        service_name = "NAME_ENQUIRY"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def transfer_funds(self, **kwargs):
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
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def retrieve_transaction_logs(self, **kwargs):
        """
        Get a list of all your transactions carried out
        params:
            - RequestReference
            - ResponseReference
            - FetchSuccessfulRecords: if set to true, only successful transactions will be retrieved
            - TransactionDate
        """
        service_name = "RETRIEVE_TRANSACTION_LOGS"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def retrieve_virtual_account_balance(self, **kwargs):
        """
        retrieve the balance status of a virtual account
        params:
            - trackingReference: tracking reference of the virtual account [optional]
        """
        service_name = "RETRIEVE_VIRTUAL_ACCOUNT_BALANCE"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response
  
