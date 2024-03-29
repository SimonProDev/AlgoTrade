# parameters for initialisation of tickers
fx_start_active_period = '07:00:00'
fx_end_active_period = '23:00:00'

init_tickers_settings = (
    ('^GDAXI',
     'DAX',
     'EQ_INDEX',
     '09:00:00',
     '18:00:00',
     None),
    ('^FTSE',
     'FTSE',
     'EQ_INDEX',
     '08:00:00',
     '19:00:00',
     None),
    ('^STOXX50E',
     'SX5E',
     'EQ_INDEX',
     '09:00:00',
     '18:00:00',
     None),
    ('^DJI',
     'DJW',
     'EQ_INDEX',
     '15:00:00',
     '22:00:00',
     None),
    ('^GSPC',
     'S&P500',
     'EQ_INDEX',
     '15:00:00',
     '22:00:00',
     None),
    ('^IXIC',
     'NASDAQ',
     'EQ_INDEX',
     '15:00:00',
     '22:00:00',
     None),
    ('GC=F',
     'GOLD',
     'COMMODITIES',
     '05:00:00',
     '23:00:00',
     None),
    ('BZ=F',
     'BRENT',
     'COMMODITIES',
     '05:00:00',
     '23:00:00',
     None),
    ('EURUSD=X',
     'EUR/USD',
     'FOREX',
     fx_start_active_period,
     fx_end_active_period,
     None),
    ('JPY=X',
     'USD/JPY',
     'FOREX',
     fx_start_active_period,
     fx_end_active_period,
     None),
    ('GBPUSD=X',
     'GBP/USD',
     'FOREX',
     fx_start_active_period,
     fx_end_active_period,
     None),
    ('AUDUSD=X',
     'AUD/USD',
     'FOREX',
     fx_start_active_period,
     fx_end_active_period,
     None),
    ('EURGBP=X',
     'EUR/GBP',
     'FOREX',
     fx_start_active_period,
     fx_end_active_period,
     None),
)
