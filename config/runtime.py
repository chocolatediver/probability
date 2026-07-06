from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class RuntimeConfig:
    data_dir: Path = Path(os.getenv("PROBABILITY_DATA_DIR", "data"))
    duckdb_path: Path = Path(os.getenv("PROBABILITY_DUCKDB_PATH", "data/probability.duckdb"))
    stream_max_events: int = int(os.getenv("PROBABILITY_STREAM_MAX_EVENTS", "100"))

    def ensure_dirs(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.duckdb_path.parent.mkdir(parents=True, exist_ok=True)
        return self

def get_runtime_config() -> RuntimeConfig:
    return RuntimeConfig().ensure_dirs()
