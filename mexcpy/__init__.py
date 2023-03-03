from .api.market_data import MarketData
from .api.spot_account import SpotAccount
from .api.wallet_data import Wallet


class MexcAPI(MarketData, SpotAccount, Wallet):
    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)