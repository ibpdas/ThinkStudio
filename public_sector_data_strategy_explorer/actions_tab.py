# actions_tab.py
import pandas as pd
import streamlit as st
from lenses_tab import ensure_sessions


def render_actions() -> None:
    ensure_sessions()
    st.subheader("Actions & Export")
    st.caption(
        "Turn your top priority shifts into an action log. "
        "Assign owners, timelines and metrics, then export to CSV."
    )

    actions_df = st.session_state.get("_actions_df", pd.DataFrame())

    if actions_df.empty:
        st.info(
            "No priority shifts have been generated yet. "
            "Go to the Journey tab to calculate gaps and priorities."
        )
        return

    st.markdown("### Action log (editable)")
    edited = st.data_editor(
        actions_df,
        num_rows="dynamic",
        use_container_width=True,
        key="actions_editor",
    )
    st.session_state["_actions_df"] = edited

    csv_bytes = edited.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download actions as CSV",
        data=csv_bytes,
        file_name="data_strategy_actions.csv",
        mime="text/csv",
    )

    st.markdown(
        "> Tip: paste this table into your programme plan or OKRs to track progress."
    )
