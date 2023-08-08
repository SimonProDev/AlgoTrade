import pandas as pd

from algotrade_engine.conf import settings
from algotrade_engine.src.ticker.ticker import Ticker


class PrepareData:
    """
    Prepare data for each ticker based on
    raw output of yf_api
    """

    def __init__(self, raw_ticker_data: pd.DataFrame):
        self.raw_ticker_data = raw_ticker_data
        self.cleaned_ticker_data = []

    def clean_df(self, ticker):
        cleaned_df = self.raw_ticker_data.iloc[1:, self.raw_ticker_data.columns.get_level_values(1) == ticker] \
            .sort_index(ascending=False) \
            .dropna()
        # create column with ti with 0 the last candlestick available
        cleaned_df['t'] = [f't{i}' for i in range(len(cleaned_df.index))]
        return cleaned_df

    def prepare_ticker_data(self) -> None:
        """
        Clean raw ticker data from yahoo finance API by creating a list
        with ticker object
        :return: None
        """
        for ticker in settings.TICKERS:
            self.cleaned_ticker_data.append(Ticker(ticker,
                                                   'type_tbd',
                                                   self.clean_df(ticker)))

    def get_ticker_data(self) -> list:
        """
        Return ticker data from yahoo finance API
        after cleaning
        :return: Dic of ticker object
        """
        return self.cleaned_ticker_data
