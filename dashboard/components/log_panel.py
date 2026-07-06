def render_log_panel(st, messages: list[str]):
    st.subheader("Run Logs")
    if not messages:
        st.info("No logs yet.")
        return
    for msg in messages[-20:]:
        st.text(msg)
