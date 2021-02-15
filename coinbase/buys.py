from typing import Dict, List
from coinbase.api import APIRequest

class Buy:
    """
    Sell resource represents a sell of bitcoin, bitcoin cash, litecoin or ethereum using a 
    payment method (either a bank or a fiat account). Each committed sell also has an associated transaction.
    """
    resource = 'accounts/{}/buys'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        self.buy_id = kwargs.get('id')
        self.buy_status = kwargs.get('status')
        self.buy_amount = kwargs.get('amount')['amount']
        self.buy_currency = kwargs.get('amount')['currency']
        self.buy_resource = kwargs.get('resource')
        self.buyfee_amount = kwargs.get('fee')['amount']
        self.buyfee_currency = kwargs.get('fee')['currency']

    @classmethod
    def buy_order(cls, account_id: str, amount: str, currency: str, payment_method: str) -> "Buy":
        params = {
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method
        }
        res = APIRequest.post_request(resource=cls.resource.format(account_id), params=params)
        return cls(**res['data'])

