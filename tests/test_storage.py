from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from storage.sqlite_store import SQLiteStore

def test_sqlite_store(tmp_path):
    df = normalize_ohlcv(get_collector("us").fetch_ohlcv("AAPL", limit=10))
    store = SQLiteStore(str(tmp_path / "test.sqlite"))
    store.save_ohlcv(df)
    loaded = store.load_ohlcv("us", "AAPL")
    assert len(loaded) == 10
