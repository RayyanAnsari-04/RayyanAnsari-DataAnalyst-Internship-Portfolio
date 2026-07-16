# ============================================
# Task 3: Deep Dive Analysis & Dashboarding
# Day 2 - Data Cleaning
# ============================================

import pandas as pd


# Load Dataset
df = pd.read_csv("Ecommerce_Sales_Task3_Dataset.csv")


# Display Original Dataset
print("----- Original Dataset -----")
print(df.head())


# Check Dataset Information
print("\n----- Dataset Information -----")
print(df.info())


# Check Missing Values
print("\n----- Missing Values -----")
print(df.isnull().sum())


# Check Duplicate Rows
print("\n----- Duplicate Rows -----")
print(df.duplicated().sum())


# Remove Duplicate Rows
df = df.drop_duplicates()


# Check Data Types
print("\n----- Data Types -----")
print(df.dtypes)


# Check Unique Values in Categorical Columns
print("\n----- Categories -----")
print(df["Category"].unique())

print("\n----- Regions -----")
print(df["Region"].unique())


# Convert Data Types (if required)
df["Unit_Price"] = df["Unit_Price"].astype(float)
df["Sales"] = df["Sales"].astype(float)
df["Profit"] = df["Profit"].astype(float)


# Final Dataset Check
print("\n----- Cleaned Dataset Information -----")
print(df.info())


# Save Cleaned Dataset
df.to_csv("Cleaned_Ecommerce_Sales.csv", index=False)


print("\nCleaned dataset saved successfully!")