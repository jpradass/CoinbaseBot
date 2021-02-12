from coinbase.client import Coinbase

client = Coinbase()

accounts = client.list_accounts()
client.list_transactions(accounts[0].account_id)
print()