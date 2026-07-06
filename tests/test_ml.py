from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.train import train_classifier

def test_train_classifier():
    df = add_basic_features(normalize_ohlcv(get_collector("crypto").fetch_ohlcv("BTC/USDT", limit=120)))
    _, metrics = train_classifier(df)
    assert "accuracy" in metrics
    assert metrics["rows"] > 50
