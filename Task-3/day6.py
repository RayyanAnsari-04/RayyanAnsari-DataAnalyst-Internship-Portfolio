# ============================================
# Task 3: Deep Dive Analysis & Dashboarding
# Day 6 - Advanced Analysis
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Cleaned Dataset

df = pd.read_csv("Cleaned_Ecommerce_Sales.csv")


# ============================================
# 1. Correlation Analysis
# ============================================

print("----- Correlation Analysis -----")

correlation = df[[
    "Unit_Price",
    "Quantity",
    "Sales",
    "Profit"
]].corr()

print(correlation)


# Heatmap

plt.figure(figsize=(8,5))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Between Numerical Features")

plt.show()


# ============================================
# 2. Sales and Profit Trend Analysis
# ============================================

sales_profit = df.groupby("Category").agg(
    Total_Sales=("Sales","sum"),
    Total_Profit=("Profit","sum")
)


print("\n----- Category Sales & Profit Analysis -----")
print(sales_profit)


# ============================================
# 3. Profit Margin Analysis
# ============================================

df["Profit_Margin"] = (
    df["Profit"] / df["Sales"]
) * 100


print("\n----- Profit Margin -----")

print(df[[
    "Product",
    "Sales",
    "Profit",
    "Profit_Margin"
]])


# ============================================
# 4. Highest Profit Products
# ============================================

profit_products = df.groupby("Product")["Profit"].sum()


top_profit_products = profit_products.sort_values(
    ascending=False
).head(10)


print("\n----- Top Profitable Products -----")

print(top_profit_products)


# ============================================
# 5. Region Performance Analysis
# ============================================

region_analysis = df.groupby("Region").agg(
    Sales=("Sales","sum"),
    Profit=("Profit","sum"),
    Orders=("Order_ID","count")
)


print("\n----- Region Performance -----")

print(region_analysis)


# ============================================
# 6. Generate Business Insights
# ============================================

print("\n----- Business Insights -----")

print("""
1. Identify categories generating maximum sales.
2. Identify regions contributing highest revenue.
3. Find products with highest profitability.
4. Analyze customer segments for targeted marketing.
5. Improve decisions using KPI and dashboard analysis.
""")


# Save Advanced Analysis

sales_profit.to_csv(
    "Category_Performance.csv"
)

region_analysis.to_csv(
    "Region_Performance.csv"
)


print("\nAdvanced Analysis Completed Successfully!")