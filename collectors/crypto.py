import pandas as pd
from .base import BaseCollector

class CryptoCollector(BaseCollector):
    def __init__(self, source: str = "binance"):
        super().__init__(source)

    def fetch_ohlcv(self, symbol: str, timeframe: str = "1h", limit: int = 200) -> pd.DataFrame:
        try:
            import ccxt
            exchange_class = getattr(ccxt, self.source)
            exchange = exchange_class({"enableRateLimit": True})
            rows = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            df = pd.DataFrame(rows, columns=["datetime", "open", "high", "low", "close", "volume"])
            df["datetime"] = pd.to_datetime(df["datetime"], unit="ms", utc=True)
            df["market"] = "crypto"
            df["symbol"] = symbol
            df["source"] = self.source
            return df[["datetime", "market", "symbol", "open", "high", "low", "close", "volume", "source"]]
        except Exception:
            dates = pd.date_range(end=pd.Timestamp.utcnow(), periods=limit, freq="h")
            close = [100.0 + i * 0.1 for i in range(limit)]
            return pd.DataFrame({
                "datetime": dates,
                "market": "crypto",
                "symbol": symbol,
                "open": close,
                "high": [x * 1.01 for x in close],
                "low": [x * 0.99 for x in close],
                "close": close,
                "volume": [1000 + i for i in range(limit)],
                "source": f"{self.source}_sample_fallback",
            })
