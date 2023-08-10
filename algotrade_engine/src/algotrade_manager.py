import copy
import importlib
import pickle
import os
import glob
from subprocess import call

from algotrade_engine.conf import settings
from algotrade_engine.src.ticker.init_tickers import initialize_tickers
from algotrade_engine.src.utils.message_utils import create_logger_message
from algotrade_engine.src.yf_api.prepare_data import PrepareData

from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.strategies.swing import Swing
from algotrade_engine.src.alerting.charts_creator import ChartCreator
from algotrade_engine.src.alerting.alerting_manager import AlertingManager


class AlgoTradeManager:
    """
    Manager class that run AlgoTrade Application
    """

    def __init__(self):
        self.ticker_data = None
        self.strategy = []

    def run_algotrade_app(self) -> None:
        settings.logger.info(create_logger_message('INITIALIZE TICKERS'))
        initialize_tickers()
        settings.logger.info(create_logger_message('DOWNLOAD TICKER DATA'))
        self.download_ticker_data()
        settings.logger.info(create_logger_message('PREPARE TICKER DATA'))
        self.prepare_ticker_data()
        settings.logger.info(create_logger_message('RUN STRATEGIES'))
        self.run_strategy()
        settings.logger.info(create_logger_message('CREATES CHARTS'))
        self.create_charts()
        settings.logger.info(create_logger_message('RUN ALERTING'))
        self.run_alerting()

    def download_ticker_data(self) -> None:
        yf_manager = YahooFinanceManager()
        yf_manager.call_yf_api()
        self.ticker_data = yf_manager.get_ticker_data()
        # with open('tmp_files/output_yf_api', 'wb') as f:
        #     pickle.dump(self.yf_manager.get_ticker_data(),
        #                 f)
        # with open('tmp_files/output_yf_api', 'rb') as pickle_file:
        #     self.ticker_data = pickle.load(pickle_file)
        settings.logger.info('TICKER DATA DOWNLOADED')

    def prepare_ticker_data(self):
        prepare_data = PrepareData(self.ticker_data)
        prepare_data.prepare_ticker_data()

    def run_strategy(self) -> None:
        # apply strategy for each ticker
        # add it to the strategy attribute if there is a trade signal
        for ticker in settings.TICKERS:
            strategy = Swing(ticker)
            strategy.build_strategy()
            if strategy.trade_signal != 0:
                settings.logger.info(f'TRADE SIGNAL IDENTIFIED FOR {ticker.yf_api_name}')
                self.strategy.append(strategy)
            # save ticker df to csv
            ticker.df.to_csv(f'/tmp/df_{ticker.yf_api_name}.csv')

    def create_charts(self) -> None:
        # delete old charts in tmp_files before creating new ones
        # old_charts = glob.glob('/tmp/*.jpg')
        # for chart in old_charts:
        #     os.remove(chart)
        # call('rm -rf /tmp/*', shell=True)

        # create chart for ticker that have a trade_signal in strategy
        for strategy in self.strategy:
            chart_creator = ChartCreator(strategy.ticker)
            chart_creator.create_chart()

    def run_alerting(self) -> None:
        alerting_manager = AlertingManager([strategy.ticker.yf_api_name for strategy in self.strategy])
        alerting_manager.create_alters()
        alerting_manager.send_alerts()
