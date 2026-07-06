import sqlite3
from pathlib import Path
import pandas as pd

SCHEMA = '''
CREATE TABLE IF NOT EXISTS ohlcv (
    datetime TEXT NOT NULL,
    market TEXT NOT NULL,
    symbol TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume REAL,
    source TEXT,
    PRIMARY KEY (datetime, market, symbol, source)
);
'''

class SQLiteStore:
    def __init__(self, db_path: str = "data/market_data.sqlite"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute(SCHEMA)
        self.conn.commit()

    def save_ohlcv(self, df: pd.DataFrame) -> int:
        before = self.conn.total_changes
        rows = df.copy()
        rows["datetime"] = rows["datetime"].astype(str)
        rows.to_sql("ohlcv_temp", self.conn, if_exists="replace", index=False)
        self.conn.execute('''
            INSERT OR REPLACE INTO ohlcv
            SELECT datetime, market, symbol, open, high, low, close, volume, source
            FROM ohlcv_temp
        ''')
        self.conn.commit()
        return self.conn.total_changes - before

    def load_ohlcv(self, market: str, symbol: str) -> pd.DataFrame:
        return pd.read_sql_query(
            "SELECT * FROM ohlcv WHERE market=? AND symbol=? ORDER BY datetime",
            self.conn,
            params=(market, symbol),
            parse_dates=["datetime"],
        )
