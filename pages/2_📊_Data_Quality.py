import streamlit as st

from core.analyzer import DataAnalyzer

st.title("📊 Data Quality Analyzer")

if "dataset" not in st.session_state:

    st.warning("Upload dataset first.")

    st.stop()

df = st.session_state["dataset"]

summary = DataAnalyzer.dataset_summary(df)

score = DataAnalyzer.quality_score(df)

st.metric("Data Quality Score", f"{score}%")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", summary["Rows"])
col2.metric("Columns", summary["Columns"])
col3.metric("Missing", summary["Missing"])
col4.metric("Duplicates", summary["Duplicates"])

col1, col2, col3 = st.columns(3)

col1.metric("Numeric", summary["Numeric"])
col2.metric("Categorical", summary["Categorical"])
col3.metric("Memory", f'{summary["Memory"]} MB')

st.divider()

st.subheader("Missing Values")

st.dataframe(
    DataAnalyzer.missing_table(df),
    use_container_width=True
)

st.divider()

st.subheader("Column Information")

st.dataframe(
    DataAnalyzer.datatype_table(df),
    use_container_width=True
)

st.divider()

st.subheader("Recommendations")

for item in DataAnalyzer.recommendations(df):
    st.success(item)