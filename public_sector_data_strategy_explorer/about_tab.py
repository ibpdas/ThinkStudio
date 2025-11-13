
---

## 8️⃣ `about_tab.py`

```python
# about_tab.py
import base64
import os
import streamlit as st


def render_about() -> None:
    st.subheader("About this Explorer")

    st.markdown(
        """
<div class="info-panel">
<strong>What this is:</strong> A design-inspired prototype that helps public bodies
<strong>design, communicate, and iterate</strong> their data strategy.
It adds a <strong>maturity baseline</strong> (six themes) so strategic choices are <em>anchored in readiness</em>,
then uses the <strong>Ten Lenses</strong> to make trade-offs explicit.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("### 🎯 Purpose")
    st.markdown(
        """
- Make **key tensions** explicit instead of implicit.  
- Compare **current vs target** profiles and turn gaps into **prioritised actions**.  
- Anchor ambition to **realistic maturity** to avoid overreach or under-delivery.
"""
    )

    st.markdown("### 👥 Who it's for")
    st.markdown(
        """
- **CDOs / Heads of Data** — set direction and align leadership  
- **Policy & Operations leaders** — frame trade-offs and agree priorities  
- **Analysts & Data teams** — translate strategy into delivery  
- **PMOs / Transformation** — track progress and course-correct
"""
    )

    st.markdown("### 🧱 Maturity (6 themes) — aligned to the government framework")
    st.markdown(
        """
This tool reuses the six themes from the **Data Maturity Assessment for Government** framework
(Central Digital and Data Office).

| Theme | What it covers |
|---|---|
| **Uses** | How you get value from data – making decisions, evidencing impact, improving services. |
| **Data** | Technical aspects of data management as an asset – collection, quality, catalogues, interoperability. |
| **Leadership** | How senior and business leaders engage with data – strategy, responsibility, oversight, investment. |
| **Culture** | Attitudes to data across the organisation – awareness, openness, security, responsibility. |
| **Tools** | Systems and tools for storing, sharing and using data. |
| **Skills** | Data and analytical literacy across the organisation, and how people develop those skills. |
"""
    )
    st.markdown(
        """
**Maturity levels (1–5)** follow the same naming as the framework:
**Beginning, Emerging, Learning, Developing, Mastering**.
"""
    )
    st.markdown(
        "[Read the Data Maturity Assessment for Government framework]"
        "(https://www.gov.uk/government/publications/data-maturity-assessment-for-government-framework/"
        "data-maturity-assessment-for-government-framework-html)"
    )

    st.markdown("### 🔍 The Ten Lenses of Data Strategy")
    st.markdown(
        """
| # | Lens | Left ↔ Right |
|---|------|--------------|
| 1 | **Abstraction Level** | Conceptual ↔ Logical/Physical |
| 2 | **Adaptability** | Living ↔ Fixed |
| 3 | **Ambition** | Essential ↔ Transformational |
| 4 | **Coverage** | Horizontal ↔ Use-case-based |
| 5 | **Governance Structure** | Ecosystem/Federated ↔ Centralised |
| 6 | **Orientation** | Technology-focused ↔ Value-focused |
| 7 | **Motivation** | Compliance-driven ↔ Innovation-driven |
| 8 | **Access Philosophy** | Data-democratised ↔ Controlled access |
| 9 | **Delivery Mode** | Incremental ↔ Big Bang |
| 10 | **Decision Model** | Data-informed ↔ Data-driven |
"""
    )

    st.markdown(
        """
**How it works together:**  
🧱 *Maturity foundation* → 🎯 *Strategic tensions* → 🧭 *Journey plan*.  
Readiness first, direction second — then prioritise and deliver.
"""
    )

    st.markdown("### 📘 User Guide (PDF)")
    pdf_name = "Data_Strategy_Explorer_User_Guide.pdf"
    if os.path.exists(pdf_name):
        with open(pdf_name, "rb") as f:
            pdf_bytes = f.read()
        b64 = base64.b64encode(pdf_bytes).decode()
        href = (
            f'<a href="data:application/pdf;base64,{b64}" '
            f'download="{pdf_name}">⬇️ Click here to download the User Guide (PDF)</a>'
        )
        st.markdown(href, unsafe_allow_html=True)

        st.markdown("#### Preview")
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="600"></iframe>',
            unsafe_allow_html=True,
        )
    else:
        st.info(
            f"Place **{pdf_name}** in the same folder as this app to enable download and inline preview."
        )

    st.markdown(
        """
---
<div class="footer">
This is a design-inspired prototype for learning and exploration. It is not an official service.
</div>
""",
        unsafe_allow_html=True,
    )
