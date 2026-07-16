# DAY 3 Exploratory Data Analysis (EDA) & Data Insights
# EDA 
import pandas as pd

# Load dataset (cleaned or raw)
df = pd.read_csv("cleaned_data.csv")  # or "data.csv" if not cleaned

# 1. Basic statistics
print("BASIC STATISTICS:")
print(df.describe())

# 2. Column info
print("\nCOLUMNS:")
print(df.columns)

# 3. Value counts (pattern check)
print("\nVALUE COUNTS (first column):")
print(df[df.columns[0]].value_counts())

# 4. Top categories
print("\nTOP VALUES:")
print(df[df.columns[0]].value_counts().head())

# CHART

import matplotlib.pyplot as plt

df[df.columns[0]].value_counts().plot(kind='bar')

plt.title("Value Counts Chart")
plt.xlabel("Categories")
plt.ylabel("Count")

plt.savefig("chart.png") 
plt.show()                