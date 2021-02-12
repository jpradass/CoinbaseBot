from coinbase.user import User
from coinbase.accounts import Account
from coinbase.transactions import Transaction
from typing import Dict, List
from coinbase.auth import auth
from coinbase.constants import COINBASE_API_URL

class Coinbase:
    def __init__(self) -> None:
        self.auth = auth

    def get_user(self) -> User:
        """
        Returns current user
        """
        return User.me()

    def list_accounts(self) -> List[Account]:
        """
        Returns list of accounts
        """
        return Account.list()

    def list_transactions(self, account_id) -> List[Account]:
        """
        Returns list of transactions from some account
        """
        return Transaction.list(account_id)

