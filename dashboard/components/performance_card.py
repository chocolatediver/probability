def render_performance_card(st, backtest_result: dict | None):
    st.subheader("Backtest Performance")
    if not backtest_result:
        st.info("Backtest not executed.")
        return
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Return", f"{backtest_result.get('total_return', 0):.2%}")
    c2.metric("Max Drawdown", f"{backtest_result.get('max_drawdown', 0):.2%}")
    c3.metric("Win Rate", f"{backtest_result.get('win_rate', 0):.2%}")
    c4.metric("Trades", backtest_result.get("trades", 0))
    st.json(backtest_result)
