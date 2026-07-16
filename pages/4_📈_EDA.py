import streamlit as st
from core.eda import EDA

st.title("📈 Exploratory Data Analysis")

if "cleaned_dataset" in st.session_state:

    df=st.session_state["cleaned_dataset"]

else:

    df=st.session_state["dataset"]

EDA.overview(df)

st.divider()

EDA.statistics(df)

st.divider()

EDA.correlation(df)

st.divider()

EDA.histogram(df)

st.divider()

EDA.boxplot(df)

st.divider()

EDA.scatter(df)

st.divider()

EDA.bar(df)

st.divider()

EDA.pie(df)