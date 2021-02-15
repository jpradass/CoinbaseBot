from coingecko.coin import Coin

class CoinGecko:
    def __init__(self) -> None:
        pass

    def coin_range(self, coin_id: str, currency: str, from_date: str, to_date: str) -> Coin:
        """
        Returns coin prices with given date range in timestamp format
        """
        return Coin.getcoin_range(coin_id, currency, from_date, to_date)