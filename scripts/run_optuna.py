import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.optimization import optimize_baseline_model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--market", default="crypto")
    parser.add_argument("--symbol", default="BTC/USDT")
    parser.add_argument("--timeframe", default="1h")
    parser.add_argument("--limit", type=int, default=800)
    parser.add_argument("--model", default="random_forest", choices=["random_forest", "gradient_boosting"])
    parser.add_argument("--trials", type=int, default=20)
    args = parser.parse_args()
    df = add_basic_features(normalize_ohlcv(get_collector(args.market).fetch_ohlcv(args.symbol, args.timeframe, args.limit)))
    print(optimize_baseline_model(df, args.model, args.trials))

if __name__ == "__main__":
    main()
