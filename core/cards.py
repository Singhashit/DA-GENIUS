import streamlit as st


def feature_cards():

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
### 📂 Dataset Upload

Upload CSV

Upload Excel

Preview Dataset

Auto Detect Columns
"""
        )

    with col2:
        st.success(
            """
### 📊 Dashboard

Automatic Charts

KPIs

Visualizations

Interactive Dashboard
"""
        )

    with col3:
        st.warning(
            """
### 🤖 AI Insights

Business Summary

Recommendations

Forecasting

Executive Reports
"""
        )