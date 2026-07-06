import math
import pandas as pd
from .indicators import rsi, macd, atr, bollinger, stochastic, obv, vwap

def add_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["return_1"] = out["close"].pct_change()
    out["log_return_1"] = (out["close"] / out["close"].shift(1)).apply(
        lambda x: 0 if pd.isna(x) or x <= 0 else math.log(x)
    )
    for window in [5, 10, 20, 60]:
        out[f"ma_{window}"] = out["close"].rolling(window).mean()
        out[f"ema_{window}"] = out["close"].ewm(span=window, adjust=False).mean()
    out["volatility_20"] = out["return_1"].rolling(20).std()
    out["rsi_14"] = rsi(out["close"], 14)
    out["macd"], out["macd_signal"], out["macd_hist"] = macd(out["close"])
    out["atr_14"] = atr(out, 14)
    out["bb_upper"], out["bb_mid"], out["bb_lower"], out["bb_width"] = bollinger(out["close"])
    out["stoch_k"], out["stoch_d"] = stochastic(out)
    out["obv"] = obv(out)
    out["vwap"] = vwap(out)
    out["close_to_vwap"] = out["close"] / out["vwap"] - 1
    return out
