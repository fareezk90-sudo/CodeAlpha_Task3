"""
CodeAlpha Internship - Task 3: Data Visualization
Dataset: Sample - Superstore.csv

Creates four charts and saves them in the outputs/ folder.
Run:
    python task3_visualization.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "Sample - Superstore.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load the dataset. latin1 works with the commonly used Superstore CSV file.
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_FILE}\n"
        "Place 'Sample - Superstore.csv' in the same folder as this script."
    )

df = pd.read_csv(DATA_FILE, encoding="latin1")

required_columns = ["Order Date", "Sales", "Profit", "Category", "Region"]
missing = [col for col in required_columns if col not in df.columns]
if missing:
    raise ValueError(
        f"Missing required columns: {missing}\n"
        f"Columns found: {list(df.columns)}"
    )

# Clean data types used in the charts.
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df = df.dropna(subset=["Order Date", "Sales", "Profit", "Category", "Region"])

if df.empty:
    raise ValueError("No usable rows remain after cleaning. Check the dataset.")

# 1. Total sales by product category.
sales_category = df.groupby("Category", as_index=False)["Sales"].sum()
sales_category = sales_category.sort_values("Sales", ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(sales_category["Category"], sales_category["Sales"])
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_sales_by_category.png", dpi=300)
plt.close()

# 2. Total profit by product category.
profit_category = df.groupby("Category", as_index=False)["Profit"].sum()
profit_category = profit_category.sort_values("Profit", ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(profit_category["Category"], profit_category["Profit"])
plt.title("Total Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_profit_by_category.png", dpi=300)
plt.close()

# 3. Monthly sales trend.
monthly_sales = (
    df.set_index("Order Date")
      .resample("MS")["Sales"]
      .sum()
      .reset_index()
)

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales["Order Date"], monthly_sales["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Order Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_monthly_sales_trend.png", dpi=300)
plt.close()

# 4. Total sales by region.
sales_region = df.groupby("Region", as_index=False)["Sales"].sum()
sales_region = sales_region.sort_values("Sales", ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(sales_region["Region"], sales_region["Sales"])
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_sales_by_region.png", dpi=300)
plt.close()

# Export summary tables to CSV for easy review.
sales_category.to_csv(OUTPUT_DIR / "sales_by_category.csv", index=False)
profit_category.to_csv(OUTPUT_DIR / "profit_by_category.csv", index=False)
monthly_sales.to_csv(OUTPUT_DIR / "monthly_sales.csv", index=False)
sales_region.to_csv(OUTPUT_DIR / "sales_by_region.csv", index=False)

# Print evidence and basic insights from the actual dataset.
print("TASK 3 COMPLETED SUCCESSFULLY")
print(f"Rows used: {len(df)}")
print(f"Date range: {df['Order Date'].min().date()} to {df['Order Date'].max().date()}")
print(f"Total sales: {df['Sales'].sum():,.2f}")
print(f"Total profit: {df['Profit'].sum():,.2f}")
print("\nSales by category:")
print(sales_category.to_string(index=False))
print("\nProfit by category:")
print(profit_category.to_string(index=False))
print("\nSales by region:")
print(sales_region.to_string(index=False))
print(f"\nCharts and summary CSV files saved in: {OUTPUT_DIR}")
