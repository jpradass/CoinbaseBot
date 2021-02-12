from typing import Dict
from coinbase.auth import auth
from coinbase.constants import COINBASE_API_URL
from coinbase.exceptions import APIException
import requests

class APIRequest:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_request(cls, resource) -> Dict:
        res = requests.get(COINBASE_API_URL + resource, auth=auth)
        if res.status_code != requests.codes.OK:
            raise APIException("There was some kind of problem with the request")
        return res.json()
