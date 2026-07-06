from pathlib import Path
import json
import duckdb
import pandas as pd

class DuckDBStore:
    def __init__(self, db_path: str = 'data/probability.duckdb'):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = duckdb.connect(str(self.db_path))
        self.conn.execute("CREATE TABLE IF NOT EXISTS realtime_events (market VARCHAR, exchange VARCHAR, type VARCHAR, symbol VARCHAR, timestamp BIGINT, price DOUBLE, quantity DOUBLE, side VARCHAR, bids JSON, asks JSON, raw JSON)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS backtest_results (created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, market VARCHAR, symbol VARCHAR, strategy VARCHAR, total_return DOUBLE, max_drawdown DOUBLE, win_rate DOUBLE, trades INTEGER, meta JSON)")

    def save_event(self, event: dict):
        self.conn.execute("INSERT INTO realtime_events VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [event.get('market'), event.get('exchange'), event.get('type'), event.get('symbol'), event.get('timestamp'), event.get('price'), event.get('quantity'), event.get('side'), json.dumps(event.get('bids')) if event.get('bids') is not None else None, json.dumps(event.get('asks')) if event.get('asks') is not None else None, json.dumps(event.get('raw', {}), ensure_ascii=False)])

    def save_backtest_result(self, market: str, symbol: str, result: dict):
        self.conn.execute("INSERT INTO backtest_results (market, symbol, strategy, total_return, max_drawdown, win_rate, trades, meta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", [market, symbol, result.get('strategy'), result.get('total_return'), result.get('max_drawdown'), result.get('win_rate'), result.get('trades'), json.dumps(result, ensure_ascii=False)])

    def query(self, sql: str) -> pd.DataFrame:
        return self.conn.execute(sql).fetchdf()
