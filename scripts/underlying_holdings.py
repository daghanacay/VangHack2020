from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

etf_ticker = 'SPY'
holding_symbol = 'AAPL'
weight_greater = ''
weight_less = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_etf_holdings(etf_ticker=etf_ticker, holding_symbol=holding_symbol, weight_greater=weight_greater, weight_less=weight_less, page_size=page_size, next_page=next_page)
print(response)