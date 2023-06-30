import pandas as pd
import yfinance as yf


class YahooFinanceManager:
    """
    interface with yahoo finance API
    """

    def __init__(self):
        self.ticker_data = None
        self.ticker_settings = {
            'ticker_list': None,
            'start_date': None,
            'end_date': None,
            'interval': None
        }

    def set_ticker_settings(self,
                            ticker_list: str = None,
                            start_date: str = None,
                            end_date: str = None,
                            interval: str = None) -> None:
        new_settings = locals()
        new_settings = {k: new_settings[k] for k in new_settings if k in ('ticker_list',
                                                                          'start_date',
                                                                          'end_date',
                                                                          'interval') and new_settings[k]}
        self.ticker_settings.update(new_settings)

    def download_ticker_data(self) -> None:
        """
        Download data from yahoo finance API
        """
        self.ticker_data = yf.download(tickers=self.ticker_settings['ticker_list'],
                                       start=self.ticker_settings['start_date'],
                                       end=self.ticker_settings['end_date'],
                                       interval=self.ticker_settings['interval'])

    def get_ticker_data(self) -> pd.DataFrame:
        return self.ticker_data
