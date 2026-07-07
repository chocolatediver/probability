import streamlit as st

from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from prediction_engine.probability import predict_probability
from backtest.simple_backtest import ma_cross_backtest
from backtest.walk_forward import walk_forward_backtest
from ml.train import train_classifier
from probability_version import VERSION

from dashboard.components.market_selector import render_market_selector
from dashboard.components.status_card import render_status_cards
from dashboard.components.chart_panel import render_chart_panel
from dashboard.components.performance_card import render_performance_card
from dashboard.components.duckdb_explorer import render_duckdb_explorer
from dashboard.components.orderbook_panel import render_orderbook_panel
from dashboard.components.log_panel import render_log_panel

st.set_page_config(page_title="Probability Platform", layout="wide")
st.title(f"Probability Platform v{VERSION}")
st.caption("AI Multi-Market Quant Research Dashboard")

selection = render_market_selector(st)

st.sidebar.header("Actions")
run_analysis = st.sidebar.button("Run Analysis", type="primary")
run_train = st.sidebar.checkbox("Train ML model", value=False)
run_walk_forward = st.sidebar.checkbox("Walk-forward backtest", value=False)

logs = []

if run_analysis:
    try:
        logs.append(f"Loading {selection.market}:{selection.symbol}")
        collector = get_collector(selection.market)
        raw = collector.fetch_ohlcv(selection.symbol, selection.timeframe, selection.limit)
        df = add_basic_features(normalize_ohlcv(raw))
        pred = predict_probability(df)
        latest_close = float(df.dropna().iloc[-1]["close"])
        logs.append("Prediction completed")

        render_status_cards(st, pred, latest_close, len(df))

        tab_chart, tab_perf, tab_duckdb, tab_orderbook, tab_data, tab_logs = st.tabs([
            "Chart", "Backtest", "DuckDB", "OrderBook", "Data", "Logs"
        ])

        with tab_chart:
            render_chart_panel(st, df)

        with tab_perf:
            if run_walk_forward:
                bt = walk_forward_backtest(df)
                logs.append("Walk-forward backtest completed")
            else:
                bt = ma_cross_backtest(df)
                logs.append("MA cross backtest completed")
            render_performance_card(st, bt)

            if run_train:
                _, metrics = train_classifier(df)
                st.subheader("ML Training Metrics")
                st.json(metrics)
                logs.append("ML model training completed")

        with tab_duckdb:
            render_duckdb_explorer(st)

        with tab_orderbook:
            render_orderbook_panel(st, selection.symbol)

        with tab_data:
            st.subheader("Feature Data")
            st.dataframe(df.tail(200), use_container_width=True)

        with tab_logs:
            render_log_panel(st, logs)

    except Exception as exc:
        st.error(f"Dashboard run failed: {exc}")
        render_log_panel(st, logs + [str(exc)])
else:
    st.info("Select market and press Run Analysis.")
    st.markdown(
        '''
        ### Dashboard Features
        - Market selector
        - Probability status cards
        - Chart panel
        - Backtest panel
        - DuckDB explorer
        - Latest orderbook viewer
        '''
    )
