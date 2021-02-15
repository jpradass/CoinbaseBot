from typing import Dict, List
from coingecko.api import APIRequest
import json

"https://api.coingecko.com/api/v3/coins/chainlink/market_chart/range?vs_currency=eur&from=1613326760&to=1613334016"
class Coin:
    resource = 'coins/{}/market_chart/range'

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        self.coin_prices = kwargs.get('prices')
        self.coin_marketcaps = kwargs.get('market_caps')
        self.coin_totalvolumes = kwargs.get('total_volumes')
    
    def __str__(self) -> str:
        return json.dumps({"prices": self.coin_prices, "market_caps": self.coin_marketcaps, "total_volumes": self.coin_totalvolumes})

    @classmethod
    def getcoin_range(cls, coin_id: str, currency: str, from_date: str, to_date: str) -> "Coin":
        """
        get prices, market_caps and total_volumes from a given coin vs fiat currency
        """
        res = APIRequest.get_request(cls.resource.format(coin_id) + f'?vs_currency={currency}&from={from_date}&to={to_date}')
        return cls(**res)