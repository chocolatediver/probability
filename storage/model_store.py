import json
import pandas as pd
from storage.duckdb_store import DuckDBStore

class ModelResultStore(DuckDBStore):
    def init_model_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS model_leaderboard (
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                market VARCHAR,
                symbol VARCHAR,
                model VARCHAR,
                accuracy DOUBLE,
                precision DOUBLE,
                recall DOUBLE,
                f1 DOUBLE,
                roc_auc DOUBLE,
                rows INTEGER,
                status VARCHAR,
                meta JSON
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS feature_importance (
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                market VARCHAR,
                symbol VARCHAR,
                model VARCHAR,
                feature VARCHAR,
                importance DOUBLE
            )
        """)

    def save_model_leaderboard(self, market: str, symbol: str, leaderboard_df: pd.DataFrame):
        self.init_model_tables()
        for _, row in leaderboard_df.iterrows():
            self.conn.execute(
                """
                INSERT INTO model_leaderboard
                (market, symbol, model, accuracy, precision, recall, f1, roc_auc, rows, status, meta)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [market, symbol, row.get("model"), _safe_float(row.get("accuracy")), _safe_float(row.get("precision")),
                 _safe_float(row.get("recall")), _safe_float(row.get("f1")), _safe_float(row.get("roc_auc")),
                 _safe_int(row.get("rows")), str(row.get("status")), json.dumps(row.to_dict(), ensure_ascii=False, default=str)],
            )

    def save_feature_importance(self, market: str, symbol: str, model: str, importance_df: pd.DataFrame):
        self.init_model_tables()
        for _, row in importance_df.iterrows():
            self.conn.execute(
                "INSERT INTO feature_importance (market, symbol, model, feature, importance) VALUES (?, ?, ?, ?, ?)",
                [market, symbol, model, row.get("feature"), _safe_float(row.get("importance"))],
            )

def _safe_float(value):
    try:
        if value is None or pd.isna(value):
            return None
        return float(value)
    except Exception:
        return None

def _safe_int(value):
    try:
        if value is None or pd.isna(value):
            return None
        return int(value)
    except Exception:
        return None
