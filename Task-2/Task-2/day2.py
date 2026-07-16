import pandas as pd

# Load Dataset
df = pd.read_csv("dataset/student_performance.csv")

print("DESCRIPTIVE STATISTICS")
print(df.describe())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nMedian Marks:")
print(df["Marks"].median())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nStandard Deviation of Marks:")
print(df["Marks"].std())