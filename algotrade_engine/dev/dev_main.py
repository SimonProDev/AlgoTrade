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
df = pd.DataFrame(
    {'Adj Close': [1, 2, 3],
     'Open': [7, 8, 9]},
    index=[1, 2, 3]
)

my_ticker = output_yf_api.get('^GDAXI')
my_ticker.run_strategy(Swing())
# my_ticker.df = my_ticker.df.assign(new_col=lambda x: 'df_ticker')
# my_ticker.strategy.df = my_ticker.strategy.df.assign(new_col=lambda x: 'df_strategy')
display(my_ticker.df, name='my_ticker.df')
print()
