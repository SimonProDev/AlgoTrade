from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.strategies.swing import Swing
from algotrade_engine.src.alerting.alerting_manager import AlertingManager


class AlgoTradeManager:
    """
    Manager class that run AlgoTrade Application
    """

    def __init__(self):
        self.ticker_data = None
        self.yf_manager = None
        self.strategy = None
        self.alerting_manager = None

    def run_algotrade_app(self):
        self.download_ticker_data()
        self.run_strategy()
        # self.run_alerting()

    def download_ticker_data(self):
        self.yf_manager = YahooFinanceManager()
        self.yf_manager.call_yf_api()
        self.ticker_data = self.yf_manager.get_ticker_data()

    """
    rework of strategy class
    should be done on several Tickers instance
    adjust constructor input to Strategy
    """
    def run_strategy(self):
        self.strategy = Swing(self.ticker_data.get('^GDAXI').get_df().copy())
        self.strategy.build_strategy()

    def run_alerting(self):
        self.alerting_manager = AlertingManager()
        self.alerting_manager.create_alters()
        self.alerting_manager.send_alerts()
