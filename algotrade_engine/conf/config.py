import importlib
import os
from dotenv import load_dotenv


from algotrade_engine.src.utils.config_utils import calculate_start_date
import algotrade_engine.conf.settings as settings

# config logger
importlib.import_module('algotrade_engine.conf.logger')

# config for gmail logins
load_dotenv()
settings.GMAIL_ADDRESS = str(os.getenv('GMAIL_ADDRESS'))
settings.GMAIL_PASSWORD = str(os.getenv('GMAIL_PW'))

# config for yf settings
settings.TICKERS = [
    '^GDAXI',
    '^FTSE',
    '^STOXX50E',
    '^DJI',
    '^GSPC',
    '^IXIC',
    '^N225',
    'GC=F',
    'BZ=F',
    'EURUSD=X',
    'JPY=X',
    'GBPUSD=X',
    'AUDUSD=X',
    'EURGBP=X',
]

settings.START_DT = calculate_start_date()
settings.END_DT = None
settings.INTERVAL = '1h'

settings.logger.info(f"""Application parameters:
Set gmail logins using adress: {settings.GMAIL_ADDRESS}
Tickers analyzed: {", ".join(settings.TICKERS)}
Start date: {settings.START_DT}
End date: {settings.END_DT}
Interval: {settings.INTERVAL}
""")
