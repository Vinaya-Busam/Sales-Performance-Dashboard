import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Performance Dashboard", 
    page_icon="📊",
    layout="wide")

st.title("Sales Performance Dashboard")
st.markdown("#### Analyze sales performance, profits, products, and business trends.")


# LOAD DATASET
df = pd.read_csv("Dataset/Sample - Superstore.csv", encoding='latin1')
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
st.markdown("---")

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")

monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

fig = px.line(monthly_sales, x="Month", y="Sales", title="Sales", markers=True)
st.plotly_chart(fig, use_container_width=True)


# Category Analysis
st.subheader("📦 Sales by Category")

category_sales = df.groupby('Category')['Sales'].sum().reset_index()
fig = px.bar(category_sales, x="Category", y="Sales", color="Category")

st.plotly_chart(fig, use_container_width=True)


# Sales by Region
st.subheader("🌍 Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
fig = px.pie(region_sales, names='Region', values='Sales', width=700, height=500)

st.plotly_chart(fig, use_container_width=True)


# Top 10 Products
st.subheader("🏆 Top 10 Products")

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

fig = px.bar(top_products, x='Sales', y='Product Name', color='Product Name', orientation='h', width=750, height=650)
st.plotly_chart(fig, use_container_width=True)


# Profit Analysis
st.subheader("💰 Profit by Category")

profit_category = df.groupby('Category')['Profit'].sum().reset_index()
fig = px.bar(profit_category, x='Category', y='Profit', color='Category')

st.plotly_chart(fig, use_container_width=True)


# Business Insights Section
st.subheader("📌 Business Insights")

best_category = df.groupby('Category')['Sales'].sum().idxmax()
best_region = df.groupby('Region')['Sales'].sum().idxmax()
most_profitable = df.groupby('Product Name')['Profit'].sum().idxmax()

st.success(
    f"""
    - #### Highest Sales Category: *{best_category}*
    - #### Best Performing Region: *{best_region}*
    - #### Most Profitable Product: *{most_profitable}*
    """
)