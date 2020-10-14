import pandas as pd
import yfinance as yf

tickers = []
with open('/home/manveer/hackathon/VangHack2020/asx-data/asx_etf_list.csv') as f:
    asx_etfs = f.readlines()[1:]

    tickers = [asx_etf.split(',')[0] + '.AX' for asx_etf in asx_etfs]

    print(tickers)

import yfinance as yf
data: pd.DataFrame = yf.download(' '.join(tickers), start="2019-01-01", end="2020-10-14")

print(data)

data.to_csv('asx_price_history_1_year.csv')

# ticker = yf.Ticker("APT.ax")
#
# hist = ticker.history(period="max")
#
# print(hist['Close'])
#
# print(ticker.actions)