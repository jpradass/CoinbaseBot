from typing import Dict, List
from coinbase.api import APIRequest

class Buy:
    resource = 'accounts/{}/buys'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        pass

    @classmethod
    def buy_order(cls) -> None:
        pass
