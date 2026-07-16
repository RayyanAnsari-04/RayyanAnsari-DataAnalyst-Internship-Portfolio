import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# SQL Server Connection

connection = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-B99NA699\\SQLEXPRESS;"
    "Database=StudentPerformanceDB;"
    "Trusted_Connection=yes;"
)


print("Database Connected Successfully")


# Load Data From SQL Server

query = "SELECT * FROM StudentPerformance"

df = pd.read_sql(query, connection)


print("\nDataset Loaded Successfully")
print(df.head())


# Create folder for charts

if not os.path.exists("charts"):
    os.makedirs("charts")


# -------------------------------
# 1. Marks Distribution
# -------------------------------

plt.figure(figsize=(8,5))

sns.histplot(df["Marks"], bins=10)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.savefig("charts/marks_distribution.png")

plt.show()


# -------------------------------
# 2. Department Wise Student Count
# -------------------------------

plt.figure(figsize=(8,5))

sns.countplot(
    x="Department",
    data=df
)

plt.title("Department Wise Student Count")
plt.xlabel("Department")
plt.ylabel("Students")

plt.savefig("charts/department_student_count.png")

plt.show()


# -------------------------------
# 3. Average Marks By Department
# -------------------------------

avg_marks = df.groupby("Department")["Marks"].mean().reset_index()


plt.figure(figsize=(8,5))

sns.barplot(
    x="Department",
    y="Marks",
    data=avg_marks
)

plt.title("Average Marks By Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.savefig("charts/average_marks_department.png")

plt.show()


# -------------------------------
# 4. Attendance vs Marks
# -------------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    x="Attendance",
    y="Marks",
    data=df
)

plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")

plt.savefig("charts/attendance_vs_marks.png")

plt.show()


# -------------------------------
# 5. Placement Status Analysis
# -------------------------------

plt.figure(figsize=(8,5))

df["PlacementStatus"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Placement Status Distribution")

plt.ylabel("")

plt.savefig("charts/placement_status.png")

plt.show()


# Close Connection

connection.close()


print("\nAll Charts Generated Successfully!")