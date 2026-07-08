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
from dashboard.components.model_panel import render_model_registry_panel
from dashboard.components.feature_importance_panel import render_feature_importance_panel

st.set_page_config(page_title="Probability Platform", layout="wide")
st.title(f"Probability Platform v{VERSION}")
selection = render_market_selector(st)
st.sidebar.header("Actions")
run_analysis = st.sidebar.button("Run Analysis", type="primary")
run_train = st.sidebar.checkbox("Train ML model", value=False)
run_walk_forward = st.sidebar.checkbox("Walk-forward backtest", value=False)
logs = []

if run_analysis:
    try:
        df = add_basic_features(normalize_ohlcv(get_collector(selection.market).fetch_ohlcv(selection.symbol, selection.timeframe, selection.limit)))
        pred = predict_probability(df)
        render_status_cards(st, pred, float(df.dropna().iloc[-1]["close"]), len(df))
        tabs = st.tabs(["Chart", "Backtest", "AI Models", "Explainability", "DuckDB", "OrderBook", "Data", "Logs"])
        with tabs[0]:
            render_chart_panel(st, df)
        with tabs[1]:
            bt = walk_forward_backtest(df) if run_walk_forward else ma_cross_backtest(df)
            render_performance_card(st, bt)
            if run_train:
                _, metrics = train_classifier(df)
                st.json(metrics)
        with tabs[2]:
            render_model_registry_panel(st, df)
        with tabs[3]:
            render_feature_importance_panel(st, df, selection.market, selection.symbol)
        with tabs[4]:
            render_duckdb_explorer(st)
        with tabs[5]:
            render_orderbook_panel(st, selection.symbol)
        with tabs[6]:
            st.dataframe(df.tail(200), use_container_width=True)
        with tabs[7]:
            render_log_panel(st, logs)
    except Exception as exc:
        st.error(f"Dashboard run failed: {exc}")
        render_log_panel(st, logs + [str(exc)])
else:
    st.info("Select market and press Run Analysis.")
    render_model_registry_panel(st)
