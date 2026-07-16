# ==========================================
# TASK 4
# Day 1 - Dataset Understanding & Exploration
# ==========================================

# Import Library
import pandas as pd

# Load Dataset
df = pd.read_excel("Ecommerce_Sales_Dataset_50_Rows.xlsx")

# Display First 5 Records
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

# Display Last 5 Records
print("\n========== LAST 5 ROWS ==========")
print(df.tail())

# Dataset Shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Column Names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# Dataset Information
print("\n========== DATASET INFORMATION ==========")
df.info()

# Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Duplicate Rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Data Types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Descriptive Statistics
print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

# Unique Values in Important Columns
print("\n========== UNIQUE CATEGORIES ==========")
print(df["Category"].unique())

print("\n========== UNIQUE REGIONS ==========")
print(df["Region"].unique())

print("\n========== PAYMENT METHODS ==========")
print(df["Payment_Method"].unique())