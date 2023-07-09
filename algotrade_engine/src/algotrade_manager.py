import copy
from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.strategies.swing import Swing
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
        self.download_ticker_data()
        self.run_strategy()
        # self.run_alerting()

    def download_ticker_data(self) -> None:
        self.yf_manager = YahooFinanceManager()
        self.yf_manager.call_yf_api()
        self.ticker_data = self.yf_manager.get_ticker_data()

    def run_strategy(self) -> None:
        for ticker in self.ticker_data:
            strategy = Swing(copy.deepcopy(ticker))
            strategy.build_strategy()
            self.strategy.append(strategy)

    def run_alerting(self) -> None:
        self.alerting_manager = AlertingManager()
        self.alerting_manager.create_alters()
        self.alerting_manager.send_alerts()
