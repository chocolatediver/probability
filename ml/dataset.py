import pandas as pd

DEFAULT_FEATURES = [
    "return_1", "log_return_1", "ma_5", "ma_10", "ma_20", "ma_60",
    "ema_5", "ema_10", "ema_20", "ema_60", "volatility_20",
    "rsi_14", "macd", "macd_signal", "macd_hist", "atr_14",
    "bb_upper", "bb_mid", "bb_lower", "bb_width",
    "stoch_k", "stoch_d", "obv", "vwap", "close_to_vwap"
]

def make_supervised_dataset(df: pd.DataFrame, horizon: int = 1):
    data = df.copy()
    data["target"] = (data["close"].shift(-horizon) > data["close"]).astype(int)
    available = [c for c in DEFAULT_FEATURES if c in data.columns]
    dataset = data[available + ["target"]].replace([float("inf"), -float("inf")], pd.NA).dropna()
    X = dataset[available]
    y = dataset["target"]
    return X, y, available
