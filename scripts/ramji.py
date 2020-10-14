import pandas as pd

df = pd.read_csv('/home/manveer/hackathon/VangHack2020/asx-data/asx_price_history_3_years.csv')

df = df.set_index('Date')

export_list = []
df_dict = df.to_dict('index')
for date_val,etf_price in df_dict.items():
    for etf, price in etf_price.items():
        export_list.append([date_val, etf, price])


import csv

with open('ramji.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for r in export_list:
        wr.writerow(r)