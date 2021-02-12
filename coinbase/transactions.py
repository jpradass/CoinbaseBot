from typing import Dict, List
import requests
from coinbase.exceptions import APIException
from coinbase.constants import COINBASE_API_URL
from coinbase.auth import auth

class Transaction:
    resource = 'accounts/{}/transactions'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        self.transaction_id = kwargs.get('id')
        self.transaction_type = kwargs.get('type')
        self.transaction_status = kwargs.get('status')
        self.transaction_crypto_amount = kwargs.get('amount')['amount']
        self.transaction_crypto_currency = kwargs.get('amount')['currency']
        self.transaction_native_amount = kwargs.get('native_amount')['amount']
        self.transaction_native_currency = kwargs.get('native_amount')['currency']

    @classmethod
    def list(cls, account_id) -> List["Transaction"]:
        res = requests.get(COINBASE_API_URL + cls.resource.format(account_id), auth=auth)
        if res.status_code != requests.codes.OK:
            raise APIException("There was some kind of problem with the request")
        return [cls(**transaction) for transaction in res.json()['data']]