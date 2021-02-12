from typing import List
import requests
from coinbase.exceptions import APIException
from coinbase.constants import COINBASE_API_URL
from coinbase.auth import auth

class Account:
    resource = 'accounts'

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.account_id = kwargs.get('id')
        self.account_code = kwargs.get('currency')['code']
        self.account_name = kwargs.get('currency')['name']
        self.account_amount = kwargs.get('balance')['amount']

    @classmethod
    def list(cls) -> List["Account"]:
        res = requests.get(COINBASE_API_URL + cls.resource, auth=auth)
        if res.status_code != requests.codes.OK:
            raise APIException("There was some kind of problem with the request")
        first_accounts = [cls(**account) for account in res.json()['data'] if float(account['balance']['amount']) != float(0)]

        res = requests.get(COINBASE_API_URL + cls.resource + f"?starting_after={res.json()['pagination']['next_starting_after']}", auth=auth)
        if res.status_code != requests.codes.OK:
            raise APIException("There was some kind of problem with the request")
        second_accounts = [cls(**account) for account in res.json()['data'] if float(account['balance']['amount']) != float(0)]

        return first_accounts + second_accounts

    