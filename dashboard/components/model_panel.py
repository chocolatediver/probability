from ml.registry import ModelRegistry
from ml.leaderboard import train_model_leaderboard

def render_model_registry_panel(st, df=None):
    st.subheader("AI Model Registry")
    registry = ModelRegistry()
    rows = [{"name": s.name, "type": s.model_type, "available": s.available, "description": s.description} for s in registry.list_models()]
    st.dataframe(rows, use_container_width=True)
    if df is None:
        return
    st.subheader("Model Leaderboard")
    selected = st.multiselect("Models", [s.name for s in registry.list_models()], default=registry.available_names()[:2])
    if st.button("Run Model Leaderboard"):
        result = train_model_leaderboard(df, selected)
        st.dataframe(result.leaderboard, use_container_width=True)
