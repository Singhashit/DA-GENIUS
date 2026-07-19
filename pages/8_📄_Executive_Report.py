import streamlit as st

from core.dashboard import Dashboard
from core.insight_engine import InsightEngine
from core.report_generator import ReportGenerator

st.title("📄 Executive Report")

if "cleaned_dataset" in st.session_state:

    df = st.session_state["cleaned_dataset"]

elif "dataset" in st.session_state:

    df = st.session_state["dataset"]

else:

    st.warning("Upload Dataset First")

    st.stop()

summary = Dashboard.dataset_summary(df)

kpis = Dashboard.generate_kpis(df)

detected = Dashboard.detect_columns(df)

insights = InsightEngine.generate(df, detected)

recommendations = InsightEngine.recommendations(detected)

st.subheader("Preview")

st.json(summary)

st.json(kpis)

for i in insights:
    st.success(i)

for r in recommendations:
    st.info(r)

if st.button("Generate Executive Report", use_container_width=True):

    file = ReportGenerator.generate(

        "Executive_Report.pdf",

        summary,

        kpis,

        insights,

        recommendations

    )

    with open(file, "rb") as f:

        st.download_button(

            "⬇ Download Executive Report",

            f,

            file_name="Executive_Report.pdf",

            mime="application/pdf",

            use_container_width=True

        )

    st.success("Executive Report Generated Successfully!")