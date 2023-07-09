import plotly.graph_objects as go
import pandas as pd
from algotrade_engine.src.tools.display_df import display

df = pd.read_parquet('../../dev/^GDAXI')
# print(df['Adj Close', '^GDAXI'])
# display(df.loc['Open.^GDAXI'])
# print()
fig = go.Figure(data=[go.Candlestick(x=df['t'],
                open=df['Open', '^GDAXI'],
                high=df['High', '^GDAXI'],
                low=df['Low', '^GDAXI'],
                close=df['Adj Close', '^GDAXI'])])
fig.update_layout(yaxis_range=[15_400, 16_400])
fig.show()
