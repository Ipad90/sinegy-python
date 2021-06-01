from sinegy_python.marketplace import Marketplace

sinegy = Marketplace(api_key = '', secret_key = '')

print('----- TRADE FEES -----')
print(sinegy.get_trade_fees('ethmyr'))

print('----- ORDER STATUS -----')
print(sinegy.get_order_status('ethmyr'))

print('----- ORDER TYPES -----')
print(sinegy.get_order_types('ethmyr'))

print('----- ORDER TIME INFORCE -----')
print(sinegy.get_order_time_inforce('ethmyr'))

print('----- ORDER SIDES -----')
print(sinegy.get_order_sides('ethmyr'))

print('----- ORDER FLAGS -----')
print(sinegy.get_order_flags('ethmyr'))

print('----- ACTIVE ORDERS -----')
print(sinegy.get_active_orders('ethmyr', 1, 10))

print('----- FILLED ORDERS -----')
print(sinegy.get_filled_orders('ethmyr', 1, 10))

print('----- GET TRADES -----')
print(sinegy.get_trades('ethmyr'))

print('----- PLACE TEST ORDER -----')
print(sinegy.place_test_order('ethmyr', 20000, 0.01, 'buy', 'limit'))

print('----- CANCEL ORDER -----')
print(sinegy.cancel_order('ethmyr', '420'))
