import json
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

from .dataset import make_supervised_dataset

def train_classifier(df: pd.DataFrame, model_type: str = "random_forest", out_dir: str = "models"):
    X, y, features = make_supervised_dataset(df)
    if len(X) < 50:
        raise ValueError("학습 데이터가 부족합니다. limit을 100 이상으로 늘리세요.")

    split = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    if model_type == "gradient_boosting":
        model = GradientBoostingClassifier(random_state=42)
    else:
        model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)

    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    metrics = {
        "model_type": model_type,
        "rows": int(len(X)),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "accuracy": round(float(accuracy_score(y_test, pred)), 6),
        "precision": round(float(precision_score(y_test, pred, zero_division=0)), 6),
        "recall": round(float(recall_score(y_test, pred, zero_division=0)), 6),
        "roc_auc": round(float(roc_auc_score(y_test, proba)), 6) if len(set(y_test)) > 1 else None,
        "features": features,
    }

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    try:
        import joblib
        joblib.dump(model, Path(out_dir) / f"{model_type}.joblib")
    except Exception:
        pass

    with open(Path(out_dir) / f"{model_type}_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    return model, metrics
