import argparse
import pandas as pd
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from ml.explainability import explain_model_features
from storage.model_store import ModelResultStore

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--market", default="crypto")
    parser.add_argument("--symbol", default="BTC/USDT")
    parser.add_argument("--timeframe", default="1h")
    parser.add_argument("--limit", type=int, default=800)
    parser.add_argument("--model", default="random_forest")
    parser.add_argument("--save", action="store_true")
    args = parser.parse_args()
    df = add_basic_features(normalize_ohlcv(get_collector(args.market).fetch_ohlcv(args.symbol, args.timeframe, args.limit)))
    result = explain_model_features(df, args.model)
    imp = pd.DataFrame(result["feature_importance"])
    print(result["method"])
    print(imp.head(30).to_string(index=False))
    if args.save and not imp.empty:
        ModelResultStore().save_feature_importance(args.market, args.symbol, args.model, imp)
        print("Saved feature importance to DuckDB.")

if __name__ == "__main__":
    main()
