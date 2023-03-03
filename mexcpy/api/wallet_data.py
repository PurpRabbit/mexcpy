import requests
from typing import Literal

from .base_api import BaseApi
from .signature import Signature
from .api_response import APIResponse
from .endpoints import *


AccountType = ['SPOT', 'FUTURES', 'ISOLATED_MARGIN']


class Wallet(BaseApi, Signature):
    def __init__(self, api_key: str, secret_key: str) -> None:
        super().__init__(api_key, secret_key)

    def get_currency_information(self) -> APIResponse:
        """
        Query currency details and the smart contract address

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#query-the-currency-information
        """
        signed_params = self._get_signed_params()
        response = requests.get(self.BASE_URL + query_currency_information, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Currency information')
    
    def withdraw(self, coin: str, address:str, amount: str, withdrawOrderId: str=None, 
                                network: str=None, memo: str=None, remark: str=None) -> APIResponse:
        """
        Withdraw coin

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#withdraw
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + withdraw, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Withdraw')
    
    def get_deposit_history(self, coin: str=None, status: str=None, startTime: str=None, endTime: str=None, limit: str=None) -> APIResponse:
        """
        Get deposit history
        Ensure that the default timestamp of 'startTime' and 'endTime' does not exceed 90 days.

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#deposit-history-supporting-network
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + deposit_history, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Deposit history')
    
    def get_withdraw_history(self, coin: str=None, status: str=None, startTime: str=None, endTime: str=None, limit: str=None) -> APIResponse:
        """
        Get withdraw history
        Supported multiple network coins' withdraw history may not return the 'network' field.
        Ensure that the default timestamp of 'startTime' and 'endTime' does not exceed 90 days.

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#withdraw-history-supporting-network
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + withdraw_history, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Withdraw history')
    
    def generate_deposit_address(self, coin: str, network: str) -> APIResponse:
        """
        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#generate-deposit-address-supporting-network
        """
        signed_params = self._get_signed_params(locals())
        response = requests.post(self.BASE_URL + generate_deposit_address, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Deposit address generation')
    
    def get_deposit_address(self, coin: str, network: str=None) -> APIResponse:
        """
        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#deposit-address-supporting-network
        """
        signed_params = self._get_signed_params(locals())
        response = requests.get(self.BASE_URL + deposit_address, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Deposit address')
    
    def universal_transfer(self, fromAccountType: AccountType, toAccountType: AccountType, asset: str, amount: str, symbol: str=None) -> APIResponse:
        """
        :symbol: symbol,needed when fromAccountType is ISOLATED_MARGIN.eg:ETHUSDT

        Link: https://mxcdevelop.github.io/apidocs/spot_v3_en/#user-universal-transfer
        """
        signed_params = self._get_signed_params(locals())
        response = requests.post(self.BASE_URL + universal_transfer, headers=self._headers, params=signed_params)
        return APIResponse(response.json(), 'Universal transfer')
    
