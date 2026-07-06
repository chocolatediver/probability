from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from backtest.simple_backtest import ma_cross_backtest

def test_ma_cross_backtest():
    df = add_basic_features(normalize_ohlcv(get_collector("crypto").fetch_ohlcv("BTC/USDT", limit=100)))
    result = ma_cross_backtest(df)
    assert "total_return" in result
    assert "max_drawdown" in result
