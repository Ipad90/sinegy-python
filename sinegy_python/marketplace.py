from .base import Base
from typing import Dict

import urllib

class Marketplace(Base):
    def __init__(self, api_key, secret_key):
        Base.__init__(self, api_key, secret_key)
        self.version = '/api/v1'
        self.base = ' https://api.sinegy.com'

    def get_currencies(self) -> Dict[str, any]:
        return Base.send(self, 'GET', f'{self.version}/general/currency', None)

    def get_currency_pairings(self) -> Dict[str, any]:
        return Base.send(self, 'GET', f'{self.version}/general/currency-pair', None)

    def get_server_status(self) -> Dict[str, any]:
        return Base.send(self, 'GET', f'{self.version}/server/status', None)

    def get_server_time(self) -> Dict[str, any]:
        return Base.send(self, 'GET', f'{self.version}/server/time', None)

    def ticker(self, pair: str) -> Dict[str, any]:
        url = f'{self.version}/market/spot/chart/ticker/24hr'
        path = {
            'currencyPair': pair,
        }
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def orderbook(self, pair: str) -> Dict[str, any]:
        url = f'{self.version}/market/spot/orderbook'
        path = {
            'currencyPair': pair,
        }
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_recent_trades(self, pair: str, page: int, limit: int = 250) -> Dict[str, any]:
        url = f'{self.version}/market/spot/trades'
        path = {
            'currencyPair': pair,
            'page': page,
            'limit': limit
        }
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_chart_data(self, pair: str, reso: str, to_ts: int, limit: int = 2000) -> Dict[str, any]:
        url = f'{self.version}/market/spot/chart/klines'
        path = {
            'currencyPair': pair,
            'limit': limit,
            'reso': reso,
            'toTs': to_ts
        }
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_account_balance(self, currency: str = None, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/balance'
        path = {
            'recvWindow': recv_window
        }
        if currency is not None:
            path['currency'] = currency
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_transactions(self, currency: str, page: int = 1, limit: int = 250, start_time: int = 0, end_time: int = 0, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/transaction'
        path = {
            'currency': currency,
            'page': page,
            'limit': limit,
            'recvWindow': recv_window
        }
        if start_time > 0:
            path['startTime'] = start_time
        if end_time > 0:
            path['endTime'] = end_time
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_deposits(self, currency: str, page: int = 1, limit: int = 250, start_time: int = 0, end_time: int = 0, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/wallet/deposit/asset'
        path = {
            'currency': currency,
            'page': page,
            'limit': limit,
            'recvWindow': recv_window
        }
        if start_time > 0:
            path['startTime'] = start_time
        if end_time > 0:
            path['endTime'] = end_time
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_withdrawals(self, currency: str, page: int = 1, limit: int = 250, start_time: int = 0, end_time: int = 0, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/wallet/withdrawal/asset'
        path = {
            'currency': currency,
            'page': page,
            'limit': limit,
            'recvWindow': recv_window
        }
        if start_time > 0:
            path['startTime'] = start_time
        if end_time > 0:
            path['endTime'] = end_time
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_trade_fees(self, pair: str) -> Dict[str, any]:
        url = f'{self.version}/general/trade/fees'
        path = {
            'currencyPair': pair
        }
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_specific_order(self, pair: str, transaction_no: str, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/orders/check'
        path = {
            'currencyPair': pair,
            'transactionNo': transaction_no,
            'recvWindow': recv_window
        }
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_active_orders(self, pair: str, page: int = 1, limit: int = 250, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/orders'
        path = {
            'currencyPair': pair,
            'page': page,
            'limit': limit,
            'recvWindow': recv_window
        }
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)
    
    def get_filled_orders(self, pair: str, page: int = 1, limit: int = 250, start_time: int = 0, end_time: int = 0, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/orders/history'
        path = {
            'currencyPair': pair,
            'page': page,
            'limit': limit,
            'recvWindow': recv_window
        }
        if start_time > 0:
            path['startTime'] = start_time
        if end_time > 0:
            path['endTime'] = end_time
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def get_trades(self, pair: str, page: int = 1, limit: int = 250, start_time: int = 0, end_time: int = 0, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/trades'
        path = {
            'currencyPair': pair,
            'recvWindow': recv_window
        }
        if start_time > 0:
            path['startTime'] = start_time
        if end_time > 0:
            path['endTime'] = end_time
        path['signature'] = Base.signature(self, 'GET', url, path)
        url += '?' + urllib.parse.urlencode(path)
        return Base.send(self, 'GET', url, None)

    def place_test_order(self, pair: str, price: float, volume: float, side: str, order_type: str, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/orders/test'
        parameters = {
            'currencyPair': pair,
            'unitPrice': price,
            'volume': volume,
            'orderSide': side,
            'orderType': order_type,
            'recvWindow': recv_window
        }
        parameters['signature'] = Base.signature(self, 'POST', url, parameters)
        return Base.send(self, 'POST', url, parameters)

    def place_order(self, pair: str, price: float, volume: float, side: str, order_type: str, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/orders/place'
        parameters = {
            'currencyPair': pair,
            'unitPrice': price,
            'volume': volume,
            'orderSide': side,
            'orderType': order_type,
            'recvWindow': recv_window
        }
        parameters['signature'] = Base.signature(self, 'POST', url, parameters)
        return Base.send(self, 'POST', url, parameters)

    def cancel_order(self, pair: str, order_id: str, recv_window: int = 5000) -> Dict[str, any]:
        url = f'{self.version}/account/orders/cancel'
        parameters = {
            'currencyPair': pair,
            'orderId': order_id,
            'recvWindow': recv_window
        }
        parameters['signature'] = Base.signature(self, 'DELETE', url, parameters)
        return Base.send(self, 'DELETE', url, parameters)
