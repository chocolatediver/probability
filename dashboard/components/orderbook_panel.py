from storage.duckdb_store import DuckDBStore

def render_orderbook_panel(st, symbol: str):
    st.subheader("Latest OrderBook")
    try:
        safe_symbol = symbol.replace("'", "''")
        sql = (
            "SELECT exchange, symbol, timestamp, bids, asks FROM realtime_events "
            f"WHERE type='orderbook' AND symbol='{safe_symbol}' ORDER BY timestamp DESC LIMIT 5"
        )
        df = DuckDBStore().query(sql)
        if len(df) == 0:
            st.info("No orderbook data yet. Run realtime stream first.")
        else:
            st.dataframe(df, use_container_width=True)
    except Exception as exc:
        st.warning(f"Orderbook unavailable: {exc}")
