# DAY 6 Data Reporting & Final Insights Preparation
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# 1. Final Dataset Summary

print("FINAL DATASET SUMMARY:")
print(df.describe())

# 2. Final Dataset Shape

print("\nFINAL SHAPE:")
print(df.shape)

# 3. Column Names

print("\nCOLUMNS:")
print(df.columns)

# 4. Top Categories / Values

print("\nTOP VALUES:")
print(df[df.columns[0]].value_counts().head())

# 5. Correlation Summary

print("\nCORRELATION:")
print(df.corr(numeric_only=True))

# 6. Final Insight Example

print("\nFINAL INSIGHT:")
print("Dataset cleaned and analyzed successfully.")