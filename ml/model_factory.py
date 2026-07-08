from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def create_classifier(model_type: str):
    model_type = model_type.lower()
    if model_type == "random_forest":
        return RandomForestClassifier(n_estimators=300, max_depth=8, random_state=42)
    if model_type == "gradient_boosting":
        return GradientBoostingClassifier(random_state=42)
    if model_type == "xgboost":
        try:
            from xgboost import XGBClassifier
        except Exception as exc:
            raise ImportError("xgboost is not installed. Install with: pip install xgboost") from exc
        return XGBClassifier(n_estimators=300, max_depth=4, learning_rate=0.05, eval_metric="logloss", random_state=42)
    if model_type == "lightgbm":
        try:
            from lightgbm import LGBMClassifier
        except Exception as exc:
            raise ImportError("lightgbm is not installed. Install with: pip install lightgbm") from exc
        return LGBMClassifier(n_estimators=300, learning_rate=0.05, random_state=42, verbose=-1)
    if model_type == "catboost":
        try:
            from catboost import CatBoostClassifier
        except Exception as exc:
            raise ImportError("catboost is not installed. Install with: pip install catboost") from exc
        return CatBoostClassifier(iterations=300, depth=5, learning_rate=0.05, random_seed=42, verbose=False)
    raise ValueError(f"Unsupported model_type: {model_type}")
