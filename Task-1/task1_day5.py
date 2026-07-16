# DAY 5 Advanced Data Analysis & Insight Generation
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# 1. Dataset overview

print("DATASET SHAPE:")
print(df.shape)

# 2. GroupBy Analysis
print("\nGROUPBY ANALYSIS:")
print(df.groupby(df.columns[0]).size())

# 3. Sorting Data

print("\nSORTED DATA:")
print(df.sort_values(by=df.columns[0]).head())

# 4. Value Count

print("\nVALUE COUNTS:")
print(df[df.columns[0]].value_counts())

# 5. Correlation Analysis

print("\nCORRELATION:")
print(df.corr(numeric_only=True))

# 6. Insights Example

print("\nTOP CATEGORY:")
print(df[df.columns[0]].value_counts().head(1))