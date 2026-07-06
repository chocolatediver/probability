from collectors.crypto import CryptoCollector
from collectors.us_stock import USStockCollector
from collectors.korea_stock import KoreaStockCollector

def get_collector(market: str):
    market = market.lower()
    if market in ["crypto", "coin", "btc"]:
        return CryptoCollector()
    if market in ["us", "usa", "us_stock"]:
        return USStockCollector()
    if market in ["korea", "kr", "kospi", "kosdaq"]:
        return KoreaStockCollector()
    raise ValueError(f"Unsupported market: {market}")
