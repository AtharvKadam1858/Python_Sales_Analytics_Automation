import pandas as pd
import os


def generate_excel_report():
    print("Starting Excel report generation...")

    data_path = "data/processed/cleaned_sales_data.csv"
    kpi_path = "reports/kpi_summary.csv"
    output_path = "reports/Sales_Report.xlsx"

    df = pd.read_csv(data_path)
    kpi_df = pd.read_csv(kpi_path)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        kpi_df.to_excel(writer, sheet_name="KPI Summary", index=False)
        df.to_excel(writer, sheet_name="Cleaned Sales Data", index=False)

        category_sales = df.groupby("Category")["Sales"].sum().reset_index()
        region_profit = df.groupby("Region")["Profit"].sum().reset_index()
        product_sales = df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()

        category_sales.to_excel(writer, sheet_name="Category Sales", index=False)
        region_profit.to_excel(writer, sheet_name="Region Profit", index=False)
        product_sales.to_excel(writer, sheet_name="Top Products", index=False)

    print("Excel report generated successfully")
    print("Report saved at:", output_path)