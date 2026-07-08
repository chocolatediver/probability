import pandas as pd

def feature_importance_dataframe(metrics: dict) -> pd.DataFrame:
    return pd.DataFrame(metrics.get("feature_importance", []), columns=["feature", "importance"])
