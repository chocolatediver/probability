from collectors.crypto import CryptoCollector
from collectors.us_stock import USStockCollector
from collectors.korea_stock import KoreaStockCollector

class CollectorFactory:
    @staticmethod
    def create(market: str, source: str | None = None):
        market = market.lower()
        if market in {"crypto", "coin", "btc"}:
            return CryptoCollector(source or "binance")
        if market in {"us", "usa", "us_stock"}:
            return USStockCollector(source or "yahoo")
        if market in {"korea", "kr", "kospi", "kosdaq"}:
            return KoreaStockCollector(source or "kis")
        raise ValueError(f"Unsupported market: {market}")
