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
            'ticker_name': '',
            'start_date': '',
            'end_date': '',
            'interval': ''
        }

    def set_ticker_settings(self,
                            ticker_name: str = '',
                            start_date: str = '',
                            end_date: str = '',
                            interval: str = '') -> None:
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

        self.ticker_data = yf.download(tickers=self.ticker_settings['ticker_name'],
                                       start=self.ticker_settings['start_date'],
                                       end=self.ticker_settings['end_date'],
                                       interval=self.ticker_settings['interval'])

    def get_ticker_data(self) -> pd.DataFrame:
        return self.ticker_data


yf_manager = YahooFinanceAPI()
yf_manager.set_ticker_settings('^GDAXI', '2023-06-01', '2023-06-06', '1h')
yf_manager.download_ticker_data()
df_res = yf_manager.get_ticker_data()

print(df_res)
print(yf_manager.ticker_settings)
