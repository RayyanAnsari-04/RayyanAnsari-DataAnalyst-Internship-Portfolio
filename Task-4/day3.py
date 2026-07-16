# ==========================================
# TASK 4
# Day 3 - Exploratory Data Analysis (EDA)
# ==========================================

import pandas as pd

# Load Cleaned Dataset
df = pd.read_excel("Cleaned_Ecommerce_Sales.xlsx")

# ------------------------------------------
# Total Sales
# ------------------------------------------

total_sales = df["Sales"].sum()
print("\n========== TOTAL SALES ==========")
print(total_sales)

# ------------------------------------------
# Total Profit
# ------------------------------------------

total_profit = df["Profit"].sum()
print("\n========== TOTAL PROFIT ==========")
print(total_profit)

# ------------------------------------------
# Total Quantity Sold
# ------------------------------------------

total_quantity = df["Quantity"].sum()
print("\n========== TOTAL QUANTITY SOLD ==========")
print(total_quantity)

# ------------------------------------------
# Sales by Category
# ------------------------------------------

print("\n========== SALES BY CATEGORY ==========")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(category_sales)

# ------------------------------------------
# Sales by Region
# ------------------------------------------

print("\n========== SALES BY REGION ==========")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(region_sales)

# ------------------------------------------
# Top 5 Customers
# ------------------------------------------

print("\n========== TOP 5 CUSTOMERS ==========")

top_customers = df.groupby("Customer_Name")["Sales"].sum().sort_values(ascending=False).head(5)
print(top_customers)

# ------------------------------------------
# Top 5 Products
# ------------------------------------------

print("\n========== TOP 5 PRODUCTS ==========")

top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
print(top_products)