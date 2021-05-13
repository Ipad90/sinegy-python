# sinegy-python
Python library for connecting to the [Sinegy API](https://docs.sinegy.com).

## How to install
````
pip install sinegy-python
````

## Generating API credentials
Go to [https://marketplace.sinegy.com/user/profile](https://marketplace.sinegy.com/user/profile) to generate API credentials.

## Official Sinegy API Documentation
Link to Sinegy's API documentation page is [https://docs.sinegy.com](https://docs.sinegy.com)

## Example
````
from sinegy_python.marketplace import Marketplace

sinegy = Marketplace(api_key = 'API_KEY', secret_key = 'SECRET_KEY')
sinegy_btc_ticker = sinegy.ticker('btcmyr')
print(sinegy_btc_ticker)
````
