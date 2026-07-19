import pandas as pd
import plotly.express as px
import streamlit as st

from prophet import Prophet


class ForecastEngine:

    @staticmethod
    def detect(df, detected):

        return detected.get("date"), detected.get("sales")

    @staticmethod
    def prepare(df, date_col, sales_col):

        temp = df[[date_col, sales_col]].copy()

        temp.columns = ["ds", "y"]

        temp["ds"] = pd.to_datetime(temp["ds"])

        temp = temp.groupby("ds")["y"].sum().reset_index()

        return temp

    @staticmethod
    def forecast(df, periods=90):

        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False
        )

        model.fit(df)

        future = model.make_future_dataframe(periods=periods)

        prediction = model.predict(future)

        return prediction

    @staticmethod
    def plot(prediction):

        fig = px.line(
            prediction,
            x="ds",
            y="yhat",
            title="Sales Forecast"
        )

        fig.add_scatter(
            x=prediction["ds"],
            y=prediction["yhat_upper"],
            mode="lines",
            name="Upper"
        )

        fig.add_scatter(
            x=prediction["ds"],
            y=prediction["yhat_lower"],
            mode="lines",
            name="Lower"
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def future_table(prediction):

        st.subheader("Forecast Table")

        st.dataframe(

            prediction[

                ["ds", "yhat", "yhat_lower", "yhat_upper"]

            ].tail(30),

            use_container_width=True

        )