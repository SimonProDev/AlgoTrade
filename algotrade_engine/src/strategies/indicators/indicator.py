from abc import ABC, abstractmethod
import pandas as pd


class Indicator(ABC):
    """
    Indicator will be applied in the context of a strategy
    will enrich df with his own metrics
    """

    def get_indicator(self, df) -> pd.DataFrame:
        return self.calculate_indicator(df)

    @abstractmethod
    def calculate_indicator(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
