import requests

from mexcpy.api.base_api import BaseApi
from mexcpy.api.api_response import APIResponse
from mexcpy.api.endpoints import *


class MarketData(BaseApi):
    @classmethod
    def get_server_time(cls) -> APIResponse:
        response = requests.get(cls._BASE_URL + check_server_time)
        return APIResponse(response.json(), 'Server time')

    @classmethod
    def get_exchange_information(cls, symbol: str | list[str]=None) -> APIResponse:
        """
        Return exchange information

        :symbol: Specify symbol or symbols to get information
        """
        params = {}
        if isinstance(symbol, list):
            params['symbols'] = ','.join(symbol)
        elif isinstance(symbol, str):
            params['symbol'] = symbol
        
        response = requests.get(cls._BASE_URL + exchange_information, params=params)
        return APIResponse(response.json(), 'Exchange information')

    @classmethod
    def get_order_book(cls, symbol: str, limit: int=None) -> APIResponse:
        """
        Return ask and bids for needed symbol

        Request parameters:
            :symbol: Symbol
            :limit: Returen number, default 100; max 5000. Not required
        
        Response:
            :lastUpdateId: int
            :bids: list[Bid[Price, Quantity]]
            :asks: list[Ask[Price, Quantity]]
        """
        params = {'symbol': symbol, 'limit': limit}
        response = requests.get(cls._BASE_URL + order_book, params=params)
        return APIResponse(response.json(), 'Order book')
    
    @classmethod
    def get_recent_trades(cls, symbol: str, limit: int=None) -> APIResponse:
        """
        Return recent trades for needed symbol

        Request parameters:
            :symbol: Symbol
            :limit: Returen number, default 100; max 5000. Not required
        
        Response:
            :id:
            :price:
            :qty:
            :quoteQty:
            :time:
            :isBuyerMaker:
            :isBestMatch:
        """
        params = {'symbol': symbol, 'limit': limit}
        response = requests.get(cls._BASE_URL + recent_trades, params=params)        
        return APIResponse(response.json(), 'Recent trades')

    @classmethod
    def get_current_average_price(cls, symbol: str) -> APIResponse:
        """
        Return current price of symbol

        Request parameters:
            :symbol: Symbol

        Response:
            :mins: Average price time frame
            :price:
        """
        params = {'symbol': symbol}
        response = requests.get(cls._BASE_URL + current_avg_price, params=params)        
        return APIResponse(response.json(), 'Average price')
    
    @classmethod
    def get_price_change_statistics(cls, symbol: str=None) -> APIResponse:
        """
        Return price change data of symbol, if symbol is not specified, data for all symbols
        will be returned

        Request parameters:
            :symbol: Not required
        
        Response:
            :symbol:
            :priceChange:
            :priceChangePercent:
            :prevClosePrice:
            :lastPrice:
            :lastQty:
            :bidPrice:
            :bidQty:
            :askPrice:
            :askQty:
            :openPrice:
            :highPrice:
            :lowPrice:
            :volume:
            :quoteVolume:
            :openTime:
            :closeTime:
            :count:
        """
        params = {'symbol': symbol}
        response = requests.get(cls._BASE_URL + price_change_statistics, params=params)        
        return APIResponse(response.json(), 'Price change statistic')

    @classmethod
    def get_symbol_price_ticker(cls, symbol: str=None) -> APIResponse:
        """
        Return symbol price ticker

        Request parameters:
            :symbol: Not required
        
        Response:
            :symbol:
            :price: Last price
        """
        params = {'symbol': symbol}
        response = requests.get(cls._BASE_URL + symbol_price_ticker, params=params)   
        return APIResponse(response.json(), 'Symbol price ticker')

    @classmethod
    def get_order_book_ticker(cls, symbol: str=None) -> APIResponse:
        """
        Return symbol price ticker

        Request parameters:
            :symbol: Not required
        
        Response:
            :symbol:
            :bidPrice: Best bid price
            :bidQty: Best bid quantity
            :askPrice: Best ask price
            :askQty: Best ask quantity
        """
        params = {'symbol': symbol}
        response = requests.get(cls._BASE_URL + order_book_ticker, params=params)   
        return APIResponse(response.json(), 'Symbol price ticker')