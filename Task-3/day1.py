# Import required library
import pandas as pd


# Load Dataset
df = pd.read_csv("Ecommerce_Sales_Task3_Dataset.csv")


# Display first 5 records
print("----- First 5 Rows of Dataset -----")
print(df.head())


# Check number of rows and columns
print("\n----- Dataset Shape -----")
print(df.shape)


# Display column names
print("\n----- Column Names -----")
print(df.columns)


# Display dataset information
print("\n----- Dataset Information -----")
print(df.info())


# Check missing values
print("\n----- Missing Values -----")
print(df.isnull().sum())


# Statistical summary
print("\n----- Statistical Summary -----")
print(df.describe())


# Display unique categories
print("\n----- Product Categories -----")
print(df["Category"].unique())


# Display unique regions
print("\n----- Regions -----")
print(df["Region"].unique())


# Total number of customers
total_customers = df["Customer_ID"].nunique()

print("\n----- Total Customers -----")
print(total_customers)


# Total sales
total_sales = df["Sales"].sum()

print("\n----- Total Sales -----")
print(total_sales)


# Total profit
total_profit = df["Profit"].sum()

print("\n----- Total Profit -----")
print(total_profit)