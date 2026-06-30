import pandas as pd
import os


def generate_business_insights():
    print("Starting business insights generation...")

    input_path = "data/processed/cleaned_sales_data.csv"
    output_path = "reports/business_insights.txt"

    df = pd.read_csv(input_path)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    highest_sales_month = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum().idxmax()
    best_category = df.groupby("Category")["Sales"].sum().idxmax()
    best_region = df.groupby("Region")["Profit"].sum().idxmax()
    best_product = df.groupby("Product_Name")["Sales"].sum().idxmax()
    most_used_payment = df["Payment_Mode"].value_counts().idxmax()
    avg_rating = round(df["Customer_Rating"].mean(), 2)

    insights = f"""
BUSINESS INSIGHTS REPORT

1. Highest sales were recorded in {highest_sales_month}.
2. The highest revenue category is {best_category}.
3. The most profitable region is {best_region}.
4. The top-selling product is {best_product}.
5. The most used payment mode is {most_used_payment}.
6. The average customer rating is {avg_rating} out of 5.

RECOMMENDATIONS

1. Focus more marketing efforts on the {best_category} category.
2. Improve business strategies in lower-performing regions.
3. Maintain sufficient stock of {best_product}.
4. Promote digital payment options like {most_used_payment}.
5. Improve delivery and customer service to increase ratings.
"""

    os.makedirs("reports", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(insights)

    print("Business insights generated successfully")
    print("Insights saved at:", output_path)