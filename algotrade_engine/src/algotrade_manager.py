import copy
import pickle
import os
import glob

from algotrade_engine.conf import settings
from algotrade_engine.src.utils.message_utils import create_logger_message

from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.strategies.swing import Swing
from algotrade_engine.src.alerting.charts_creator import ChartCreator
from algotrade_engine.src.alerting.alerting_manager import AlertingManager


class AlgoTradeManager:
    """
    Manager class that run AlgoTrade Application
    """

    def __init__(self):
        self.ticker_data = []
        self.yf_manager = None
        self.strategy = []
        self.alerting_manager = None

    def run_algotrade_app(self) -> None:
        settings.logger.info(create_logger_message('DOWNLOAD TICKER DATA'))
        self.download_ticker_data()
        settings.logger.info(create_logger_message('RUN STRATEGIES'))
        self.run_strategy()
        settings.logger.info(create_logger_message('CREATES CHARTS'))
        self.create_charts()
        settings.logger.info(create_logger_message('RUN ALERTING'))
        self.run_alerting()

    def download_ticker_data(self) -> None:
        self.yf_manager = YahooFinanceManager()
        self.yf_manager.call_yf_api()
        self.ticker_data = self.yf_manager.get_ticker_data()
        with open('algotrade_engine/dev/output_yf_api', 'wb') as f:
            pickle.dump(self.yf_manager.get_ticker_data(),
                        f)
        with open('algotrade_engine/dev/output_yf_api', 'rb') as pickle_file:
            self.ticker_data = pickle.load(pickle_file)
        settings.logger.info('TICKER DATA DOWNLOADED')

    def run_strategy(self) -> None:
        # apply strategy for each ticker
        # add it to the strategy attribute if there is a trade signal
        for ticker in self.ticker_data:
            strategy = Swing(copy.deepcopy(ticker))
            strategy.build_strategy()
            if strategy.trade_signal != 0:
                self.strategy.append(strategy)

    def create_charts(self) -> None:
        # delete old charts in tmp_files before creating new ones
        tmp_files_path = glob.glob('algotrade_engine/tmp_files/*.jpg')
        for chart in tmp_files_path:
            os.remove(chart)

        # create chart for ticker that have a trade_signal in strategy
        for strategy in self.strategy:
            chart_creator = ChartCreator(strategy.ticker)
            chart_creator.create_chart()

    def run_alerting(self) -> None:
        self.alerting_manager = AlertingManager([strategy.ticker.name for strategy in self.strategy])
        self.alerting_manager.create_alters()
        self.alerting_manager.send_alerts()
