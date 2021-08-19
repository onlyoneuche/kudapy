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
            - email: user's email
            - phoneNumber: user's phone number
            - lastName: user's surname
            - firstName: user's firstname
        """
        service_name = "ADMIN_CREATE_VIRTUAL_ACCOUNT"
        kwargs.update({'trackingReference': get_tracking_reference()})
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def create_account_with_nuban(self, **kwargs):
        """
        Create a Kuda virtual account for a user.
        params:
            - email: user email
            - phoneNumber: user phone number
            - lastName: user's surname
            - firstName: user's firstname
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
            - beneficiaryAccountNumber: Nuban account number
            - beneficiaryBankCode: refer to bank list for appropiate bank codes
        """
        service_name = "NAME_ENQUIRY"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def transfer_funds(self, **kwargs):
        """
        Transfer funds to an account number
        params:
            - amount: Amount to transfer
            - beneficiaryName: Name of the recipient
            - beneficiaryAccount: Account number to credit
            - beneficiarybankCode: refer to bank list for appropiate bank codes
            - name_enquiry_id: ID of the name enquiry action
            - narration: Optional description of transfer
            - senderName: Name of the person sending money
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
  
    def retrieve_main_account_transactions(self, **kwargs):
        """
        retrieve a list of all transactions for the currently authenticated user
        params:
            - pageSize
            - pageNumber
        """
        service_name = "ADMIN_MAIN_ACCOUNT_TRANSACTIONS"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def filter_main_account_transactions(self, **kwargs):
        """
        retrieve a list of all transactions for the currently authenticated user, filtered by date
        params:
            - startDate
            - endDate
        """
        service_name = "ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def fund_virtual_account(self, **kwargs):
        """
        fund an existing virtual account through deposits from an associated KUDA account or\
        from any other Nigerian bank by transfer
        params:
            - trackingReference: tracking reference of the virtual account
            - amount: all amounts in kobo
            - narration [optional]

        """
        service_name = "FUND_VIRTUAL_ACCOUNT"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response

    def withdraw_from_virtual_account(self, **kwargs):
        """
        Withdrawing funds from a virtual account means to transfer funds from a virtual account \
        to an associated KUDA account or to any other Nigerian Bank account.
        params:
            - trackingReference: tracking reference of the virtual account
            - amount: all amounts in kobo
            - narration [optional]

        """
        service_name = "WITHDRAW_VIRTUAL_ACCOUNT"
        status, response = self._make_request(service_name, data=kwargs)
        return status, response