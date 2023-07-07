from abc import ABC, abstractmethod
import pandas as pd
from algotrade_engine.src.strategies.indicators.indicator import Indicator


class Strategy(ABC):
    """
    Strategy to be applied on a ticker
    will enrich df with indicators, buy and sell triggers
    """

    def __init__(self, df: pd.DataFrame):
        self.name = ''
        self.df = df
        self.indicators = []

    def build_strategy(self) -> None:
        """
        Manager function that will trigger the creation of strategy on df
        :return: None
        """
        self.add_indicators()
        self.calculate_indicators()
        self.add_triggers()

    def calculate_indicators(self) -> None:
        for indicator in self.indicators:
            self.df = indicator.get_indicator(self.df)

    @abstractmethod
    def add_indicators(self) -> None:
        pass

    def add_indicator(self, indicator: Indicator) -> None:
        self.indicators.append(indicator)

    def add_triggers(self) -> None:
        self.add_buy_triggers()
        self.add_sell_triggers()

    @abstractmethod
    def add_buy_triggers(self) -> None:
        pass

    @abstractmethod
    def add_sell_triggers(self) -> None:
        pass
