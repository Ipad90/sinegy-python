from sinegy_python.marketplace import Marketplace

sinegy = Marketplace(api_key = '', secret_key = '')

print('----- TICKER -----')
print(sinegy.ticker('ethmyr'))

print('----- ORDERBOOK -----')
print(sinegy.orderbook('ethmyr'))

print('----- RECENT TRADES -----')
print(sinegy.get_recent_trades('ethmyr', 1, 10))

print('----- CHART DATA -----')
print(sinegy.get_chart_data('ethmyr', 'histohour', 1607609830, 10))
