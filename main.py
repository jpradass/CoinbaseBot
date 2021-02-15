from coinbase.client import Coinbase
from coingecko.client import CoinGecko

# client = Coinbase()
geckoclient = CoinGecko()

print(geckoclient.coin_range('chainlink', 'eur', '1613326760', '1613334016'))
# print(client.getcurrent_price('LINK-EUR'))
# accounts = client.list_accounts()
#print([(account.account_id, account.account_code, account.account_amount) for account in accounts])
# print([(transaction.transaction_id, transaction.transaction_type ,transaction.transaction_crypto_currency, transaction.transaction_crypto_amount) for transaction in client.list_transactions(accounts[1].account_id)])
# print([(payment.payment_id, payment.payment_type, payment.payment_currency)for payment in client.listpayment_methods()])