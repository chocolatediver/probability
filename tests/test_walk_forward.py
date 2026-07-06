from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from backtest.walk_forward import walk_forward_backtest

def test_walk_forward_backtest():
    df = add_basic_features(normalize_ohlcv(get_collector('crypto').fetch_ohlcv('BTC/USDT', limit=300)))
    result = walk_forward_backtest(df, train_window=100, test_window=20)
    assert 'total_return' in result
    assert result['strategy'].startswith('walk_forward')
