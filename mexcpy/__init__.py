from .api import MarketData
from .api import SpotAccount
from .api import Wallet


class MexcAPI(MarketData, SpotAccount, Wallet):
    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)