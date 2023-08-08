import algotrade_engine.conf.settings as settings
from algotrade_engine.src.ticker.ticker import Ticker
from algotrade_engine.src.ticker.tickers_settings import init_tickers_settings


def initialize_tickers():
    settings.TICKERS = [Ticker(*s) for s in init_tickers_settings
                        if s[3] < settings.CURRENT_TIME < s[4]]
