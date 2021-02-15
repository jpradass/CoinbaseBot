from coinbase.price import Price
from coinbase.payments import Payment
from coinbase.user import User
from coinbase.accounts import Account
from coinbase.transactions import Transaction
from typing import List
from coinbase.auth import auth

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

    def list_transactions(self, account_id: str) -> List[Account]:
        """
        Returns list of transactions from some account
        """
        return Transaction.list(account_id)

    def listpayment_methods(self) -> List[Payment]:
        """
        Lists current user’s payment methods.
        """
        return Payment.list()

    def getcurrent_price(self, pair_coin) -> Price:
        """
        Get current price for token
        """
        return Price.get_price(pair_coin=pair_coin)

    def make_transfer(self, from_account: str, to_account: str, transfer_type: str, amount: str, currency: str) -> Transaction:
        """
        Transfer money between accounts
        
        @params 
        from_account: string representing account uuid where token will be sended
        to_account: string representing account uuid where token will be addressed
        transfer_type: string representing transfer type. It could be:
            trade
            sell
            buy
            send
            request
            transfer
        amount: string representing amount to be deposited
        currency: string representing currency for the amount

        @ return Transaction entity with the transaction made
        """
        return Transaction.make_transfer(self, from_account, to_account, transfer_type, amount, currency)
