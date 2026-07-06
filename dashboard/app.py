import argparse
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from prediction_engine.probability import predict_probability

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--market", required=True)
    parser.add_argument("--symbol", required=True)
    args = parser.parse_args()

    collector = get_collector(args.market)
    df = add_basic_features(normalize_ohlcv(collector.fetch_ohlcv(args.symbol)))
    pred = predict_probability(df)

    print("\n=== Dashboard Preview ===")
    print(df.tail(5)[["datetime", "close", "rsi_14", "macd_hist", "atr_14"]])
    print("\nPrediction:", pred)

if __name__ == "__main__":
    main()
