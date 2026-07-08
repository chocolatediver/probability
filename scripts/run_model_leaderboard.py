import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.leaderboard import train_model_leaderboard
from storage.model_store import ModelResultStore

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--market", default="crypto")
    parser.add_argument("--symbol", default="BTC/USDT")
    parser.add_argument("--timeframe", default="1h")
    parser.add_argument("--limit", type=int, default=800)
    parser.add_argument("--models", default=None)
    parser.add_argument("--save", action="store_true")
    args = parser.parse_args()
    model_names = [x.strip() for x in args.models.split(",")] if args.models else None
    df = add_basic_features(normalize_ohlcv(get_collector(args.market).fetch_ohlcv(args.symbol, args.timeframe, args.limit)))
    result = train_model_leaderboard(df, model_names)
    print(result.leaderboard.to_string(index=False))
    if args.save:
        ModelResultStore().save_model_leaderboard(args.market, args.symbol, result.leaderboard)
        print("Saved leaderboard to DuckDB.")

if __name__ == "__main__":
    main()
