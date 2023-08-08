# from datetime import datetime, time
# import pytz
#
#
# tz_paris = pytz.timezone('Europe/Paris')
#
# start = '16:19:00'
# end = '16:20:00'
# now = datetime.now(tz_paris).strftime("%H:%M:%S")
#
# print(f'start = {start} and now = {now}')
# print()
# print(now > start)
# print(now < end)

import yfinance as yf

df = yf.download(tickers=['^DJI'],
                 start='2023-08-06',
                 end=None,
                 interval='30m')
print(df)
