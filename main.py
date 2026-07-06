import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from prediction_engine.probability import predict_probability
from storage.sqlite_store import SQLiteStore
from storage.parquet_store import ParquetStore
from report.exporter import export_prediction_report
from report.markdown_report import export_markdown_report
from backtest.simple_backtest import ma_cross_backtest
from ml.train import train_classifier

def run(market: str, symbol: str, timeframe: str, limit: int, save: bool, report: bool, parquet: bool, backtest: bool, train: bool):
    collector = get_collector(market)
    raw = collector.fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=limit)
    normalized = normalize_ohlcv(raw)
    features = add_basic_features(normalized)
    prediction = predict_probability(features)

    print("=== AI Multi-Market Quant Platform v0.4 ===")
    print(f"Market: {market}")
    print(f"Symbol: {symbol}")
    print(f"Rows: {len(features)}")
    print(f"P(UP): {prediction['p_up']}")
    print(f"P(DOWN): {prediction['p_down']}")
    print(f"Confidence: {prediction['confidence']}")
    print(f"Model: {prediction['model']}")

    bt = None
    metrics = None

    if save:
        inserted = SQLiteStore().save_ohlcv(normalized)
        print(f"SQLite saved rows: {inserted}")

    if parquet:
        path = ParquetStore().save_ohlcv(normalized)
        print(f"Columnar saved: {path}")

    if backtest:
        bt = ma_cross_backtest(features)
        print(f"Backtest: {bt}")

    if train:
        _, metrics = train_classifier(features)
        print(f"ML Metrics: {metrics}")

    if report:
        csv_path = export_prediction_report(features, prediction)
        md_path = export_markdown_report(prediction, bt, metrics)
        print(f"CSV Report: {csv_path}")
        print(f"Markdown Report: {md_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--market", required=True, help="crypto | us | korea")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--timeframe", default="1h")
    parser.add_argument("--limit", type=int, default=300)
    parser.add_argument("--save", action="store_true")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--parquet", action="store_true")
    parser.add_argument("--backtest", action="store_true")
    parser.add_argument("--train", action="store_true")
    args = parser.parse_args()
    run(args.market, args.symbol, args.timeframe, args.limit, args.save, args.report, args.parquet, args.backtest, args.train)
