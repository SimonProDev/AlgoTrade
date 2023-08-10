import plotly.graph_objects as go

from algotrade_engine.conf import settings
from algotrade_engine.src.ticker.ticker import Ticker


class ChartCreator:
    """
    Create financial charts using plotly library
    from Strategy object using pandas df
    """

    def __init__(self, ticker: Ticker):
        self.ticker = ticker
        self.chart = None

    def create_chart(self) -> None:
        settings.logger.info(f'CREATE CHART FOR TICKER: {self.ticker.yf_api_name}')
        self.create_candlestick_chart()
        settings.logger.info(f'SAVE CHART FOR TICKER: {self.ticker.yf_api_name}')
        self.save_chart()

    def create_candlestick_chart(self) -> None:
        df = self.ticker.get_df().sort_index(ascending=True).iloc[:51]
        ticker_name = self.ticker.yf_api_name
        chart_data = go.Candlestick(x=df['t'],
                                    open=df['Open', ticker_name],
                                    high=df['High', ticker_name],
                                    low=df['Low', ticker_name],
                                    close=df['Adj Close', ticker_name],
                                    increasing_line_color='light grey',
                                    decreasing_line_color='black')
        self.chart = go.Figure(data=[chart_data])\
            .update_layout(xaxis_rangeslider_visible=False,
                           title=dict(text=ticker_name,
                                      font=dict(size=40)))

    def save_chart(self) -> None:
        self.chart.write_image(f'/tmp/{self.ticker.yf_api_name}_chart.jpg')

    def get_chart(self) -> go.Figure:
        return self.chart
