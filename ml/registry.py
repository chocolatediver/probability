from dataclasses import dataclass

@dataclass
class ModelSpec:
    name: str
    model_type: str
    available: bool
    description: str

class ModelRegistry:
    def __init__(self):
        self._models = {
            "random_forest": ModelSpec("random_forest", "sklearn", True, "Baseline RandomForest classifier"),
            "gradient_boosting": ModelSpec("gradient_boosting", "sklearn", True, "Baseline GradientBoosting classifier"),
            "xgboost": ModelSpec("xgboost", "optional", self._check_import("xgboost"), "Optional XGBoost classifier"),
            "lightgbm": ModelSpec("lightgbm", "optional", self._check_import("lightgbm"), "Optional LightGBM classifier"),
            "catboost": ModelSpec("catboost", "optional", self._check_import("catboost"), "Optional CatBoost classifier"),
        }

    @staticmethod
    def _check_import(module_name: str) -> bool:
        try:
            __import__(module_name)
            return True
        except Exception:
            return False

    def list_models(self) -> list[ModelSpec]:
        return list(self._models.values())

    def get(self, name: str) -> ModelSpec:
        if name not in self._models:
            raise KeyError(f"Unknown model: {name}")
        return self._models[name]

    def available_names(self) -> list[str]:
        return [m.name for m in self._models.values() if m.available]
