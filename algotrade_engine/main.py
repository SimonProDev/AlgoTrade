import importlib
import time
import schedule
import algotrade_engine.conf.settings as settings
from algotrade_engine.src.algotrade_manager import AlgoTradeManager
from algotrade_engine.src.utils.message_utils import create_app_logo


def algo_trade_engine(app_param):
    start = time.perf_counter()
    print(create_app_logo())

    # assign app_param in settings
    settings.APPLICATION_PARAMETERS = app_param

    # run config
    importlib.import_module('algotrade_engine.conf.config')

    # run application
    algotrade_manager = AlgoTradeManager()
    algotrade_manager.run_algotrade_app()

    # log end metrics
    stop = time.perf_counter()
    settings.logger.info(f'Execution takes {(stop-start)/60:.2f} minutes')


if __name__ == "__main__":
    algo_trade_engine(app_param=['', '1.0'])
    # schedule.every(1).minutes.do(algo_trade_engine, ['', '1.0'])
    # while True:
    #     # Checks whether a scheduled task is pending to run or not
    #     schedule.run_pending()
    #     time.sleep(1)

