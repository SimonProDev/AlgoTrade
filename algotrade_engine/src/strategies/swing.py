from algotrade_engine.src.strategies.strategy import Strategy
from algotrade_engine.src.strategies.indicators.is_green_candle import GreenCandle


class Swing(Strategy):

    def __init__(self):
        super().__init__()
        self.name = 'swing'

    def build_strategy(self, df):
        self.add_indicator(GreenCandle())
        return self.calculate_indicators(df)

    def add_buy_triggers(self) -> None:
        return

    def add_sell_triggers(self) -> None:
        return
