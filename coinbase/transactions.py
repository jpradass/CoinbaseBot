from coinbase.api import APIRequest
from typing import Dict, List

class Transaction:
    """
    Transaction resource represents an event on the account. It can be either negative or positive on 
    amount depending if it credited or debited funds on the account. If there’s another party, the transaction will have either to or from field. 
    For certain types of transactions, also linked resources with type value as field will be included in the payload (example buy and sell).
    """
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
    def list(cls, account_id: str) -> List["Transaction"]:
        res = APIRequest.get_request(cls.resource.format(account_id))
        return [cls(**transaction) for transaction in res['data']]
    
    @classmethod
    def make_transfer(cls, from_account: str, to_account: str, transfer_type: str, amount: str, currency: str) -> "Transaction":
        params = {
            "to": to_account,
            "type": transfer_type,
            "amount": amount,
            "currency": currency
        }
        res = APIRequest.post_request(cls.resource.format(from_account), params=params)
        return cls(**res['data'])