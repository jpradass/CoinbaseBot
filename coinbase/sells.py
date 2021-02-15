from typing import Dict, List
from coinbase.api import APIRequest

class Sell:
    """
    Sell resource represents a sell of bitcoin, bitcoin cash, litecoin or ethereum using a payment method (either a bank or a fiat account). 
    Each committed sell also has an associated transaction.
    """
    resource = 'accounts/{}/sells'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        self.sell_id = kwargs.get('id')
        self.sell_status = kwargs.get('status')
        self.sell_amount = kwargs.get('amount')['amount']
        self.sell_currency = kwargs.get('amount')['currency']
        self.sell_resource = kwargs.get('resource')
        self.sellfee_amount = kwargs.get('fee')['amount']
        self.sellfee_currency = kwargs.get('fee')['currency']

    @classmethod
    def sell_order(cls, account_id: str, amount: str, currency: str, payment_method: str) -> "Sell":
        params = {
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method
        }
        res = APIRequest.post_request(resource=cls.resource.format(account_id), params=params)
        return cls(**res['data'])