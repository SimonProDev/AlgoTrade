import numpy as np
from algotrade_engine.src.strategies.strategy import Strategy
from algotrade_engine.src.strategies.indicators.candle_color import CandleColor
from algotrade_engine.src.ticker.ticker import Ticker
from algotrade_engine.src.utils.display_df import display


class Swing(Strategy):

    def __init__(self, ticker: Ticker):
        super().__init__(ticker)
        self.name = 'swing'

    def add_indicators(self) -> None:
        self.add_indicator(CandleColor())

    def add_entry_triggers(self) -> None:
        """
        Sum last 4 candle_color
        tips: rolling backward is the same as rolling forward then shifting
        :return: None
        """
        df = self.ticker.get_df()
        # refactor into indicator 'sum_last_4_candle_color' and add to indicators
        df['sum_last_4_candle_color'] = df['candle_color'] \
            .transform(lambda x: x.rolling(4).sum().shift(-3))
        df['trade_trigger'] = np.where(df['sum_last_4_candle_color'] == 0, 1,
                                       np.where(df['sum_last_4_candle_color'] == 0, -1, 0))
        self.ticker.set_df(df)

    def add_exit_triggers(self) -> None:
        # sell triggers are created at the same time as buy triggers
        pass
