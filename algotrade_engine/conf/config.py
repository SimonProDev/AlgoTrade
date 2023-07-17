import algotrade_engine.conf.settings as settings
import importlib
from pyfiglet import Figlet
import os
from dotenv import load_dotenv


# config logger
importlib.import_module('algotrade_engine.conf.logger')

# config for gmail logins
load_dotenv()
settings.GMAIL_ADDRESS = str(os.getenv('GMAIL_ADDRESS'))
settings.GMAIL_PASSWORD = str(os.getenv('GMAIL_PW'))

# config for yf settings
settings.TICKERS = [
    '^GDAXI',
    'EURUSD=X',
]

settings.START_DT = '2023-07-01'
# settings.END_DT = None
settings.END_DT = '2023-07-04'
settings.INTERVAL = '1h'
settings.logger.info(f"""Application parameters:
Set gmail logins using adress: {settings.GMAIL_ADDRESS}
Tickers analyzed: {", ".join(settings.TICKERS)}
Start date: {settings.START_DT}
End date: {settings.END_DT}
Interval: {settings.INTERVAL}
""")
