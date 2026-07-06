import os
import pandas as pd
from .base import BaseCollector

class KoreaStockCollector(BaseCollector):
    def __init__(self, source: str = "kis"):
        super().__init__(source)

    def fetch_ohlcv(self, symbol: str, timeframe: str = "1d", limit: int = 200) -> pd.DataFrame:
        # v0.3: KIS Open API 연결을 위한 구조를 준비했다.
        # 실제 호출은 APP_KEY/APP_SECRET/ACCESS_TOKEN 발급 후 v0.4에서 활성화한다.
        dates = pd.date_range(end=pd.Timestamp.utcnow(), periods=limit, freq="D")
        close = [70000 + i * 10 for i in range(limit)]
        return pd.DataFrame({
            "datetime": dates,
            "market": "korea",
            "symbol": symbol,
            "open": close,
            "high": [x * 1.01 for x in close],
            "low": [x * 0.99 for x in close],
            "close": close,
            "volume": [1000000 + i * 1000 for i in range(limit)],
            "source": f"{self.source}_sample_fallback",
        })
