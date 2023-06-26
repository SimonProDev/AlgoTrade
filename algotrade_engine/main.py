import importlib
import time
import algotrade_engine.conf.settings as settings
from algotrade_engine.src.algotrade_manager import AlgoTradeManager


def algo_trade_engine(app_param):
    start = time.perf_counter()

    # assign app_param in settings
    settings.APPLICATION_PARAMETERS = app_param

    # run config
    importlib.import_module('algotrade_engine.conf.config')

    # run application
    print(settings.START_MESSAGE)
    algotrade_manager = AlgoTradeManager()
    algotrade_manager.run_algotrade_app()

    # log end metrics
    stop = time.perf_counter()
    settings.logger.info(f'Execution takes {(stop-start)/60:.2f} minutes')


if __name__ == "__main__":
    algo_trade_engine(app_param=['',
                                 '1.0'])
