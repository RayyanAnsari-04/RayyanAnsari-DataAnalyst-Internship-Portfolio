
import pandas as pd

# Load Dataset
df = pd.read_excel("Cleaned_Ecommerce_Sales.xlsx")

# ------------------------------------------
# Key Metrics
# ------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

best_category = df.groupby("Category")["Sales"].sum().idxmax()
best_region = df.groupby("Region")["Sales"].sum().idxmax()

top_customer = df.groupby("Customer_Name")["Sales"].sum().idxmax()
top_product = df.groupby("Product")["Sales"].sum().idxmax()

# ------------------------------------------
# Display Business Insights
# ------------------------------------------

print("========== BUSINESS INSIGHTS ==========\n")

print(f"Total Sales      : ₹{total_sales:,.2f}")
print(f"Total Profit     : ₹{total_profit:,.2f}")
print(f"Best Category    : {best_category}")
print(f"Best Region      : {best_region}")
print(f"Top Customer     : {top_customer}")
print(f"Top Product      : {top_product}")

print("\n========== BUSINESS RECOMMENDATIONS ==========\n")

print("1. Increase inventory for the best-selling products.")
print("2. Focus marketing campaigns in the highest-performing region.")
print("3. Reward loyal customers with exclusive offers.")
print("4. Improve sales strategies for lower-performing categories.")
print("5. Monitor profit margins to maximize business growth.")

print("\n✅ Day 8 Business Storytelling Completed Successfully!")