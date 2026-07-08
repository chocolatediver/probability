import pandas as pd
from ml.dataset import make_supervised_dataset
from ml.train import train_classifier
from ml.feature_importance import feature_importance_dataframe

def explain_model_features(df: pd.DataFrame, model_type: str = "random_forest", max_rows: int = 300) -> dict:
    X, _, features = make_supervised_dataset(df)
    X_sample = X.tail(max_rows)
    model, metrics = train_classifier(df, model_type=model_type, out_dir=f"models/{model_type}")
    try:
        import shap
        explainer = shap.Explainer(model, X_sample)
        shap_values = explainer(X_sample)
        values = abs(shap_values.values).mean(axis=0)
        importance = pd.DataFrame({"feature": features, "importance": values})
        importance = importance.sort_values("importance", ascending=False).reset_index(drop=True)
        return {"model_type": model_type, "method": "shap", "feature_importance": importance.head(50).to_dict("records")}
    except Exception as exc:
        fallback = feature_importance_dataframe(metrics)
        return {
            "model_type": model_type,
            "method": "model_feature_importance_fallback",
            "error": str(exc),
            "feature_importance": fallback.head(50).to_dict("records"),
        }
