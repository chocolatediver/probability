def signal_from_probability(p_up: float) -> str:
    if p_up >= 0.6:
        return "BUY"
    if p_up <= 0.4:
        return "SELL"
    return "HOLD"

def render_status_cards(st, prediction: dict, latest_close: float, rows: int):
    p_up = float(prediction.get("p_up", 0.5))
    p_down = float(prediction.get("p_down", 0.5))
    confidence = float(prediction.get("confidence", 0.0))
    signal = signal_from_probability(p_up)

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Latest Price", f"{latest_close:,.4f}")
    c2.metric("P(UP)", f"{p_up:.2%}")
    c3.metric("P(DOWN)", f"{p_down:.2%}")
    c4.metric("Confidence", f"{confidence:.2%}")
    c5.metric("Signal", signal)
    st.caption(f"Rows loaded: {rows} | Model: {prediction.get('model', 'unknown')}")
