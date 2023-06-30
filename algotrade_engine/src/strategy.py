from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Strategy to be applied on a ticker
    will enrich df with indicators, buy and sell triggers
    """

    def __init__(self, name, df):
        self.name = name
        self.df = df
        self.indicators = None

    def build_strategy(self) -> None:
        self.add_indicators()
        self.add_buy_triggers()
        self.add_sell_triggers()

    @abstractmethod
    def add_indicators(self) -> None:
        pass

    @abstractmethod
    def add_buy_triggers(self) -> None:
        pass

    @abstractmethod
    def add_sell_triggers(self) -> None:
        pass
