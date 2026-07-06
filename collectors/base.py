from abc import ABC, abstractmethod
import pandas as pd

class BaseCollector(ABC):
    def __init__(self, source: str):
        self.source = source

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, timeframe: str = "1h", limit: int = 200) -> pd.DataFrame:
        raise NotImplementedError
