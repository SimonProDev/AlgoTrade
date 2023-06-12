import pandas as pd
import yfinance as yf


class YahooFinanceAPI:
    """
    interface with yahoo finance API
    To be developed when functions are developed
    :param:
    """

    def __init__(self):
        self.ticker_data = None
        self.ticker_settings = {
            'ticker_name': None,
            'start_date': None,
            'end_date': None,
            'interval': None
        }

    def set_ticker_settings(self,
                            ticker_name: str = None,
                            start_date: str = None,
                            end_date: str = None,
                            interval: str = None) -> None:
        new_settings = locals()
        new_settings = {k: new_settings[k] for k in new_settings if k in ('ticker_name',
                                                                          'start_date',
                                                                          'end_date',
                                                                          'interval') and new_settings[k]}
        self.ticker_settings.update(new_settings)

    def download_ticker_data(self) -> None:
        """
        Download data from yahoo finance API
        """
        if self.ticker_settings['end_date']:
            self.ticker_data = yf.download(tickers=self.ticker_settings['ticker_name'],
                                           start=self.ticker_settings['start_date'],
                                           end=self.ticker_settings['end_date'],
                                           interval=self.ticker_settings['interval'])
        else:
            self.ticker_data = yf.download(tickers=self.ticker_settings['ticker_name'],
                                           start=self.ticker_settings['start_date'],
                                           interval=self.ticker_settings['interval'])

    def get_ticker_data(self) -> pd.DataFrame:
        return self.ticker_data


pd.set_option('display.max_columns', None)

yf_manager = YahooFinanceAPI()
# yf_manager.set_ticker_settings('^GDAXI', '2023-06-05', '2023-06-12', '1h')
yf_manager.set_ticker_settings('^GDAXI', '2023-06-05', None, '1h')
yf_manager.download_ticker_data()
df_res = yf_manager.get_ticker_data()


print(df_res)
# print(df_res.loc['2023-06-05 10:00:00+02:00':'2023-06-05 17:00:00+02:00'])
