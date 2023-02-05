import pandas as pd
from IPython.display import display
import yfinance as yf


df = yf.download('MSCI',
                 start='2022-01-01',
                 end='2023-01-01',
                 actions=True).drop(columns=['Open', 'High', 'Low', 'Volume', 'Stock Splits'])

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
display(df)
