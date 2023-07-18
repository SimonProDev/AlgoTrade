from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager


yf_manager = YahooFinanceManager()
yf_manager.set_ticker_settings(ticker_list=['EURUSD=X'],
                               start_date='2023-07-01',
                               end_date='',
                               interval='1h')
yf_manager.download_ticker_data()
print(yf_manager.raw_ticker_data)
