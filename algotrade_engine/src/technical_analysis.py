from abc import ABC, abstractmethod


class Indicator(ABC):
    """
    Indicator will be applied in the context of a strategy
    will enrich df with his own metrics
    """

    def __init__(self, name):
        self.name = name

    def get_indicator(self, df) -> None:
        return self.add_indicator(df)

    @abstractmethod
    def add_indicator(self, df) -> None:
        pass
