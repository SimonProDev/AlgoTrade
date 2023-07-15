import algotrade_engine.conf.settings as settings
import importlib

from algotrade_engine.src.alerting.alerting_manager import AlertingManager
from algotrade_engine.src.algotrade_manager import AlgoTradeManager

from algotrade_engine.src.tools.display_df import display
import pandas as pd


# run config
importlib.import_module('algotrade_engine.conf.config')

pd.set_option('display.max_rows', None)

algotrade_manager = AlgoTradeManager()
algotrade_manager.run_algotrade_app()

# alerting_manager = AlertingManager()
# alerting_manager.create_alters()
# alerting_manager.send_alerts()

print()
