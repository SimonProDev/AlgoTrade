from algotrade_engine.src.yf_api.yf_manager import YahooFinanceManager
from algotrade_engine.src.tools.display_df import display


yf_manager = YahooFinanceManager()
yf_manager.set_ticker_settings(['EURUSD=X', '^GDAXI'], '2023-06-20', None, '1h')
yf_manager.download_ticker_data()
df_res = yf_manager.get_ticker_data()


display(df_res)
display(df_res.iloc[:, df_res.columns.get_level_values(1) == '^GDAXI'])
print()
