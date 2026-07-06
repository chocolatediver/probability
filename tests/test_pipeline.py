from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from prediction_engine.probability import predict_probability

def test_crypto_pipeline():
    collector = get_collector("crypto")
    df = collector.fetch_ohlcv("BTC/USDT", limit=50)
    df = normalize_ohlcv(df)
    df = add_basic_features(df)
    pred = predict_probability(df)
    assert "p_up" in pred
    assert 0 <= pred["p_up"] <= 1
