# ==========================================
# TASK 4
# Day 2 - Data Cleaning & Validation
# ==========================================

import pandas as pd

# Load Dataset
df = pd.read_excel("Ecommerce_Sales_Dataset_50_Rows.xlsx")

print("========== ORIGINAL DATASET ==========")
print(df.head())

# Check Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Check Duplicate Rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Convert Order_Date into Date Format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Verify Data Types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Dataset Shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Summary Statistics
print("\n========== SUMMARY ==========")
print(df.describe())

# Save Clean Dataset
df.to_excel("Cleaned_Ecommerce_Sales.xlsx", index=False)

print("\n✅ Cleaned dataset has been saved successfully!")