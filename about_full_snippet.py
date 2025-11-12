
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render_about_tab_full(container, AXES):
    with container:
        st.subheader("About this Explorer")

        # --- Purpose & Audience
        st.markdown("""
### 🎯 Purpose
Help public bodies **design, communicate, and iterate** their data strategy by making
the **key tensions** explicit, comparing **current vs target**, and turning gaps into **prioritised actions**.

### 👥 Who it's for
- **CDOs / Heads of Data** — to set direction and align leadership.
- **Policy & Ops leaders** — to frame trade‑offs and agree priorities.
- **Analysts & Data teams** — to translate strategy into delivery.
- **PMOs / Transformation** — to track progress and course‑correct.
""")

        # --- How to use
        st.markdown("""
### 🛠️ How to use this tool
1) **Explore** the landscape of strategies (by year, country, org type) for context.  
2) **Set profiles**: use the **Ten Lenses** sliders to define **Current** and **Target** positions.  
3) **Compare** in the **Journey** tab to see directional gaps (left/right) and magnitudes.  
4) **Prioritise** the top shifts and convert them into actions (owners, timelines, measures).  
5) **Re‑assess quarterly** — treat your strategy as **living**.
""")

        # --- Visual Diagram (workflow)
        st.markdown("### 🗺️ Visual: how the tool fits together")
        try:
            import graphviz
            g = graphviz.Digraph(format="svg")
            g.attr(rankdir="LR", fontsize="11")
            g.node("A", "🔎 Explore\nLandscape & filters", shape="rectangle", style="rounded")
            g.node("B", "👁️ Set Profiles\nTen Lenses sliders\n(Current & Target)", shape="rectangle", style="rounded")
            g.node("C", "🧭 Journey\nGap analysis\n(radar + bars + priorities)", shape="rectangle", style="rounded")
            g.node("D", "✅ Action Plan\nOwners • Milestones • Measures", shape="rectangle", style="rounded")
            g.node("E", "♻️ Re‑assess\nQuarterly cadence", shape="rectangle", style="rounded")

            g.edges([("A","B"), ("B","C"), ("C","D"), ("D","E"), ("E","B")])
            st.graphviz_chart(g)
        except Exception:
            st.info("Diagram requires `graphviz`. If unavailable, skip this visual.")

        # --- What the lenses mean
        st.markdown("### 👁️ What the Ten Lenses mean")
        st.caption("Each lens is a **tension to manage** — positions are not 'good' or 'bad', they’re **context‑dependent**.")
        fig = go.Figure()
        for i, (dim, left, right) in enumerate(AXES):
            fig.add_trace(go.Bar(
                x=[50, 50], y=[f"{i+1}. {dim}", f"{i+1}. {dim}"],
                orientation="h", marker_color=["#70A9FF", "#FFB8B8"],
                showlegend=False, hovertext=[left, right]
            ))
        fig.update_layout(barmode="stack", xaxis=dict(showticklabels=False, range=[0,100]),
                          height=460, margin=dict(l=20,r=20,t=10,b=10), title=None)
        st.plotly_chart(fig, use_container_width=True)

        # --- Quick definitions table
        rows = []
        for (dim, left, right) in AXES:
            rows.append({"Lens": dim, "Left (0)": left, "Right (100)": right})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)

        # --- Examples (illustrative, non‑prescriptive)
        st.markdown("### 📚 Examples (illustrative) — how different contexts lean")
        st.caption("Use these to spark discussion — not as templates.")
        examples = pd.DataFrame([
            {"Context": "Estonia (Gov‑wide digital state)", "Lean": "Federated enablement + high adaptability", "Notes": "Shared platforms; domains innovate within standards"},
            {"Context": "Singapore (Smart Nation)", "Lean": "Value‑focused + transformational exemplars", "Notes": "Cross‑cutting outcomes; strong centre of excellence"},
            {"Context": "UK NHS (sensitive data)", "Lean": "Controlled access + incremental delivery", "Notes": "Stronger governance; human‑in‑the‑loop decisions"},
            {"Context": "Local government service redesign", "Lean": "Data‑informed + citizen‑focused", "Notes": "Openness where safe; service‑led iteration"}
        ])
        st.dataframe(examples, use_container_width=True)

        # --- FAQs
        st.markdown("""
### ❓ FAQs
**Is one side of a lens better?**  
No — positions reflect context and risk appetite. The goal is **conscious balance**.

**What if Current and Target are far apart?**  
That's good information: pick **3 shifts** to start; avoid Big‑Bang unless mandated.

**How do we decide left vs right?**  
Use the **Lenses explainer** in the **Lenses tab** — each lens includes when to lean left/right and a concrete example.
""")

        # --- Closing tip
        st.markdown("> *Treat strategy as a rhythm, not a document.* Review quarterly, learn, and adjust your lens positions.")
