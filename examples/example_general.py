from sinegy_python.marketplace import Marketplace

sinegy = Marketplace(api_key = '', secret_key = '')

print('----- CURRENCIES -----')
print(sinegy.get_currencies())

print('----- CURRENCY PAIRS -----')
print(sinegy.get_currency_pairings())

print('----- SERVER STATUS -----')
print(sinegy.get_server_status())

print('----- SERVER TIME -----')
print(sinegy.get_server_time())
