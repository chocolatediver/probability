import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.train import train_classifier

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--market", required=True)
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--timeframe", default="1h")
    parser.add_argument("--limit", type=int, default=500)
    parser.add_argument("--model", default="random_forest", choices=["random_forest", "gradient_boosting"])
    args = parser.parse_args()

    collector = get_collector(args.market)
    df = add_basic_features(normalize_ohlcv(collector.fetch_ohlcv(args.symbol, args.timeframe, args.limit)))
    _, metrics = train_classifier(df, args.model)
    print("=== Training Complete ===")
    print(metrics)

if __name__ == "__main__":
    main()
