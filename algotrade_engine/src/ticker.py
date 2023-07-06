from algotrade_engine.src.strategies.strategy import Strategy


class Ticker:
    """
    Ticker to be called in yahoo finance API
    A strategy will be applied to each ticker enriching the dataframe
    """

    def __init__(self, name, ticker_type, df):
        self.name = name
        self.ticker_type = ticker_type
        self.df = df
        self.strategy = None

    def run_strategy(self, strategy: Strategy) -> None:
        self.add_strategy(strategy)
        self.df = self.strategy.build_strategy(self.df)

    def add_strategy(self, strategy: Strategy) -> None:
        self.strategy = strategy
