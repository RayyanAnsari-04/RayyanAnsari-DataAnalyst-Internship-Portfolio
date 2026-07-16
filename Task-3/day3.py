import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Cleaned Dataset
df = pd.read_csv("Cleaned_Ecommerce_Sales.csv")


# Display Dataset
print("----- Dataset Preview -----")
print(df.head())


# Dataset Information
print("\n----- Dataset Information -----")
print(df.info())


# Statistical Summary
print("\n----- Statistical Summary -----")
print(df.describe())


# Category Wise Sales Analysis
category_sales = df.groupby("Category")["Sales"].sum()

print("\n----- Sales by Category -----")
print(category_sales)


# Region Wise Sales Analysis
region_sales = df.groupby("Region")["Sales"].sum()

print("\n----- Sales by Region -----")
print(region_sales)


# Product Wise Profit Analysis
product_profit = df.groupby("Product")["Profit"].sum()

print("\n----- Profit by Product -----")
print(product_profit)


# Customer Purchase Analysis
customer_sales = df.groupby("Customer_Name")["Sales"].sum()

print("\n----- Top Customers -----")
print(customer_sales.sort_values(ascending=False).head(10))


# ============================================
# Data Visualization
# ============================================


# Category Sales Bar Chart
plt.figure(figsize=(8,5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()


# Region Sales Bar Chart
plt.figure(figsize=(8,5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()


# Profit Distribution
plt.figure(figsize=(8,5))

sns.histplot(
    df["Profit"],
    bins=10
)

plt.title("Profit Distribution")
plt.xlabel("Profit")

plt.show()


# Sales vs Profit Relationship
plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit"
)

plt.title("Sales vs Profit")

plt.show()


print("\nEDA Analysis Completed Successfully!")