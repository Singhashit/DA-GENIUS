import streamlit as st


def show_metrics():

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Datasets",
        "1,240",
        "+34"
    )

    c2.metric(
        "Dashboards",
        "327",
        "+21"
    )

    c3.metric(
        "AI Insights",
        "9,812",
        "+641"
    )

    c4.metric(
        "Forecast Accuracy",
        "96.7%",
        "0.8%"
    )