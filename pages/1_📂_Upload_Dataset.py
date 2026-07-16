import streamlit as st
import pandas as pd

from core.loader import DataLoader

st.title("📂 Dataset Upload")

st.write("Upload a CSV or Excel dataset to begin analysis.")

uploaded_file = st.file_uploader(
    "Choose Dataset",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file:

    df = DataLoader.load_file(uploaded_file)

    if df is not None:

        st.session_state["dataset"] = df

        st.success("Dataset Loaded Successfully!")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))
        col4.metric("Duplicate Rows", int(df.duplicated().sum()))

        st.divider()

        st.subheader("Dataset Preview")

        st.dataframe(df, use_container_width=True)

        st.divider()

        st.subheader("Column Information")

        info = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(info, use_container_width=True)

        st.divider()

        st.subheader("Statistical Summary")

        st.dataframe(df.describe(include="all").fillna(""))