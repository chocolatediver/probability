import pandas as pd
from ml.explainability import explain_model_features
from storage.model_store import ModelResultStore

def render_feature_importance_panel(st, df, market: str, symbol: str):
    st.subheader("Feature Importance / Explainability")
    model = st.selectbox("Explain model", ["random_forest", "gradient_boosting"], index=0)
    save = st.checkbox("Save feature importance to DuckDB", value=False)
    if st.button("Run Explainability"):
        result = explain_model_features(df, model)
        imp = pd.DataFrame(result["feature_importance"])
        st.caption(f"Method: {result.get('method')}")
        if result.get("error"):
            st.warning(result["error"])
        if not imp.empty:
            st.bar_chart(imp.set_index("feature")["importance"].head(20))
            st.dataframe(imp, use_container_width=True)
            if save:
                ModelResultStore().save_feature_importance(market, symbol, model, imp)
                st.success("Saved feature importance to DuckDB.")
