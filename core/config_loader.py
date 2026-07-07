from pathlib import Path
from typing import Any
import yaml

class ConfigLoader:
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)

    def load(self, name: str) -> dict[str, Any]:
        path = self.config_dir / f"{name}.yaml"
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def load_all(self) -> dict[str, Any]:
        result = {}
        for path in sorted(self.config_dir.glob("*.yaml")):
            with path.open("r", encoding="utf-8") as f:
                result[path.stem] = yaml.safe_load(f) or {}
        return result
