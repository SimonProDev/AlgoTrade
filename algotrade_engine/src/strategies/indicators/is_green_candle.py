from algotrade_engine.src.strategies.indicators.indicator import Indicator
import pandas as pd


class GreenCandle(Indicator):

    def __init__(self):
        self.name = 'GreenCandle'

    def calculate_indicator(self, df: pd.DataFrame) -> pd.DataFrame:
        res_df = df
        res_df['GreenCandle'] = res_df['Adj Close'] > res_df['Open']
        res_df['GreenCandle'].astype(int)
        return res_df