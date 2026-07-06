def render_chart_panel(st, df):
    st.subheader("Chart Panel")
    chart_cols = [c for c in ["close", "ma_20", "bb_upper", "bb_lower", "vwap"] if c in df.columns]
    if chart_cols:
        st.line_chart(df.set_index("datetime")[chart_cols].dropna())
    else:
        st.warning("No chart columns available.")

    with st.expander("Indicator Snapshot", expanded=False):
        cols = [c for c in ["datetime", "close", "rsi_14", "macd_hist", "atr_14", "bb_width", "close_to_vwap"] if c in df.columns]
        st.dataframe(df[cols].tail(30), use_container_width=True)
