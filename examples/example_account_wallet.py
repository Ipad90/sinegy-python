from sinegy_python.marketplace import Marketplace

sinegy = Marketplace(api_key = '', secret_key = '')

print('----- ACCOUNT BALANCE -----')
print(sinegy.get_account_balance())

print('----- ACCOUNT TRANSACTIONS -----')
print(sinegy.get_transactions('MYR'))

print('----- DEPOSITS -----')
print(sinegy.get_deposits('MYR'))

print('----- WITHDRAWALS -----')
print(sinegy.get_withdrawals('MYR'))
