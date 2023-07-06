from abc import ABC, abstractmethod
import pandas as pd
from algotrade_engine.src.strategies.indicators.indicator import Indicator


class Strategy(ABC):
    """
    Strategy to be applied on a ticker
    will enrich df with indicators, buy and sell triggers
    """

    def __init__(self):
        self.indicators = []
        self.name = ''

    @abstractmethod
    def build_strategy(self, df: pd.DataFrame) -> None:
        pass

    def add_indicator(self, indicator: Indicator) -> None:
        self.indicators.append(indicator)

    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        res_df = None
        for indicator in self.indicators:
            res_df = indicator.get_indicator(df)
        return res_df

    # def get_strategy_df(self) -> pd.DataFrame:
    #     return self.df

    @abstractmethod
    def add_buy_triggers(self) -> None:
        pass

    @abstractmethod
    def add_sell_triggers(self) -> None:
        pass
