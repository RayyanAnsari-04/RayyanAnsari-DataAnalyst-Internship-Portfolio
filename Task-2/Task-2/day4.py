import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset/student_performance.csv")

# Gender Distribution
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(gender_count.index, gender_count.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.savefig("charts/gender_distribution.png")
plt.show()

# Department Distribution
dept_count = df["Department"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(dept_count.index, dept_count.values)
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.savefig("charts/department_distribution.png")
plt.show()

# Placement Status Distribution
placement_count = df["PlacementStatus"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(placement_count.index, placement_count.values)
plt.title("Placement Status Distribution")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")
plt.savefig("charts/placement_distribution.png")
plt.show()