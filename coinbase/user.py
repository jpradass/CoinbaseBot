from coinbase.api import APIRequest

class User:
    resource = 'user'

    def __init__(self, *args: object, **kwargs: object) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')

    @classmethod
    def me(cls) -> "User":
        res = APIRequest.get_request(cls.resource)
        return cls(**res['data'])

    