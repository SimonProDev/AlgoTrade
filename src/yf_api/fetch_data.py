import yfinance as yf


class YahooFinanceManager:
    """
    interface with yahoo finance API
    To be developed when functions are developed
    :param:
    """

    def __init__(self):
        self.name = 'yf_manager'


def get_ticker(ticker_name: str) -> yf.ticker.Ticker:
    return yf.Ticker(ticker_name)


# my_ticker = get_ticker('MSFT')
# print(my_ticker.info)


my_ticker_1 = yf.download('^GDAXI', '2023-06-01', '2023-06-06', interval='1h')
print(my_ticker_1)

# git test