import streamlit as st
from core.cleaner import DataCleaner

st.title("🧹 Smart Data Cleaning")

if "dataset" not in st.session_state:

    st.warning("Upload dataset first.")

    st.stop()

df = st.session_state["dataset"]

st.info("Original Dataset")

st.dataframe(df.head())

col1, col2 = st.columns(2)

with col1:

    if st.button("🧹 Clean Dataset", use_container_width=True):

        cleaned = DataCleaner.clean(df)

        st.session_state["cleaned_dataset"] = cleaned

        st.success("Dataset cleaned successfully!")

with col2:

    if st.button("↩ Restore Original", use_container_width=True):

        st.session_state["cleaned_dataset"] = df

if "cleaned_dataset" in st.session_state:

    cleaned = st.session_state["cleaned_dataset"]

    st.divider()

    st.subheader("Cleaned Dataset")

    st.dataframe(cleaned)

    csv = cleaned.to_csv(index=False).encode()

    st.download_button(
        "⬇ Download Clean Dataset",
        csv,
        "cleaned_dataset.csv",
        "text/csv",
        use_container_width=True
    )