
class APIException(Exception):
    """Raised when there's some kind of problem with the API"""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

class UserInputException(Exception):
    """Raised when the user input isn't correct"""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)