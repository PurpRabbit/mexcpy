import requests
from typing import Literal

from .base_api import BaseApi
from .signature import Signature
from .api_response import APIResponse
from .endpoints import *


OrderSide = Literal['BUY', 'SELL']
OrderType = Literal['LIMIT', 'MARKET', 'LIMIT_MAKER', 'IMMEDIATE_OR_CANCEL', 'FILL_OR_KILL']


class SpotAccount(BaseApi, Signature):
    def __init__(self, api_key: str, secret_key: str) -> None:
        super().__init__(api_key, secret_key)

    def get_account_information(self) -> APIResponse:
        """
        Get current account information
        
        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#account-information
        """
        signed_params = self._get_signed_params()
        response = requests.get(self.BASE_URL + account_information, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Account information')
    
    def create_new_order(self, symbol: str, side: OrderSide, type: OrderType, quantity: int=None,
                                quoteOrderQty: int=None, price: int=None, newClientOrderId: str=None) -> APIResponse:
        """
        Create new spot order

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#new-order
        """

        signed_params = self._get_signed_params(locals())
        response = requests.post(self.BASE_URL + new_order, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'New order')
    
    def cancel_order(self, symbol: str, orderId: str=None, origClientOrderId: str=None, newClientOrderId: str=None) -> APIResponse:
        """
        Cancel an active order
        Either :orderId: or :origClientOrderId: must be sent.

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#cancel-order
        """
        signed_params = self._get_signed_params(locals())
        response = requests.delete(self.BASE_URL + cancel_order, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Cancel order')
    
    def cancel_orders_on_symbol(self, symbol: str) -> APIResponse:
        """
        Cancel all pending orders for a single symbol, including OCO pending orders.

        :symbol: maximum input 5 symbols, separated by ','. e.g. "BTCUSDT,MXUSDT,ADAUSDT"

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#cancel-all-open-orders-on-a-symbol
        """
        signed_params = self._get_signed_params(locals())
        response = requests.delete(self.BASE_URL + cancel_all_symbol_orders, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Cancel open orders')
    
    def check_order_status(self, symbol: str, origClientOrderId: str=None, orderId: str=None) -> APIResponse:
        """
        Check an order's status

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#query-order
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + query_order, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Order status')
    
    def get_current_open_orders(self, symbol: str) -> APIResponse:
        """
        Get all open orders on a symbol.

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#current-open-orders
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + current_open_orders, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Current open orders')
    
    def get_all_orders(self, symbol: str, startTime: int=None, endTime: int=None, limit: int=None) -> APIResponse:
        """
        Get all account orders including active, 
        cancelled or completed orders(the query period is the latest 24 hours by default).
        You can query a maximum of the latest 7 days.

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#all-orders
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + all_orders, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'All orders')
    
    def get_account_trade_list(self, symbol: str, orderId: str=None, startTime: int=None, endTime: int=None, limit: int=None) -> APIResponse:
        """
        Get trades for a specific account and symbol,Only the transaction records in the past 1 month can be queried.
        If you want to view more transaction records, please use the export function on the web side, 
        which supports exporting transaction records of the past 3 years at most

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#account-trade-list
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + trade_list, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Account trade list')
    