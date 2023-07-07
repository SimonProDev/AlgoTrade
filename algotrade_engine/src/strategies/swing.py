import pandas as pd
import numpy as np
from algotrade_engine.src.strategies.strategy import Strategy
from algotrade_engine.src.strategies.indicators.candle_color import CandleColor


class Swing(Strategy):

    def __init__(self, df: pd.DataFrame):
        super().__init__(df)
        self.name = 'swing'

    def add_indicators(self) -> None:
        self.add_indicator(CandleColor())

    def add_buy_triggers(self) -> None:
        """
        Sum last 4 candle_color
        tips: rolling backward is the same as rolling forward then shifting
        :return: None
        """
        self.df['sum_last_4_candle_color'] = self.df['candle_color'] \
            .transform(lambda x: x.rolling(4).sum().shift(-3))
        self.df['buy_sell_trigger'] = np.where(self.df['sum_last_4_candle_color'] == 4, 1,
                                               np.where(self.df['sum_last_4_candle_color'] == 0, -1, 0))

    def add_sell_triggers(self) -> None:
        pass
