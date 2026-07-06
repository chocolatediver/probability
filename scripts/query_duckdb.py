import argparse
from storage.duckdb_store import DuckDBStore

DEFAULT_QUERIES = {
    "events": "SELECT exchange, type, symbol, COUNT(*) AS n FROM realtime_events GROUP BY 1,2,3 ORDER BY n DESC",
    "trades": "SELECT * FROM realtime_events WHERE type='trade' ORDER BY timestamp DESC LIMIT 20",
    "orderbook": "SELECT * FROM realtime_events WHERE type='orderbook' ORDER BY timestamp DESC LIMIT 20",
    "backtests": "SELECT * FROM backtest_results ORDER BY created_at DESC LIMIT 20",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", choices=DEFAULT_QUERIES.keys(), default="events")
    parser.add_argument("--sql", default=None)
    args = parser.parse_args()
    print(DuckDBStore().query(args.sql or DEFAULT_QUERIES[args.name]))

if __name__ == "__main__":
    main()
