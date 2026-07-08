from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.explainability import explain_model_features

def test_explain_model_features_fallback():
    df = add_basic_features(normalize_ohlcv(get_collector("crypto").fetch_ohlcv("BTC/USDT", limit=160)))
    result = explain_model_features(df, "random_forest", max_rows=50)
    assert "feature_importance" in result
    assert len(result["feature_importance"]) > 0
