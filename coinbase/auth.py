import hmac, hashlib, time
from typing import Any
from requests.auth import AuthBase
from coinbase.constants import API_KEY, API_SECRET, API_VERSION

class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key: str, secret_key: str, cb_version: str) -> None:
        self.api_key = api_key
        self.secret_key = secret_key
        self.cb_version = cb_version

    def __call__(self, request: Any) -> Any:
        timestamp = str(int(time.time()))
        message = timestamp + request.method + request.path_url + (request.body or '')
        signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-VERSION': self.cb_version,
        })
        return request

auth = CoinbaseWalletAuth(API_KEY, API_SECRET, API_VERSION)