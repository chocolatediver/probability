import pandas as pd
from .base import BaseCollector

class USStockCollector(BaseCollector):
    def __init__(self, source: str = "yahoo"):
        super().__init__(source)

    def fetch_ohlcv(self, symbol: str, timeframe: str = "1d", limit: int = 200) -> pd.DataFrame:
        try:
            import yfinance as yf
            interval = "1d" if timeframe in ["1d", "D"] else timeframe
            period = "1y" if limit <= 252 else "5y"
            hist = yf.download(symbol, period=period, interval=interval, progress=False, auto_adjust=False)
            hist = hist.tail(limit).reset_index()
            dt_col = "Date" if "Date" in hist.columns else "Datetime"
            df = pd.DataFrame({
                "datetime": pd.to_datetime(hist[dt_col], utc=True),
                "market": "us",
                "symbol": symbol,
                "open": hist["Open"].astype(float),
                "high": hist["High"].astype(float),
                "low": hist["Low"].astype(float),
                "close": hist["Close"].astype(float),
                "volume": hist["Volume"].astype(float),
                "source": self.source,
            })
            return df
        except Exception:
            dates = pd.date_range(end=pd.Timestamp.utcnow(), periods=limit, freq="D")
            close = [150 + i * 0.05 for i in range(limit)]
            return pd.DataFrame({
                "datetime": dates,
                "market": "us",
                "symbol": symbol,
                "open": close,
                "high": [x * 1.01 for x in close],
                "low": [x * 0.99 for x in close],
                "close": close,
                "volume": [500000 + i * 100 for i in range(limit)],
                "source": f"{self.source}_sample_fallback",
            })
