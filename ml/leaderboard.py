from dataclasses import dataclass
import pandas as pd
from ml.registry import ModelRegistry
from ml.train import train_classifier

@dataclass
class LeaderboardResult:
    leaderboard: pd.DataFrame
    metrics: list[dict]

def train_model_leaderboard(df, model_names: list[str] | None = None) -> LeaderboardResult:
    candidates = model_names or ModelRegistry().available_names()
    rows = []
    for name in candidates:
        try:
            _, metrics = train_classifier(df, model_type=name, out_dir=f"models/{name}")
            rows.append({"model": name, "accuracy": metrics.get("accuracy"), "precision": metrics.get("precision"),
                         "recall": metrics.get("recall"), "f1": metrics.get("f1"), "roc_auc": metrics.get("roc_auc"),
                         "rows": metrics.get("rows"), "status": "ok"})
        except Exception as exc:
            rows.append({"model": name, "accuracy": None, "precision": None, "recall": None, "f1": None,
                         "roc_auc": None, "rows": None, "status": f"failed: {exc}"})
    leaderboard = pd.DataFrame(rows)
    return LeaderboardResult(leaderboard=leaderboard.sort_values(["roc_auc", "f1", "accuracy"], ascending=False, na_position="last"), metrics=rows)
