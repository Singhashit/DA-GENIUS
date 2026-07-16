import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="DA GENIUS",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Load CSS ----------
css_file = Path("assets/css/style.css")

if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text()}</style>",
        unsafe_allow_html=True
    )

# ---------- Sidebar ----------
with st.sidebar:

    st.title("📊 DA GENIUS")

    st.markdown("---")

    st.success("AI Powered Data Analyst")

    st.markdown("""
### Navigation

🏠 Home

📂 Upload Dataset

📊 Dashboard

🤖 AI Insights

📄 Reports

⚙ Settings
""")

# ---------- Hero ----------

st.markdown(
"""
<div class='title'>
🚀 DA GENIUS
</div>

<div class='subtitle'>
AI Powered Business & Data Analyst Platform
</div>
""",
unsafe_allow_html=True
)

st.write("")

st.info(
"""
Upload any dataset and automatically generate:

• Interactive Dashboards

• Business Insights

• Data Cleaning

• KPI Analysis

• Forecasting

• Executive Reports
"""
)

st.write("")

# ---------- Feature Cards ----------

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
<div class="card">

### 📂 Upload

Upload CSV & Excel datasets.

</div>
""",unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">

### 📊 Dashboard

Automatic KPI Dashboard.

</div>
""",unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="card">

### 🤖 AI Insights

AI Generated Business Recommendations.

</div>
""",unsafe_allow_html=True)

st.write("")

st.divider()

st.subheader("Tech Stack")

c1,c2,c3,c4,c5=st.columns(5)

c1.metric("Python","🐍")
c2.metric("SQL","🗄")
c3.metric("Power BI","📊")
c4.metric("Machine Learning","🤖")
c5.metric("Streamlit","⚡")

st.divider()

st.success("Sprint 1 ✅ Landing Page Completed")