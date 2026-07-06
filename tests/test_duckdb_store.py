from storage.duckdb_store import DuckDBStore

def test_duckdb_save_event(tmp_path):
    store = DuckDBStore(str(tmp_path / 'test.duckdb'))
    store.save_event({'market':'crypto','exchange':'binance','type':'trade','symbol':'BTC/USDT','timestamp':1,'price':100.0,'quantity':0.1,'side':'buy','raw':{}})
    df = store.query('SELECT * FROM realtime_events')
    assert len(df) == 1
