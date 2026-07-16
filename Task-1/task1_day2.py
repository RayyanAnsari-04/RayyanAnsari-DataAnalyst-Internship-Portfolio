import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\RAYYAN\Desktop\datawrangling-task1\data.csv")

# Dataset overview
print("SHAPE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns)

print("\nMISSING VALUES:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

print("\nDUPLICATES:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nFINAL SHAPE:")
print(df.shape)

# Save cleaned dataset
df.to_csv(r"C:\Users\RAYYAN\Desktop\datawrangling-task1\cleaned_data.csv", index=False)

print("\nCLEANED DATA SAVED SUCCESSFULLY")