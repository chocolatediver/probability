from ml.dataset import DEFAULT_FEATURES

def predict_with_model(df, model):
    row = df.dropna().iloc[-1]
    features = [c for c in DEFAULT_FEATURES if c in df.columns]
    X = row[features].to_frame().T
    p_up = float(model.predict_proba(X)[0, 1])
    return {
        "p_up": round(p_up, 4),
        "p_down": round(1 - p_up, 4),
        "confidence": round(abs(p_up - 0.5) * 2, 4),
        "model": type(model).__name__,
        "features": features,
    }
