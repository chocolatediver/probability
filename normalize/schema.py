import pandas as pd

REQUIRED_COLUMNS = [
    "datetime", "market", "symbol", "open", "high", "low", "close", "volume", "source"
]

def normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    out = df[REQUIRED_COLUMNS].copy()
    out["datetime"] = pd.to_datetime(out["datetime"], utc=True)
    for c in ["open", "high", "low", "close", "volume"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    return out.dropna().sort_values("datetime").reset_index(drop=True)
