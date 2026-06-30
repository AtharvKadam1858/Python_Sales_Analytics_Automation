import pandas as pd
import os


def clean_data():
    print("Starting data cleaning...")

    input_path = "data/raw/sales_data.xlsx"
    output_path = "data/processed/cleaned_sales_data.csv"

    if not os.path.exists(input_path):
        print("Error: sales_data.xlsx not found in data/raw folder")
        return None

    df = pd.read_excel(input_path)

    print("Raw Excel data loaded successfully")
    print("Rows before cleaning:", df.shape[0])
    print("Columns:", df.shape[1])

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].median())
    df["Payment_Mode"] = df["Payment_Mode"].fillna("Unknown")
    df["Delivery_Status"] = df["Delivery_Status"].fillna("Unknown")

    numeric_columns = [
        "Quantity",
        "Unit_Price",
        "Discount",
        "Sales",
        "Cost",
        "Profit",
        "Age"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(0)

    df = df[df["Sales"] > 0]
    df = df[df["Quantity"] > 0]

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(output_path, index=False)

    print("Data cleaning completed")
    print("Rows after cleaning:", df.shape[0])
    print("Cleaned file saved at:", output_path)

    return df


if __name__ == "__main__":
    clean_data()