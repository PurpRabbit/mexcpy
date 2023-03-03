# Market data enpoints

test_conectivity = '/api/v3/ping'
check_server_time = '/api/v3/time'
exchange_information = '/api/v3/exchangeInfo'
order_book = '/api/v3/depth'
recent_trades = '/api/v3/trades'
current_avg_price = '/api/v3/avgPrice'
price_change_statistics = '/api/v3/ticker/24hr'
symbol_price_ticker = '/api/v3/ticker/price'
order_book_ticker = '/api/v3/ticker/bookTicker'


# Spot Account/Trade endpoints

new_order = '/api/v3/order'
cancel_order = '/api/v3/order'
cancel_all_symbol_orders = '/api/v3/openOrders'
query_order = '/api/v3/order'
current_open_orders = '/api/v3/openOrders'
all_orders = '/api/v3/allOrders'
trade_list = '/api/v3/myTrades'
account_information = '/api/v3/account'


# Wallet endpoint

query_currency_information = '/api/v3/capital/config/getall'
withdraw = '/api/v3/capital/withdraw/apply'
deposit_history = '/api/v3/capital/deposit/hisrec'
withdraw_history = '/api/v3/capital/withdraw/history'
generate_deposit_address = '/api/v3/capital/deposit/address'
deposit_address = '/api/v3/capital/deposit/address'
universal_transfer = '/api/v3/capital/transfer'