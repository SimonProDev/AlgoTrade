import yfinance as yf
import algotrade_engine.conf.settings as settings
from algotrade_engine.src.ticker import Ticker


class YahooFinanceManager:
    """
    interface manager with yahoo finance API
    """

    def __init__(self):
        self.raw_ticker_data = None
        self.clean_ticker_data = []
        self.ticker_settings = {
            'ticker_list': [],
            'start_date': None,
            'end_date': None,
            'interval': None
        }

    def call_yf_api(self) -> None:
        """
        Function manager to set parameters, download and prepare data
        :return: None
        """
        self.set_ticker_settings(settings.TICKERS,
                                 settings.START_DT,
                                 settings.END_DT,
                                 settings.INTERVAL)
        self.download_ticker_data()
        self.prepare_ticker_data()

    def set_ticker_settings(self,
                            ticker_list: list = None,
                            start_date: str = None,
                            end_date: str = None,
                            interval: str = None) -> None:
        """
        Set parameters for yahoo finance API call
        :param ticker_list: list of tickers defined in config
        :param start_date: start date of data collected
        :param end_date: end date of data collected
        :param interval: interval of data collected
        :return: None
        """
        new_settings = locals()
        new_settings = {k: new_settings[k] for k in new_settings if k in ('ticker_list',
                                                                          'start_date',
                                                                          'end_date',
                                                                          'interval') and new_settings[k]}
        self.ticker_settings.update(new_settings)

    def download_ticker_data(self) -> None:
        """
        Download data from yahoo finance API
        :return: None
        """
        self.raw_ticker_data = yf.download(tickers=self.ticker_settings['ticker_list'],
                                           start=self.ticker_settings['start_date'],
                                           end=self.ticker_settings['end_date'],
                                           interval=self.ticker_settings['interval'])

    def clean_df(self, ticker):
        cleaned_df = self.raw_ticker_data.iloc[:, self.raw_ticker_data.columns.get_level_values(1) == ticker] \
            .sort_index(ascending=False) \
            .dropna()
        cleaned_df['t'] = [f't{i}' for i in range(len(cleaned_df.index))]
        return cleaned_df

    def prepare_ticker_data(self) -> None:
        """
        Clean raw ticker data from yahoo finance API by creating a dict
        with ticker_name and ticker object
        :return: None
        """
        for ticker in self.ticker_settings.get('ticker_list'):
            self.clean_ticker_data.append(Ticker(ticker,
                                                 'type_tbd',
                                                 self.clean_df(ticker)))
        """
        save dataframe for test
        for ticker in self.clean_ticker_data:
            ticker.get_df().to_parquet(f'{ticker.name}')
        """

    def get_ticker_data(self) -> list:
        """
        Return ticker data from yahoo finance API
        after cleaning
        :return: Dic of ticker object
        """
        return self.clean_ticker_data
