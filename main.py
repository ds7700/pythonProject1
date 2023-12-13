import requests
import json
import pandas as pd
import datetime
print ("cto nyjno?")
symb = input()
print ("какой тф?(1m/3m/5m/15m/30m/1h/2h/4h/1d/1w)")
tf = input()
def candles(symb,tf):
    url = 'https://fapi.binance.com/fapi/v1/klines'
    param = {'symbol': symb, 'interval': tf}
    r = requests.get(url, params=param)
    if r.status_code == 200:
       df = pd.DataFrame(r.json())
       m = pd.DataFrame()
       m['date'] = df.iloc[:,0]
       m['date'] = pd.to_datetime(m['date'], unit = 'ms')
       m['open'] = df.iloc[:,1].astype(float)
       m['high'] = df.iloc[:, 2].astype(float)
       m['low'] = df.iloc[:, 3].astype(float)
       m['close'] = df.iloc[:, 4].astype(float)
       return m
    else:
        return print("error")

k = candles(symb, tf)
print(k)