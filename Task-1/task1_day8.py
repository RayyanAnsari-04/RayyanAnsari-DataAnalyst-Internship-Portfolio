# DAY 8 Final Visualization Review & Presentation Preparation
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# 1. Bar Chart

df[df.columns[0]].value_counts().head().plot(kind='bar')

plt.title("Final Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Count")

plt.savefig("final_bar_chart.png")
plt.show()

# 2. Histogram

df[df.columns[1]].plot(kind='hist')

plt.title("Final Histogram")
plt.xlabel("Values")

plt.savefig("final_histogram.png")
plt.show()

# 3. Pie Chart

df[df.columns[0]].value_counts().head().plot(kind='pie', autopct='%1.1f%%')

plt.title("Final Pie Chart")

plt.savefig("final_pie_chart.png")
plt.show()

# 4. Completion Message

print("FINAL VISUALIZATIONS READY ✔")