from coinbase.api import APIRequest
from typing import List

class Account:
    """
    Account resource represents all of a user’s accounts, including bitcoin, bitcoin cash, litecoin and 
    ethereum wallets, fiat currency accounts, and vaults. This is represented in the type field. 
    It’s important to note that new types can be added over time so you want to make sure this won’t break your implementation.
    """
    resource = 'accounts'

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.account_id = kwargs.get('id')
        self.account_code = kwargs.get('currency')['code']
        self.account_name = kwargs.get('currency')['name']
        self.account_amount = kwargs.get('balance')['amount']

    @classmethod
    def list(cls) -> List["Account"]:
        res = APIRequest.get_request(cls.resource)
        first_accounts = [cls(**account) for account in res['data'] if float(account['balance']['amount']) != float(0)]

        res = APIRequest.get_request(cls.resource + f"?starting_after={res['pagination']['next_starting_after']}")
        second_accounts = [cls(**account) for account in res['data'] if float(account['balance']['amount']) != float(0)]

        return first_accounts + second_accounts

    