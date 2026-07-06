import pandas as pd

def predict_probability(df: pd.DataFrame) -> dict:
    latest = df.dropna().iloc[-1]
    trend_score = 0.5
    if latest.get("ma_5", 0) > latest.get("ma_20", 0):
        trend_score += 0.1
    if latest.get("return_1", 0) > 0:
        trend_score += 0.05
    p_up = max(0.01, min(0.99, trend_score))
    return {
        "p_up": round(float(p_up), 4),
        "p_down": round(float(1 - p_up), 4),
        "confidence": round(float(abs(p_up - 0.5) * 2), 4),
        "model": "v0.1_stub_probability_engine"
    }
