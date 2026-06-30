import pandas as pd
import os


def analyze_data():
    print("Starting data analysis...")

    input_path = "data/processed/cleaned_sales_data.csv"
    output_path = "reports/kpi_summary.csv"

    if not os.path.exists(input_path):
        print("Error: cleaned_sales_data.csv not found")
        return None

    df = pd.read_csv(input_path)

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()
    total_customers = df["Customer_ID"].nunique()
    average_sales = df["Sales"].mean()
    average_profit = df["Profit"].mean()

    best_category = df.groupby("Category")["Sales"].sum().idxmax()
    best_region = df.groupby("Region")["Sales"].sum().idxmax()
    best_product = df.groupby("Product_Name")["Sales"].sum().idxmax()
    best_salesperson = df.groupby("Salesperson")["Sales"].sum().idxmax()

    kpi_data = {
        "Metric": [
            "Total Sales",
            "Total Profit",
            "Total Orders",
            "Total Customers",
            "Average Sales",
            "Average Profit",
            "Best Category",
            "Best Region",
            "Best Product",
            "Best Salesperson"
        ],
        "Value": [
            round(total_sales, 2),
            round(total_profit, 2),
            total_orders,
            total_customers,
            round(average_sales, 2),
            round(average_profit, 2),
            best_category,
            best_region,
            best_product,
            best_salesperson
        ]
    }

    kpi_df = pd.DataFrame(kpi_data)

    os.makedirs("reports", exist_ok=True)
    kpi_df.to_csv(output_path, index=False)

    print("Data analysis completed")
    print("KPI summary saved at:", output_path)

    return kpi_df