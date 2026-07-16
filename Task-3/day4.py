import pandas as pd
# Load Cleaned Dataset
df = pd.read_csv("Cleaned_Ecommerce_Sales.csv")


# Total Sales
total_sales = df["Sales"].sum()

print("----- Total Sales -----")
print(total_sales)


# Total Profit
total_profit = df["Profit"].sum()

print("\n----- Total Profit -----")
print(total_profit)


# Total Orders
total_orders = df["Order_ID"].nunique()

print("\n----- Total Orders -----")
print(total_orders)


# Total Customers
total_customers = df["Customer_ID"].nunique()

print("\n----- Total Customers -----")
print(total_customers)


# Average Order Value
average_order_value = total_sales / total_orders

print("\n----- Average Order Value -----")
print(average_order_value)


# Profit Margin
profit_margin = (total_profit / total_sales) * 100

print("\n----- Profit Margin (%) -----")
print(profit_margin)


# Category Performance
category_performance = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\n----- Category Performance -----")
print(category_performance)


# Region Performance
region_performance = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\n----- Region Performance -----")
print(region_performance)


print("\nKPI Analysis Completed Successfully!")