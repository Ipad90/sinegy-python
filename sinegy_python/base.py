from typing import Dict

import base64
import hmac
import requests
import time
import urllib

class Base:       
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def signature(self, method, url, parameters) -> bytes:
        parameters['timestamp'] = self.timestamp()
        parameters = urllib.parse.urlencode(parameters)
        signature = f'{method}|{url}|{parameters}'.encode()
        signature = hmac.new(self.secret_key.encode(), signature, 'sha256').digest()
        return base64.b64encode(signature)

    def timestamp(self) -> int:
        return int(time.time() * 1000)

    def send(self, method, url, data) -> Dict[str, any]:
        url = f'{self.base}{url}'
        headers = {
            'api-key': self.api_key
        }
        req = requests.request(method, url = url, headers = headers, data = data)
        return req.json()
