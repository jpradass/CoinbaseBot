from typing import Dict, List
from coinbase.api import APIRequest
import json

PriceJSON = Dict[str, str]

class Price:
    """
    Get the total price to buy one token
    """
    resource = 'prices/{}/buy'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        self.base_coin = kwargs.get('base')
        self.currency = kwargs.get('currency')
        self.amount = kwargs.get('amount')

    def __str__(self) -> PriceJSON:
        return json.dumps({"base": self.base_coin, "currency": self.currency, "amount": self.amount})

    @classmethod
    def get_price(cls, pair_coin: str) -> "Price":
        res = APIRequest.get_request(cls.resource.format(pair_coin))
        return cls(**res['data'])

