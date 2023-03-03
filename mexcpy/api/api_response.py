class APIResponse:
    def __init__(self, response: dict | list, request_name: str=None):
        self.__request_name = request_name
        self.__response = response

        if isinstance(response, dict):
            self._set_dict_attrs(response)
    
    def json(self) -> dict | list:
        return self.__response
    
    def _set_dict_attrs(self, response: dict) -> None:
        for key, value in response.items():
            if isinstance(value, dict):
                setattr(self, key, type(key, (APIResponse), value))
            else:
                setattr(self, key, value)

    def __repr__(self) -> str:
        return self.__name__ if self.__request_name is None else self.__request_name
    

    