import streamlit as st

from core.dashboard import Dashboard
from core.insight_engine import InsightEngine

st.title("🤖 AI Business Insights")

if "cleaned_dataset" in st.session_state:

    df = st.session_state["cleaned_dataset"]

elif "dataset" in st.session_state:

    df = st.session_state["dataset"]

else:

    st.warning("Upload dataset first.")

    st.stop()

detected = Dashboard.detect_columns(df)

insights = InsightEngine.generate(df, detected)

st.subheader("Business Insights")

for item in insights:

    st.success(item)

st.divider()

st.subheader("Executive Summary")

st.code(

    InsightEngine.executive_summary(insights)

)

st.divider()

st.subheader("Recommendations")

for rec in InsightEngine.recommendations(detected):

    st.info(rec)