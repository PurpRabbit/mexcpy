import time
import hmac
import hashlib
from urllib.parse import urlencode


class Signature:
    def __init__(self, api_key: str, secret_key: str):
        self.__secret_key = secret_key
        self._headers = {
            "X-MEXC-APIKEY": api_key,
            "Content-Type": "application/json"
        }

    def _get_signed_params(self, params: dict=None) -> dict:
        if params and 'self' in params:
            params.pop('self')
        parameters = params.copy() if params is not None else dict()
        parameters['recvWindow'] = 60000
        parameters['timestamp'] = int(time.time()*1000)
        query_string = urlencode(parameters)
        parameters['signature'] = hmac.new(self.__secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        return urlencode(parameters)