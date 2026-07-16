import streamlit as st
import pandas as pd

from core.dashboard import Dashboard
from core.visualization import Charts

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Automatic Dashboard")

# -------------------------------
# Load Dataset
# -------------------------------

if "cleaned_dataset" in st.session_state:

    df = st.session_state["cleaned_dataset"]

elif "dataset" in st.session_state:

    df = st.session_state["dataset"]

else:

    st.warning("Please upload a dataset first.")

    st.stop()

# -------------------------------
# Detect Columns
# -------------------------------

detect = Dashboard.detect_columns(df)

sales = detect["sales"]
profit = detect["profit"]
date = detect["date"]
customer = detect["customer"]
product = detect["product"]
region = detect["region"]
category = detect["category"]

# -------------------------------
# KPI Cards
# -------------------------------

st.header("📌 Key Performance Indicators")

Charts.kpi_cards(
    Dashboard.generate_kpis(df)
)

st.divider()

# -------------------------------
# Dataset Summary
# -------------------------------

st.header("Dataset Summary")

summary = Dashboard.dataset_summary(df)

st.dataframe(
    pd.DataFrame(summary.items(), columns=["Metric", "Value"]),
    use_container_width=True
)

st.divider()

# -------------------------------
# Monthly Trend
# -------------------------------

if date and sales:

    st.header("📈 Monthly Sales Trend")

    Charts.monthly_trend(
        df,
        date,
        sales
    )

# -------------------------------
# Revenue by Region
# -------------------------------

if region and sales:

    st.divider()

    st.header("🌍 Revenue by Region")

    temp = (
        df.groupby(region)[sales]
        .sum()
        .reset_index()
        .sort_values(sales, ascending=False)
    )

    Charts.bar(
        temp,
        region,
        sales,
        "Revenue by Region"
    )

# -------------------------------
# Profit by Category
# -------------------------------

if category and profit:

    st.divider()

    st.header("💰 Profit by Category")

    temp = (
        df.groupby(category)[profit]
        .sum()
        .reset_index()
        .sort_values(profit, ascending=False)
    )

    Charts.bar(
        temp,
        category,
        profit,
        "Profit by Category"
    )

# -------------------------------
# Top Products
# -------------------------------

if product:

    st.divider()

    st.header("🏆 Top Products")

    Charts.top_categories(
        df,
        product
    )

# -------------------------------
# Top Customers
# -------------------------------

if customer:

    st.divider()

    st.header("👥 Top Customers")

    Charts.top_categories(
        df,
        customer
    )

# -------------------------------
# Correlation
# -------------------------------

st.divider()

st.header("Correlation Matrix")

Charts.heatmap(df)

# -------------------------------
# Histogram
# -------------------------------

numeric = Dashboard.numeric(df)

if len(numeric) > 0:

    st.divider()

    st.header("Distribution")

    col = st.selectbox(
        "Select Numeric Column",
        numeric
    )

    Charts.histogram(
        df,
        col
    )

# -------------------------------
# Boxplot
# -------------------------------

if len(numeric) > 0:

    st.divider()

    st.header("Outlier Detection")

    col = st.selectbox(
        "Select Column",
        numeric,
        key="box"
    )

    Charts.box(
        df,
        col
    )

# -------------------------------
# Scatter
# -------------------------------

if len(numeric) >= 2:

    st.divider()

    st.header("Scatter Analysis")

    c1, c2 = st.columns(2)

    x = c1.selectbox(
        "X Axis",
        numeric,
        key="x"
    )

    y = c2.selectbox(
        "Y Axis",
        numeric,
        index=1,
        key="y"
    )

    Charts.scatter(
        df,
        x,
        y
    )

# -------------------------------
# Pie Chart
# -------------------------------

cats = Dashboard.categorical(df)

if len(cats):

    st.divider()

    st.header("Category Distribution")

    col = st.selectbox(
        "Category",
        cats,
        key="pie"
    )

    Charts.pie(
        df,
        col
    )

# -------------------------------
# Recommended Charts
# -------------------------------

st.divider()

st.header("🤖 Recommended Dashboard Components")

for chart in Dashboard.recommendations(df):

    st.success(chart)