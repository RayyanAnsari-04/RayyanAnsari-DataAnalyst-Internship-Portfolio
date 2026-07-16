import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset/student_performance.csv")

# Histogram 1 - Marks
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=10)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("charts/marks_histogram.png")
plt.show()

# Histogram 2 - Attendance
plt.figure(figsize=(8,5))
plt.hist(df["Attendance"], bins=10)
plt.title("Distribution of Attendance")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.savefig("charts/attendance_histogram.png")
plt.show()

# Histogram 3 - Study Hours
plt.figure(figsize=(8,5))
plt.hist(df["StudyHours"], bins=10)
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.savefig("charts/studyhours_histogram.png")
plt.show()