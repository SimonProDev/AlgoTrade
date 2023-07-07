import pandas as pd
from algotrade_engine.src.strategies.strategy import Strategy
from algotrade_engine.src.strategies.indicators.is_green_candle import GreenRedCandle


class Swing(Strategy):

    def __init__(self, df: pd.DataFrame):
        super().__init__(df)
        self.name = 'swing'

    def build_strategy(self) -> None:
        self.add_indicator(GreenRedCandle())
        self.calculate_indicators()
        self.add_triggers()

    def add_buy_triggers(self) -> None:
        pass

    def add_sell_triggers(self) -> None:
        pass
