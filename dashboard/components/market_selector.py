from dataclasses import dataclass

@dataclass
class MarketSelection:
    market: str
    symbol: str
    timeframe: str
    limit: int

DEFAULT_SYMBOLS = {
    "crypto": ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BTC/KRW"],
    "us": ["AAPL", "NVDA", "MSFT", "TSLA", "SPY", "QQQ"],
    "korea": ["005930", "000660", "035420", "068270"],
}

DEFAULT_TIMEFRAMES = {
    "crypto": ["1m", "5m", "15m", "1h", "4h", "1d"],
    "us": ["1d"],
    "korea": ["1d"],
}

def render_market_selector(st) -> MarketSelection:
    st.sidebar.header("Market Selector")
    market = st.sidebar.selectbox("Market", ["crypto", "us", "korea"], index=0)
    symbol = st.sidebar.selectbox("Symbol", DEFAULT_SYMBOLS[market], index=0)
    timeframes = DEFAULT_TIMEFRAMES[market]
    default_idx = timeframes.index("1h") if "1h" in timeframes else 0
    timeframe = st.sidebar.selectbox("Timeframe", timeframes, index=default_idx)
    limit = st.sidebar.slider("Rows", 100, 2000, 500, step=50)
    return MarketSelection(market=market, symbol=symbol, timeframe=timeframe, limit=limit)
