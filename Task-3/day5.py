import pandas as pd


# Load Cleaned Dataset
df = pd.read_csv("Cleaned_Ecommerce_Sales.csv")


# Customer Sales Analysis

customer_analysis = df.groupby("Customer_Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order_ID", "count")
)


print("----- Customer Analysis -----")
print(customer_analysis)


# Top 10 Customers by Sales

top_customers = customer_analysis.sort_values(
    by="Total_Sales",
    ascending=False
).head(10)


print("\n----- Top 10 Customers -----")
print(top_customers)


# Product Performance Analysis

product_analysis = df.groupby("Product").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Quantity_Sold=("Quantity", "sum")
)


print("\n----- Product Analysis -----")
print(product_analysis)


# Top Products by Sales

top_products = product_analysis.sort_values(
    by="Total_Sales",
    ascending=False
).head(10)


print("\n----- Top 10 Products -----")
print(top_products)


# Category Performance

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
)


print("\n----- Category Analysis -----")
print(category_analysis)


# Customer Segmentation Based on Sales

def customer_segment(sales):

    if sales >= 30000:
        return "High Value Customer"

    elif sales >= 10000:
        return "Medium Value Customer"

    else:
        return "Low Value Customer"


customer_analysis["Customer_Segment"] = customer_analysis["Total_Sales"].apply(
    customer_segment
)


print("\n----- Customer Segmentation -----")
print(customer_analysis)


# Segment Count

segment_count = customer_analysis["Customer_Segment"].value_counts()

print("\n----- Customer Segment Count -----")
print(segment_count)


# Save Customer Analysis File

customer_analysis.to_csv(
    "Customer_Analysis.csv"
)


print("\nDeep Dive Analysis Completed Successfully!")