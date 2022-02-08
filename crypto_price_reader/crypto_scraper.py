import requests

api_key = "pk_4378f1e764fe4ac6b310101cd54197d2"


class CryptoCurrency:
    base_url = "https://cloud.iexapis.com/stable/crypto/"

    def __init__(self, symbol):
        self.symbol = symbol

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={api_key}"

    @property
    def price(self):
        req = requests.get(self.complete_url).json()
        return float(req.get('price'))
