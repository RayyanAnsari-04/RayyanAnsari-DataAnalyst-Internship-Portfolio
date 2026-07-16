# DAY 7 Project Documentation & Final Project Organization
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# 1. Dataset Preview

print("DATASET PREVIEW:")
print(df.head())

# 2. Final Dataset Information

print("\nDATASET INFO:")
print(df.info())

# 3. Final Statistics

print("\nFINAL STATISTICS:")
print(df.describe())

# 4. Final Value Counts

print("\nTOP VALUES:")
print(df[df.columns[0]].value_counts().head())

# 5. Confirmation Message

print("\nPROJECT DOCUMENTATION READY ✔")