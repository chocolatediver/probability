from storage.duckdb_store import DuckDBStore

DEFAULT_QUERIES = {
    "Realtime Events Summary": "SELECT exchange, type, symbol, COUNT(*) AS n FROM realtime_events GROUP BY 1,2,3 ORDER BY n DESC",
    "Latest Trades": "SELECT * FROM realtime_events WHERE type='trade' ORDER BY timestamp DESC LIMIT 50",
    "Latest OrderBook": "SELECT * FROM realtime_events WHERE type='orderbook' ORDER BY timestamp DESC LIMIT 50",
    "Backtest Results": "SELECT * FROM backtest_results ORDER BY created_at DESC LIMIT 50",
}

def render_duckdb_explorer(st):
    st.subheader("DuckDB Explorer")
    query_name = st.selectbox("Saved Query", list(DEFAULT_QUERIES.keys()))
    sql = st.text_area("SQL", DEFAULT_QUERIES[query_name], height=120)
    if st.button("Run DuckDB Query"):
        try:
            df = DuckDBStore().query(sql)
            st.dataframe(df, use_container_width=True)
        except Exception as exc:
            st.error(f"DuckDB query failed: {exc}")
