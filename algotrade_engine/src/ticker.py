import pandas as pd


class Ticker:
    """
    Ticker to be called in yahoo finance API
    A strategy will be applied to each ticker enriching the dataframe
    """

    def __init__(self, name, ticker_type, df):
        self.name = name
        self.ticker_type = ticker_type
        self.df = df

    def get_df(self) -> pd.DataFrame:
        return self.df

    def set_df(self, df: pd.DataFrame) -> None:
        self.df = df
