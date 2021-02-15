from typing import Dict, List
from coinbase.api import APIRequest


class Payment:
    """
    Payment method resource represents the different kinds of payment methods that can be used 
    when buying and selling bitcoin, bitcoin cash, litecoin or ethereum.
    """
    resource = 'payment-methods'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        self.payment_id = kwargs.get('id')
        self.payment_type = kwargs.get('type')
        self.payment_name = kwargs.get('name')
        self.payment_currency = kwargs.get('currency')
        

    @classmethod
    def list(cls) -> List["Payment"]:
        res = APIRequest.get_request(cls.resource)
        return [cls(**payment) for payment in res['data']]
