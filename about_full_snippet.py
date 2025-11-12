
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
- **CDOs / Heads of Data** 
[ ] to set direction and align leadership.
[ ]to frame trade‑offs and agree priorities.
[ ] to translate strategy into delivery.
[ ] to track progress and course‑correct.
""")

        # --- How to use
        st.markdown("""
### 🛠️ How to use this tool
1) **Explore** the landscape of strategies (by year, country, org type) for context.  
2) **Set profiles**: use the **Ten Lenses** sliders to define **Current** and **Target** positions.  
3) **Compare** in the **Journey** tab to see directional gaps (left/right) and magnitudes.  
4) **Prioritise** the top shifts and convert them into actions (owners, timelines, measures).  
5) **Re‑assess regulary** — treat your strategy as **living thing**.
""")

with tab_about:
    st.subheader("About this Explorer")
    st.markdown("""
The **Public Sector Data Strategy Explorer** helps governments and public bodies understand **how data strategies differ** — in scope, ambition, and governance.  
It combines a searchable dataset of real strategies with a conceptual framework called **The Ten Lenses of Data Strategy**.
""")

    # --- Visual Overview of Lenses (dual-color bars)
    st.markdown("### 👁️ The Ten Lenses of Data Strategy — Visual Overview")

    lenses = [
        ("Abstraction Level", "Conceptual", "Logical / Physical"),
        ("Adaptability", "Living", "Fixed"),
        ("Ambition", "Essential", "Transformational"),
        ("Coverage", "Horizontal", "Use-case-based"),
        ("Governance Structure", "Ecosystem / Federated", "Centralised"),
        ("Orientation", "Technology-focused", "Value-focused"),
        ("Motivation", "Compliance-driven", "Innovation-driven"),
        ("Access Philosophy", "Data-democratised", "Controlled access"),
        ("Delivery Mode", "Incremental", "Big Bang"),
        ("Decision Model", "Data-informed", "Data-driven")
    ]

    import plotly.graph_objects as go
    fig = go.Figure()
    for i, (dim, left, right) in enumerate(lenses):
        fig.add_trace(go.Bar(
            x=[50, 50],
            y=[f"{i+1}. {dim}", f"{i+1}. {dim}"],
            orientation='h',
            marker_color=['#70A9FF', '#FFB8B8'],
            showlegend=False,
            hovertext=[left, right]
        ))
    fig.update_layout(
        barmode='stack',
        title="Trade-off Spectrum Across Ten Lenses",
        xaxis=dict(showticklabels=False, range=[0,100]),
        height=500,
        margin=dict(l=20,r=20,t=40,b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Detailed Table with Examples
    st.markdown("""
### 🔍 Explanation and Public-Sector Examples

| # | Lens | Description | Public-Sector Example |
|---|------|--------------|----------------------|
| **1** | **Abstraction Level** | **Conceptual** strategies define vision and principles; **Logical / Physical** specify architecture and governance. | A national “Data Vision 2030” is conceptual; a departmental “Data Architecture Blueprint” is logical/physical. |
| **2** | **Adaptability** | **Living** evolves with new tech and policy; **Fixed** provides a stable framework. | The UK’s AI White Paper is living; GDPR is fixed. |
| **3** | **Ambition** | **Essential** ensures foundations; **Transformational** drives innovation and automation. | NHS data governance reforms are essential; Estonia’s X-Road is transformational. |
| **4** | **Coverage** | **Horizontal** builds maturity across all functions; **Use-case-based** targets exemplar projects. | A cross-government maturity model vs a sector-specific pilot. |
| **5** | **Governance Structure** | **Ecosystem / Federated** encourages collaboration; **Centralised** ensures uniform control. | UK’s federated CDO network vs Singapore’s Smart Nation. |
| **6** | **Orientation** | **Technology-focused** emphasises platforms; **Value-focused** prioritises outcomes and citizens. | A cloud migration roadmap vs a policy-impact dashboard. |
| **7** | **Motivation** | **Compliance-driven** manages risk; **Innovation-driven** creates opportunity. | GDPR compliance vs data-sharing sandboxes. |
| **8** | **Access Philosophy** | **Democratised** broadens data access; **Controlled** enforces permissions. | Open data portals vs restricted health datasets. |
| **9** | **Delivery Mode** | **Incremental** iterates and tests; **Big Bang** transforms at once. | Local pilots vs national-scale reform. |
| **10** | **Decision Model** | **Data-informed** blends human judgment; **Data-driven** relies on analytics. | Evidence-based policymaking vs automated fraud detection. |
""")

    st.markdown("""
---
### 💡 How to Use This Dashboard
- **Explore tab:** Browse and compare published data strategies by organisation, country, and year.  
- **Strategy Types tab:** Reflect on your organisation’s balance across the Ten Lenses.  
- **About tab:** Learn the conceptual foundations and examples behind each dimension.  

> *“Every data strategy is a balancing act — between governance and growth, structure and experimentation, control and creativity.”*
""")
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
