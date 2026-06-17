import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Performance Dashboard", 
    page_icon="📊",
    layout="wide")

st.title("Sales Performance Dashboard")
st.markdown("Analyze sales performance, profits, products, and business trends.")


# LOAD DATASET
df = pd.read_csv("Dataset/Sample - Superstore Sales.csv", encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df["Order Date"].dt.strftime("%Y-%m")


# KPI Cards
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = total_sales / total_orders

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Average Order Value", f"${avg_order_value:,.2f}")


# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

fig = px.line(monthly_sales, x="Month", y="Sales", title="Sales", markers=True)
st.plotly_chart(fig, use_container_width=True)