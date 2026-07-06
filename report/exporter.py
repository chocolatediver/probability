from pathlib import Path
import pandas as pd

def export_prediction_report(df: pd.DataFrame, prediction: dict, out_dir: str = "data/processed") -> Path:
    path = Path(out_dir)
    path.mkdir(parents=True, exist_ok=True)
    symbol = str(df["symbol"].iloc[-1]).replace("/", "_")
    market = str(df["market"].iloc[-1])
    file_path = path / f"{market}_{symbol}_prediction_report.csv"
    summary = pd.DataFrame([{
        "market": market,
        "symbol": symbol,
        **prediction
    }])
    summary.to_csv(file_path, index=False, encoding="utf-8-sig")
    return file_path
