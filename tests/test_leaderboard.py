from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.leaderboard import train_model_leaderboard

def test_train_model_leaderboard_baselines():
    df = add_basic_features(normalize_ohlcv(get_collector("crypto").fetch_ohlcv("BTC/USDT", limit=160)))
    result = train_model_leaderboard(df, ["random_forest", "gradient_boosting"])
    assert len(result.leaderboard) == 2
    assert "accuracy" in result.leaderboard.columns
