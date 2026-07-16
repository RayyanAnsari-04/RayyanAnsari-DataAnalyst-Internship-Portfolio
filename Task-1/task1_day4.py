# DAY 4 Advanced Data Visualization & Insights Extraction
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# 1. BAR CHART

df[df.columns[0]].value_counts().plot(kind='bar')

plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Count")

plt.savefig("bar_chart.png")
plt.show()

# 2. HISTOGRAM

df[df.columns[1]].plot(kind='hist')

plt.title("Histogram")
plt.xlabel("Values")

plt.savefig("histogram.png")
plt.show()

# 3. PIE CHART

df[df.columns[0]].value_counts().head().plot(kind='pie', autopct='%1.1f%%')

plt.title("Pie Chart")

plt.savefig("pie_chart.png")
plt.show()

# 4. LINE CHART

df[df.columns[1]].plot(kind='line')

plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Values")

plt.savefig("line_chart.png")
plt.show()