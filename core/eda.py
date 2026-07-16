import pandas as pd
import plotly.express as px
import streamlit as st


class EDA:

    @staticmethod
    def overview(df):

        c1,c2,c3,c4=st.columns(4)

        c1.metric("Rows",df.shape[0])
        c2.metric("Columns",df.shape[1])
        c3.metric("Missing",df.isnull().sum().sum())
        c4.metric("Duplicate",df.duplicated().sum())

    @staticmethod
    def statistics(df):

        st.subheader("Dataset Statistics")
        st.dataframe(df.describe(include="all").fillna(""))

    @staticmethod
    def correlation(df):

        numeric=df.select_dtypes(include="number")

        if numeric.shape[1]<2:
            return

        corr=numeric.corr()

        fig=px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            title="Correlation Heatmap"
        )

        st.plotly_chart(fig,use_container_width=True)

    @staticmethod
    def histogram(df):

        numeric=df.select_dtypes(include="number").columns

        if len(numeric)==0:
            return

        col=st.selectbox("Histogram Column",numeric)

        fig=px.histogram(df,x=col)

        st.plotly_chart(fig,use_container_width=True)

    @staticmethod
    def boxplot(df):

        numeric=df.select_dtypes(include="number").columns

        if len(numeric)==0:
            return

        col=st.selectbox("Boxplot Column",numeric,key="box")

        fig=px.box(df,y=col)

        st.plotly_chart(fig,use_container_width=True)

    @staticmethod
    def scatter(df):

        numeric=df.select_dtypes(include="number").columns

        if len(numeric)<2:
            return

        c1,c2=st.columns(2)

        x=c1.selectbox("X",numeric,key="x")

        y=c2.selectbox("Y",numeric,key="y")

        fig=px.scatter(df,x=x,y=y)

        st.plotly_chart(fig,use_container_width=True)

    @staticmethod
    def bar(df):

        cat=df.select_dtypes(include="object").columns

        if len(cat)==0:
            return

        col=st.selectbox("Category",cat)

        fig=px.bar(
            df[col].value_counts().head(10)
            .reset_index(),
            x="count",
            y=col,
            orientation="h"
        )

        st.plotly_chart(fig,use_container_width=True)

    @staticmethod
    def pie(df):

        cat=df.select_dtypes(include="object").columns

        if len(cat)==0:
            return

        col=st.selectbox("Pie Column",cat,key="pie")

        fig=px.pie(
            values=df[col].value_counts().head(10).values,
            names=df[col].value_counts().head(10).index
        )

        st.plotly_chart(fig,use_container_width=True)