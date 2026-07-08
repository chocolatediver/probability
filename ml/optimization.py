import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, f1_score
from ml.dataset import make_supervised_dataset

def optimize_baseline_model(df: pd.DataFrame, model_type: str = "random_forest", n_trials: int = 20) -> dict:
    try:
        import optuna
    except Exception as exc:
        return {"model_type": model_type, "status": "skipped", "reason": f"optuna not installed: {exc}", "best_params": {}, "best_score": None}

    X, y, _ = make_supervised_dataset(df)
    split = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    def objective(trial):
        if model_type == "gradient_boosting":
            params = {
                "n_estimators": trial.suggest_int("n_estimators", 50, 400),
                "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.2),
                "max_depth": trial.suggest_int("max_depth", 2, 6),
                "random_state": 42,
            }
            model = GradientBoostingClassifier(**params)
        else:
            params = {
                "n_estimators": trial.suggest_int("n_estimators", 100, 500),
                "max_depth": trial.suggest_int("max_depth", 3, 12),
                "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
                "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 10),
                "random_state": 42,
            }
            model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)
        if hasattr(model, "predict_proba") and len(set(y_test)) > 1:
            return roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
        return f1_score(y_test, model.predict(X_test), zero_division=0)

    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=n_trials)
    return {"model_type": model_type, "status": "ok", "best_params": study.best_params, "best_score": round(float(study.best_value), 6), "n_trials": n_trials}
