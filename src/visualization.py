import pandas as pd
import matplotlib.pyplot as plt
import os


def create_charts():
    print("Starting chart generation...")

    input_path = "data/processed/cleaned_sales_data.csv"

    if not os.path.exists(input_path):
        print("Error: cleaned_sales_data.csv not found")
        return

    df = pd.read_csv(input_path)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    os.makedirs("charts", exist_ok=True)

    monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()
    monthly_sales.index = monthly_sales.index.astype(str)

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("charts/monthly_sales_trend.png")
    plt.close()

    category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    category_sales.plot(kind="bar")
    plt.title("Category-wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("charts/category_sales.png")
    plt.close()

    region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    region_profit.plot(kind="bar")
    plt.title("Region-wise Profit")
    plt.xlabel("Region")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig("charts/region_profit.png")
    plt.close()

    payment_mode = df["Payment_Mode"].value_counts()

    plt.figure(figsize=(8, 5))
    payment_mode.plot(kind="bar")
    plt.title("Payment Mode Distribution")
    plt.xlabel("Payment Mode")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("charts/payment_mode.png")
    plt.close()

    delivery_status = df["Delivery_Status"].value_counts()

    plt.figure(figsize=(8, 5))
    delivery_status.plot(kind="bar")
    plt.title("Delivery Status Distribution")
    plt.xlabel("Delivery Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("charts/delivery_status.png")
    plt.close()

    print("Charts generated successfully")