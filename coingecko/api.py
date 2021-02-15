import requests
from typing import Dict
from coingecko.constants import COINGECKO_API_URL
from coingecko.exceptions import APIException

class APIRequest:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_request(self, resource) -> Dict:
        res = requests.get(COINGECKO_API_URL + resource)
        if res.status_code != requests.codes.OK:
            raise APIException("There was some kind of problem with the request")
        return res.json()