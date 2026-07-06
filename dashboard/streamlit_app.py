import streamlit as st
from markets.selector import get_collector
from normalize.schema import normalize_ohlcv
from feature_engine.basic import add_basic_features
from prediction_engine.probability import predict_probability
from backtest.simple_backtest import ma_cross_backtest
from ml.train import train_classifier

st.set_page_config(page_title="AI Multi-Market Quant Platform", layout="wide")
st.title("AI Multi-Market Quant Platform v0.4")

market = st.sidebar.selectbox("Market", ["crypto", "us", "korea"])
default_symbol = "BTC/USDT" if market == "crypto" else ("AAPL" if market == "us" else "005930")
symbol = st.sidebar.text_input("Symbol", default_symbol)
limit = st.sidebar.slider("Limit", 100, 1500, 500)
run_train = st.sidebar.checkbox("Train ML model", value=False)

if st.sidebar.button("Run"):
    collector = get_collector(market)
    df = add_basic_features(normalize_ohlcv(collector.fetch_ohlcv(symbol, limit=limit)))
    pred = predict_probability(df)
    bt = ma_cross_backtest(df)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("P(UP)", pred["p_up"])
    c2.metric("P(DOWN)", pred["p_down"])
    c3.metric("Confidence", pred["confidence"])
    c4.metric("Backtest Return", bt["total_return"])

    st.line_chart(df.set_index("datetime")[["close", "ma_20", "bb_upper", "bb_lower"]].dropna())
    st.write("Backtest", bt)

    if run_train:
        _, metrics = train_classifier(df)
        st.write("ML Metrics", metrics)

    st.dataframe(df.tail(100))
