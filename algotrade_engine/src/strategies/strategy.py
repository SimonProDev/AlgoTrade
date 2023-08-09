from abc import ABC, abstractmethod

from algotrade_engine.conf import settings
from algotrade_engine.src.ticker.ticker import Ticker
from algotrade_engine.src.strategies.indicators.indicator import Indicator


class Strategy(ABC):
    """
    Strategy to be applied on a ticker
    will enrich df with indicators, buy and sell triggers
    """

    def __init__(self, ticker: Ticker):
        self.name = ''
        self.ticker = ticker
        self.indicators = []
        self.trade_signal = 0

    def build_strategy(self) -> None:
        """
        Manager function that will trigger the creation of strategy on df
        :return: None
        """
        settings.logger.info(f'RUN STRATEGY {self.name} FOR {self.ticker.user_name}')
        self.add_indicators()
        settings.logger.info(f'RUN STRATEGY ADD INDICATORS {[indicator.name for indicator in self.indicators]}')
        self.calculate_indicators()
        settings.logger.info('RUN STRATEGY CALCULATE INDICATORS')
        self.add_triggers()
        settings.logger.info('RUN STRATEGY ADD TRIGGERS')
        self.add_trade_signal()
        settings.logger.info('RUN STRATEGY ADD TRADE SIGNAL')

    def calculate_indicators(self) -> None:
        for indicator in self.indicators:
            self.ticker.set_df(indicator.get_indicator(self.ticker.get_df()))

    @abstractmethod
    def add_indicators(self) -> None:
        pass

    def add_indicator(self, indicator: Indicator) -> None:
        self.indicators.append(indicator)

    def add_triggers(self) -> None:
        self.add_entry_triggers()
        self.add_exit_triggers()

    @abstractmethod
    def add_entry_triggers(self) -> None:
        pass

    @abstractmethod
    def add_exit_triggers(self) -> None:
        pass

    def add_trade_signal(self):
        # if pandas df has at least 1 row and has a trade signal
        # update trade_signal
        if self.ticker.get_df().shape[0] > 0:
            if self.ticker.get_df()['trade_trigger'].iloc[0] != 0:
                self.trade_signal = self.ticker.get_df()['trade_trigger'].iloc[0]
                self.trade_signal = 1

