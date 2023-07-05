import algotrade_engine.conf.settings as settings
import importlib

from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.tools.display_df import display
import pandas as pd

# run config
importlib.import_module('algotrade_engine.conf.config')

yf_manager = YahooFinanceManager()
yf_manager.call_yf_api()
output_yf_api = yf_manager.get_ticker_data()

pd.set_option('display.max_rows', None)
# display(df_res)
# display(df_res.iloc[:, df_res.columns.get_level_values(1) == '^GDAXI'])
# display(output_yf_api.get('^GDAXI').df)
# print(output_yf_api.get('EURUSD=X'))
print(output_yf_api.get('^GDAXI').df)
print()
