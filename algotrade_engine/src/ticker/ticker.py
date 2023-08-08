import pandas as pd


class Ticker:
    """
    Ticker to be called in yahoo finance API
    A strategy will be applied to each ticker enriching the dataframe
    """

    def __init__(self, yf_api_name, user_name, ticker_type, start_active_period, end_active_period, df):
        self.yf_api_name = yf_api_name
        self.user_name = user_name
        self.ticker_type = ticker_type
        self.start_active_period = start_active_period
        self.end_active_period = end_active_period
        self.df = df

    def get_df(self) -> pd.DataFrame:
        return self.df

    def set_df(self, df: pd.DataFrame) -> None:
        self.df = df
