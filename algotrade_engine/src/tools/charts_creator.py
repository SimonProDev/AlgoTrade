import plotly.graph_objects as go
from algotrade_engine.src.strategies.strategy import Strategy


class ChartCreator:
    """
    Create financial charts using plotly library
    from Strategy object using pandas df
    """

    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.chart = None

    def create_chart(self):
        df = self.strategy.ticker.get_df()
        ticker_name = self.strategy.ticker.name
        chart_data = go.Candlestick(x=df['t'],
                                    open=df['Open', ticker_name],
                                    high=df['High', ticker_name],
                                    low=df['Low', ticker_name],
                                    close=df['Adj Close', ticker_name],
                                    increasing_line_color='green',
                                    decreasing_line_color='red')
        self.chart = go.Figure(data=[chart_data])\
            .update_layout(xaxis_rangeslider_visible=False)

    def get_chart(self):
        return self.chart
