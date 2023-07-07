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

    @abstractmethod
    def build_strategy(self) -> None:
        pass

    def add_indicator(self, indicator: Indicator) -> None:
        self.indicators.append(indicator)

    def calculate_indicators(self) -> None:
        for indicator in self.indicators:
            self.df = indicator.get_indicator(self.df)

    def add_triggers(self) -> None:
        self.add_buy_triggers()
        self.add_sell_triggers()

    @abstractmethod
    def add_buy_triggers(self) -> None:
        pass

    @abstractmethod
    def add_sell_triggers(self) -> None:
        pass
