# ==========================================
# TASK 4
# Day 7 - Correlation Analysis
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("Cleaned_Ecommerce_Sales.xlsx")

# ------------------------------------------
# Select Numerical Columns
# ------------------------------------------

numerical_data = df[["Sales", "Profit", "Quantity"]]

# ------------------------------------------
# Correlation Matrix
# ------------------------------------------

correlation_matrix = numerical_data.corr()

print("========== CORRELATION MATRIX ==========\n")
print(correlation_matrix)

# ------------------------------------------
# Plot Heatmap
# ------------------------------------------

plt.figure(figsize=(6,5))

plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")

plt.colorbar()

plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

plt.title("Correlation Matrix")

# Display correlation values inside the heatmap

for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(
            j,
            i,
            round(correlation_matrix.iloc[i, j], 2),
            ha='center',
            va='center',
            color='black'
        )

plt.tight_layout()
plt.show()

print("\n✅ Day 7 Correlation Analysis Completed Successfully!")