import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd


class Charts:

    @staticmethod
    def kpi_cards(kpis):

        cols = st.columns(len(kpis))

        for i, (key, value) in enumerate(kpis.items()):
            cols[i].metric(key, value)

    @staticmethod
    def line(df, x, y, title=None):

        fig = px.line(
            df,
            x=x,
            y=y,
            markers=True,
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def bar(df, x, y, title=None):

        fig = px.bar(
            df,
            x=x,
            y=y,
            color=y,
            text_auto=".2s",
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def horizontal_bar(df, x, y, title=None):

        fig = px.bar(
            df,
            x=x,
            y=y,
            orientation="h",
            color=x,
            text_auto=".2s",
            title=title
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def pie(df, names, values=None, title=None):

        if values is None:

            temp = (
                df[names]
                .value_counts()
                .head(10)
                .reset_index()
            )

            temp.columns = [names, "Count"]

            fig = px.pie(
                temp,
                names=names,
                values="Count",
                hole=0.45,
                title=title
            )

        else:

            fig = px.pie(
                df,
                names=names,
                values=values,
                hole=0.45,
                title=title
            )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def histogram(df, column):

        fig = px.histogram(
            df,
            x=column,
            nbins=40,
            marginal="box"
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def box(df, column):

        fig = px.box(
            df,
            y=column,
            points="outliers"
        )

        fig.update_layout(
            template="plotly_white",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def scatter(df, x, y, color=None):

        fig = px.scatter(
            df,
            x=x,
            y=y,
            color=color
        )

        fig.update_layout(
            template="plotly_white",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def heatmap(df):

        numeric = df.select_dtypes("number")

        if numeric.shape[1] < 2:
            st.info("Not enough numeric columns.")
            return

        corr = numeric.corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu_r"
        )

        fig.update_layout(
            template="plotly_white",
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def treemap(df, path, values):

        fig = px.treemap(
            df,
            path=path,
            values=values
        )

        fig.update_layout(
            margin=dict(t=40, l=0, r=0, b=0)
        )

        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def top_categories(df, column):

        temp = (
            df[column]
            .value_counts()
            .head(10)
            .reset_index()
        )

        temp.columns = [column, "Count"]

        Charts.horizontal_bar(
            temp,
            "Count",
            column,
            f"Top {column}"
        )

    @staticmethod
    def monthly_trend(df, date_col, value_col):

        temp = df.copy()

        temp[date_col] = pd.to_datetime(temp[date_col])

        temp["Month"] = temp[date_col].dt.to_period("M").astype(str)

        temp = (
            temp
            .groupby("Month")[value_col]
            .sum()
            .reset_index()
        )

        Charts.line(
            temp,
            "Month",
            value_col,
            "Monthly Trend"
        )