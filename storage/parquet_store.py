from pathlib import Path
import pandas as pd

class ParquetStore:
    def __init__(self, root_dir: str = "data/parquet"):
        self.root_dir = Path(root_dir)
        self.root_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, market: str, symbol: str) -> Path:
        safe_symbol = symbol.replace("/", "_").replace(":", "_")
        return self.root_dir / market / f"{safe_symbol}.parquet"

    def save_ohlcv(self, df: pd.DataFrame) -> Path:
        market = str(df["market"].iloc[-1])
        symbol = str(df["symbol"].iloc[-1])
        path = self._path(market, symbol)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            df.to_parquet(path, index=False)
            return path
        except Exception:
            csv_path = path.with_suffix(".csv")
            df.to_csv(csv_path, index=False, encoding="utf-8-sig")
            return csv_path

    def load_ohlcv(self, market: str, symbol: str) -> pd.DataFrame:
        path = self._path(market, symbol)
        if path.exists():
            return pd.read_parquet(path)
        csv_path = path.with_suffix(".csv")
        if csv_path.exists():
            return pd.read_csv(csv_path, parse_dates=["datetime"])
        raise FileNotFoundError(f"No stored file for {market}:{symbol}")
