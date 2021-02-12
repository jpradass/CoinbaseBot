import requests
from coinbase.exceptions import APIException
from coinbase.constants import COINBASE_API_URL
from coinbase.auth import auth

class User:
    resource = 'user'

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')

    @classmethod
    def me(cls) -> "User":
        res = requests.get(COINBASE_API_URL + cls.resource, auth=auth)
        if res.status_code != requests.codes.OK:
            raise APIException("There was some kind of problem with the request")
        return cls(**res.json()['data'])

    