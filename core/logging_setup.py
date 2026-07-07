import logging
from pathlib import Path
from core.config_loader import ConfigLoader

def setup_logging() -> None:
    try:
        cfg = ConfigLoader().load("logging").get("logging", {})
    except Exception:
        cfg = {}
    level_name = cfg.get("level", "INFO")
    log_file = cfg.get("file", "logs/probability.log")
    fmt = cfg.get("format", "%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=getattr(logging, level_name.upper(), logging.INFO),
        format=fmt,
        handlers=[logging.StreamHandler(), logging.FileHandler(log_file, encoding="utf-8")],
    )
