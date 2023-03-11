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
    # Attributes like symbol, priceChange, priceChangePercent are adding dynamically after method execution.
    # You can find all possible attributes in documentation
    data = MexcAPI.get_current_average_price()
    print(data.symbol, data.priceChange, data.priceChangePercent)
    
    
    # Private endpoints example
    # These methods require api and secret keys
    # You need to create instance of MexcAPI class
    mexc = MexcAPI(API_KEY, SECRET_KEY)
    result = mexc.get_account_information().json()
    print(result)


Public methods
--------------

    get_server_time()
    get_exchange_information()
    get_order_book()
    get_recent_trades()
    get_current_average_price()
    get_price_change_statistics()
    get_symbol_price_ticker()
    get_order_book_ticker()


Private methods
---------------

    get_account_information()
    create_new_order()
    cancel_order()
    cancel_orders_on_symbol()
    check_order_status()
    get_current_open_orders()
    get_all_orders()
    get_account_trade_list()

    get_currency_information()
    withdraw()
    get_deposit_history()
    get_withdraw_history()
    generate_deposit_address()
    get_deposit_address()
    universal_transfer()
