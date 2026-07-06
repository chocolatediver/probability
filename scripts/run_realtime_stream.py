import argparse
import asyncio
from realtime.binance_stream import BinanceStreamCollector
from realtime.upbit_stream import UpbitStreamCollector
from storage.duckdb_store import DuckDBStore

def print_and_store(store):
    def handler(event):
        print(event)
        store.save_event(event)
    return handler

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exchange", choices=["binance", "upbit"], default="binance")
    parser.add_argument("--symbol", default="BTC/USDT")
    parser.add_argument("--type", choices=["trade", "orderbook"], default="trade")
    parser.add_argument("--max-events", type=int, default=20)
    args = parser.parse_args()

    collector_cls = BinanceStreamCollector if args.exchange == "binance" else UpbitStreamCollector
    try:
        collector = collector_cls(args.symbol, max_events=args.max_events)
    except TypeError:
        collector = collector_cls(args.symbol)
        collector.max_events = args.max_events

    store = DuckDBStore()
    handler = print_and_store(store)
    if args.type == "trade":
        await collector.stream_trades(handler)
    else:
        await collector.stream_orderbook(handler)

if __name__ == "__main__":
    asyncio.run(main())
