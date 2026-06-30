import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Sales Analytics Dashboard", page_icon="📊", layout="wide")

df = pd.read_csv("data/processed/cleaned_sales_data.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Sales Dashboard", "Customer Analysis", "Reports"]
)

st.sidebar.header("Filters")

region = st.sidebar.multiselect("Region", df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Category", df["Category"].unique(), default=df["Category"].unique())

filtered_df = df[(df["Region"].isin(region)) & (df["Category"].isin(category))]

if page == "Home":
    st.title("Python Sales Analytics Automation System")
    st.write("This project automates data cleaning, KPI analysis, Excel/PDF reporting, business insights, and dashboard visualization.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"₹{filtered_df['Sales'].sum():,.0f}")
    col2.metric("Total Profit", f"₹{filtered_df['Profit'].sum():,.0f}")
    col3.metric("Total Orders", filtered_df["Order_ID"].nunique())
    col4.metric("Total Customers", filtered_df["Customer_ID"].nunique())

elif page == "Sales Dashboard":
    st.title("📊 Sales Dashboard")

    monthly_sales = filtered_df.groupby(filtered_df["Order_Date"].dt.to_period("M"))["Sales"].sum().reset_index()
    monthly_sales["Order_Date"] = monthly_sales["Order_Date"].astype(str)

    st.plotly_chart(px.line(monthly_sales, x="Order_Date", y="Sales", markers=True, title="Monthly Sales Trend"), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()
        st.plotly_chart(px.bar(category_sales, x="Category", y="Sales", title="Category-wise Sales"), use_container_width=True)

    with col2:
        region_profit = filtered_df.groupby("Region")["Profit"].sum().reset_index()
        st.plotly_chart(px.bar(region_profit, x="Region", y="Profit", title="Region-wise Profit"), use_container_width=True)

elif page == "Customer Analysis":
    st.title("👥 Customer Analysis")

    gender_sales = filtered_df.groupby("Gender")["Sales"].sum().reset_index()
    st.plotly_chart(px.pie(gender_sales, names="Gender", values="Sales", title="Sales by Gender"), use_container_width=True)

    rating_count = filtered_df["Customer_Rating"].value_counts().reset_index()
    rating_count.columns = ["Rating", "Count"]
    st.plotly_chart(px.bar(rating_count, x="Rating", y="Count", title="Customer Rating Distribution"), use_container_width=True)

elif page == "Reports":
    st.title("📄 Reports & Downloads")

    st.subheader("Business Insights")

    if os.path.exists("reports/business_insights.txt"):
        with open("reports/business_insights.txt", "r", encoding="utf-8") as file:
            st.text(file.read())

    st.subheader("Download Files")

    if os.path.exists("reports/Sales_Report.xlsx"):
        with open("reports/Sales_Report.xlsx", "rb") as file:
            st.download_button("Download Excel Report", file, "Sales_Report.xlsx")

    if os.path.exists("reports/Sales_Report.pdf"):
        with open("reports/Sales_Report.pdf", "rb") as file:
            st.download_button("Download PDF Report", file, "Sales_Report.pdf")

    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Filtered Data", csv, "filtered_sales_data.csv")