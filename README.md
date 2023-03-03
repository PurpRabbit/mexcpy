# mexcpy
Unofficial Mexc exchange API wrapper. Official [documentation](https://mxcdevelop.github.io/apidocs/spot_v3_en/#introduction).

Features
--------

- Market, Spot, Wallet endpoints implementation
- Easy authentication using only api & secret keys

Start
-----

[Account registration](https://www.mexc.com/register?inviteCode=1EWNj)

[Create new API key](https://www.mexc.com/user/openapi)

Installation:

    git clone https://github.com/PurpRabbit/mexcpy


Example
-------

    from mexcpy import MexcAPI
    
    # Public endpoints example
    # All methods return an instance of ResponseAPI class, to get clear data, the json() method must be called
    data = MexcAPI.get_server_time().json()
    print(data)
    
    # Instead of usind the json() method you can refer to attributes of ResponseAPI class instance
    data = MexcAPI.get_current_average_price()
    print(data.symbol, data.priceChange, data.priceChangePercent)
    # Attributes like symbol, priceChange, priceChangePercent are adding dynamically after method execution.
    # You can find all possible attributes in [documentation](https://mxcdevelop.github.io/apidocs/spot_v3_en/#introduction)
    
    
    # Private endpoints example
    # These methods require api and secret keys
    # You need to create instance of MexcAPI class
    mexc = MexcAPI(API_KEY, SECRET_KEY)
    result = mexc.get_account_information().json()
    print(result)
