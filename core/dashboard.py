import pandas as pd
import numpy as np


class Dashboard:

    # -------------------------
    # Detect Important Columns
    # -------------------------

    @staticmethod
    def detect_columns(df):

        cols = {c.lower(): c for c in df.columns}

        detected = {}

        keywords = {

            "sales": [
                "sales",
                "sale",
                "revenue",
                "amount",
                "total",
                "income"
            ],

            "profit": [
                "profit",
                "margin",
                "earning"
            ],

            "date": [
                "date",
                "order date",
                "invoice date",
                "purchase date"
            ],

            "customer": [
                "customer",
                "client",
                "buyer"
            ],

            "product": [
                "product",
                "item",
                "product name"
            ],

            "region": [
                "region",
                "state",
                "city",
                "country"
            ],

            "category": [
                "category",
                "segment",
                "type"
            ]

        }

        for key in keywords:

            detected[key] = None

            for word in keywords[key]:

                for col in cols:

                    if word in col:

                        detected[key] = cols[col]

                        break

        return detected


    # -------------------------
    # KPI Engine
    # -------------------------

    @staticmethod
    def generate_kpis(df):

        detect = Dashboard.detect_columns(df)

        sales = detect["sales"]

        profit = detect["profit"]

        customer = detect["customer"]

        product = detect["product"]

        kpis = {}

        if sales:

            kpis["Revenue"] = round(df[sales].sum(),2)

        if profit:

            kpis["Profit"] = round(df[profit].sum(),2)

        if customer:

            kpis["Customers"] = df[customer].nunique()

        if product:

            kpis["Products"] = df[product].nunique()

        kpis["Rows"] = len(df)

        return kpis


    # -------------------------
    # Dataset Summary
    # -------------------------

    @staticmethod
    def dataset_summary(df):

        return {

            "Rows": df.shape[0],

            "Columns": df.shape[1],

            "Missing": int(df.isnull().sum().sum()),

            "Duplicates": int(df.duplicated().sum()),

            "Memory(MB)": round(
                df.memory_usage(deep=True).sum()/1024**2,
                2
            )

        }


    # -------------------------
    # Numeric Columns
    # -------------------------

    @staticmethod
    def numeric(df):

        return df.select_dtypes(
            include=np.number
        ).columns.tolist()


    # -------------------------
    # Category Columns
    # -------------------------

    @staticmethod
    def categorical(df):

        return df.select_dtypes(
            include="object"
        ).columns.tolist()


    # -------------------------
    # Date Columns
    # -------------------------

    @staticmethod
    def dates(df):

        dates=[]

        for col in df.columns:

            try:

                x=pd.to_datetime(df[col])

                if x.notna().sum()>len(df)*0.7:

                    dates.append(col)

            except:

                pass

        return dates


    # -------------------------
    # Dashboard Recommendation
    # -------------------------

    @staticmethod
    def recommendations(df):

        detect = Dashboard.detect_columns(df)

        charts=[]

        if detect["sales"]:

            charts.append("Revenue KPI")

        if detect["profit"]:

            charts.append("Profit KPI")

        if detect["date"]:

            charts.append("Monthly Trend")

        if detect["category"]:

            charts.append("Category Analysis")

        if detect["region"]:

            charts.append("Regional Analysis")

        if detect["customer"]:

            charts.append("Customer Analysis")

        if detect["product"]:

            charts.append("Top Products")

        if len(charts)==0:

            charts.extend([

                "Histogram",

                "Correlation",

                "Scatter Plot"

            ])

        return charts