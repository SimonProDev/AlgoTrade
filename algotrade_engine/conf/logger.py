import logging
import algotrade_engine.conf.settings as settings

# Logger config
logging.basicConfig(filename="algotrade_engine/tmp_files/logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Create logger
logger = logging.getLogger('ALGOTRADE_LOGGER')
logger.setLevel(logging.DEBUG)

# Create handler parameters
cons_handler = logging.StreamHandler()
cons_handler.setLevel(logging.INFO)

# Set format of logger message
cons_format = logging.Formatter('%(name)s - [%(levelname)s] - %(message)s')
cons_handler.setFormatter(cons_format)

# Add handler to logger
logger.addHandler(cons_handler)

# Add logger to settings variable
settings.logger = logger
logger.info(f'Logger initialized with severity level set at {logger.level}')
