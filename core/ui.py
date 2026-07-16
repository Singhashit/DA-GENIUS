import streamlit as st


def hero():

    st.title("🚀 DA GENIUS")

    st.subheader(
        "AI Analytics Copilot for Data Analysts & Business Analysts"
    )

    st.write(
        """
Upload any CSV or Excel dataset and instantly generate:

- Interactive Dashboards
- KPI Analysis
- AI Business Insights
- Executive Reports
- Forecasting
"""
    )

    st.button(
        "📂 Upload Dataset",
        use_container_width=True,
    )