# ==========================================
# TASK 4
# Day 5 - Descriptive Statistics
# ==========================================

import pandas as pd

# Load Dataset
df = pd.read_excel("Cleaned_Ecommerce_Sales.xlsx")

# -------------------------------
# Mean
# -------------------------------

print("========== MEAN ==========")
print("Average Sales :", df["Sales"].mean())
print("Average Profit:", df["Profit"].mean())

# -------------------------------
# Median
# -------------------------------

print("\n========== MEDIAN ==========")
print("Median Sales :", df["Sales"].median())
print("Median Profit:", df["Profit"].median())

# -------------------------------
# Mode
# -------------------------------

print("\n========== MODE ==========")
print("Most Common Category:")
print(df["Category"].mode())

# -------------------------------
# Minimum & Maximum
# -------------------------------

print("\n========== MINIMUM & MAXIMUM ==========")
print("Minimum Sales :", df["Sales"].min())
print("Maximum Sales :", df["Sales"].max())

# -------------------------------
# Standard Deviation
# -------------------------------

print("\n========== STANDARD DEVIATION ==========")
print("Sales Std Dev :", df["Sales"].std())
print("Profit Std Dev:", df["Profit"].std())

# -------------------------------
# Variance
# -------------------------------

print("\n========== VARIANCE ==========")
print("Sales Variance :", df["Sales"].var())
print("Profit Variance:", df["Profit"].var())

# -------------------------------
# Complete Statistical Summary
# -------------------------------

print("\n========== COMPLETE SUMMARY ==========")
print(df[["Sales", "Profit", "Quantity"]].describe())

print("\n✅ Day 5 Statistical Analysis Completed Successfully!")