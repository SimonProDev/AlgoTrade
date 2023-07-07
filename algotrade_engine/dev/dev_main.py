import algotrade_engine.conf.settings as settings
import importlib

from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.tools.display_df import display
import pandas as pd
from algotrade_engine.src.strategies.swing import Swing

# run config
importlib.import_module('algotrade_engine.conf.config')

yf_manager = YahooFinanceManager()
yf_manager.call_yf_api()
output_yf_api = yf_manager.get_ticker_data()


pd.set_option('display.max_rows', None)

my_ticker = output_yf_api.get('^GDAXI')

my_strategy = Swing(my_ticker.get_df().copy())
my_strategy.build_strategy()
# my_ticker.df = my_ticker.df.assign(new_col=lambda x: 'df_ticker')
# my_ticker.strategy.df = my_ticker.strategy.df.assign(new_col=lambda x: 'df_strategy')
display(my_ticker.get_df(), name='my_ticker.df')
display(my_strategy.df, name='my_strategy.df')
print()
