from abc import ABC, abstractmethod
from typing import Callable, Dict, Any

class BaseStreamCollector(ABC):
    def __init__(self, symbol: str, max_events: int | None = None):
        self.symbol = symbol
        self.max_events = max_events

    def _should_stop(self, count: int) -> bool:
        return self.max_events is not None and count >= self.max_events

    @abstractmethod
    async def stream_trades(self, on_message: Callable[[Dict[str, Any]], None]):
        raise NotImplementedError

    @abstractmethod
    async def stream_orderbook(self, on_message: Callable[[Dict[str, Any]], None]):
        raise NotImplementedError
