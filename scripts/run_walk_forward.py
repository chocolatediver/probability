import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from backtest.walk_forward import walk_forward_backtest
from storage.duckdb_store import DuckDBStore

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--market', default='crypto')
    p.add_argument('--symbol', default='BTC/USDT')
    p.add_argument('--limit', type=int, default=800)
    a = p.parse_args()
    df = add_basic_features(normalize_ohlcv(get_collector(a.market).fetch_ohlcv(a.symbol, limit=a.limit)))
    result = walk_forward_backtest(df)
    DuckDBStore().save_backtest_result(a.market, a.symbol, result)
    print(result)

if __name__ == '__main__':
    main()
