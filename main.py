import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from prediction_engine.probability import predict_probability
from storage.sqlite_store import SQLiteStore
from storage.parquet_store import ParquetStore
from storage.duckdb_store import DuckDBStore
from report.exporter import export_prediction_report
from report.markdown_report import export_markdown_report
from backtest.simple_backtest import ma_cross_backtest
from backtest.walk_forward import walk_forward_backtest
from ml.train import train_classifier

def run(market, symbol, timeframe, limit, save, report, parquet, backtest, train, walk_forward, duckdb):
    raw = get_collector(market).fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=limit)
    normalized = normalize_ohlcv(raw)
    features = add_basic_features(normalized)
    prediction = predict_probability(features)
    print('=== Probability Platform v0.5 ===')
    print(f"Market: {market}\nSymbol: {symbol}\nRows: {len(features)}")
    print(f"P(UP): {prediction['p_up']}\nP(DOWN): {prediction['p_down']}\nConfidence: {prediction['confidence']}\nModel: {prediction['model']}")
    bt, metrics = None, None
    if save: print(f"SQLite saved rows: {SQLiteStore().save_ohlcv(normalized)}")
    if parquet: print(f"Columnar saved: {ParquetStore().save_ohlcv(normalized)}")
    if backtest: bt = ma_cross_backtest(features); print(f"Backtest: {bt}")
    if walk_forward: bt = walk_forward_backtest(features); print(f"Walk-forward Backtest: {bt}")
    if duckdb and bt: DuckDBStore().save_backtest_result(market, symbol, bt); print('DuckDB backtest result saved.')
    if train: _, metrics = train_classifier(features); print(f"ML Metrics: {metrics}")
    if report:
        print(f"CSV Report: {export_prediction_report(features, prediction)}")
        print(f"Markdown Report: {export_markdown_report(prediction, bt, metrics)}")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--market', required=True)
    p.add_argument('--symbol', required=True)
    p.add_argument('--timeframe', default='1h')
    p.add_argument('--limit', type=int, default=500)
    p.add_argument('--save', action='store_true')
    p.add_argument('--report', action='store_true')
    p.add_argument('--parquet', action='store_true')
    p.add_argument('--backtest', action='store_true')
    p.add_argument('--train', action='store_true')
    p.add_argument('--walk-forward', action='store_true')
    p.add_argument('--duckdb', action='store_true')
    a = p.parse_args()
    run(a.market, a.symbol, a.timeframe, a.limit, a.save, a.report, a.parquet, a.backtest, a.train, a.walk_forward, a.duckdb)
