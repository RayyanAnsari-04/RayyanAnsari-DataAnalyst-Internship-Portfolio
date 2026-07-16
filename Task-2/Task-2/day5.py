import pandas as pd

df = pd.read_csv("dataset/student_performance.csv")

print("========== DATASET SUMMARY ==========")

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nAverage Attendance:")
print(df["Attendance"].mean())

print("\nAverage Study Hours:")
print(df["StudyHours"].mean())

print("\nPlacement Status Count:")
print(df["PlacementStatus"].value_counts())

print("\nDepartment Count:")
print(df["Department"].value_counts())

print("\nGender Count:")
print(df["Gender"].value_counts())