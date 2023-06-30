import algotrade_engine.conf.settings as settings
import importlib

from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.tools.display_df import display

# run config
importlib.import_module('algotrade_engine.conf.config')

yf_manager = YahooFinanceManager()
yf_manager.call_yf_api()
df_res = yf_manager.get_ticker_data()

display(df_res)
# display(df_res.iloc[:, df_res.columns.get_level_values(1) == '^GDAXI'])
print()
