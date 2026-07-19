import streamlit as st

from core.dashboard import Dashboard
from core.forecasting import ForecastEngine

st.title("📈 Sales Forecast")

if "cleaned_dataset" in st.session_state:

    df = st.session_state["cleaned_dataset"]

elif "dataset" in st.session_state:

    df = st.session_state["dataset"]

else:

    st.warning("Upload Dataset First")

    st.stop()

detect = Dashboard.detect_columns(df)

date_col, sales_col = ForecastEngine.detect(df, detect)

if date_col is None or sales_col is None:

    st.error("Forecasting requires Date and Sales columns.")

    st.stop()

days = st.slider(

    "Forecast Days",

    30,

    365,

    90

)

data = ForecastEngine.prepare(

    df,

    date_col,

    sales_col

)

with st.spinner("Training Forecast Model..."):

    pred = ForecastEngine.forecast(

        data,

        periods=days

    )

ForecastEngine.plot(pred)

ForecastEngine.future_table(pred)

csv = pred.to_csv(index=False).encode()

st.download_button(

    "Download Forecast",

    csv,

    "forecast.csv",

    "text/csv",

    use_container_width=True

)