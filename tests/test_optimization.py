from ml.optimization import optimize_baseline_model
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features

def test_optimize_baseline_model_no_crash():
    df = add_basic_features(normalize_ohlcv(get_collector("crypto").fetch_ohlcv("BTC/USDT", limit=160)))
    result = optimize_baseline_model(df, "random_forest", n_trials=1)
    assert "status" in result
