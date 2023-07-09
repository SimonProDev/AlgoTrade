import algotrade_engine.conf.settings as settings
import importlib

from algotrade_engine.src.algotrade_manager import AlgoTradeManager

from algotrade_engine.src.tools.display_df import display
import pandas as pd


# run config
importlib.import_module('algotrade_engine.conf.config')

pd.set_option('display.max_rows', None)

algotrade_manager = AlgoTradeManager()
algotrade_manager.run_algotrade_app()
for strategy in algotrade_manager.strategy:
    display(strategy.ticker.df)
print()
