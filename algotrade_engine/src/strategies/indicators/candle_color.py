from algotrade_engine.src.strategies.indicators.indicator import Indicator
import pandas as pd


class CandleColor(Indicator):

    def __init__(self):
        self.name = 'candle_color'

    def calculate_indicator(self, df: pd.DataFrame) -> pd.DataFrame:
        res_df = df
        res_df[self.name] = (res_df['Adj Close'] > res_df['Open']).astype(int)
        return res_df
