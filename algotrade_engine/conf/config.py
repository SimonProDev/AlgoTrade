import importlib
import os
from datetime import datetime
import pytz

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
settings.START_DT = calculate_start_date(90)
settings.END_DT = None
settings.INTERVAL = '1h'

tz_paris = pytz.timezone('Europe/Paris')
settings.CURRENT_TIME = datetime.now(tz_paris).strftime("%H:%M:%S")

settings.logger.info(f"""Application parameters:
Set gmail logins using address: {settings.GMAIL_ADDRESS}
Start date: {settings.START_DT}
End date: {settings.END_DT}
Interval: {settings.INTERVAL}
Current time: {settings.CURRENT_TIME}
""")
