import pandas as pd
import pyodbc


# Connect to SQL Server

connection = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-B99NA699\\SQLEXPRESS;"
    "Database=StudentPerformanceDB;"
    "Trusted_Connection=yes;"
)


# Load data from SQL Server

query = "SELECT * FROM StudentPerformance"

df = pd.read_sql(query, connection)


# Dataset Information

print("Dataset Information:")
print(df.info())


# First 5 rows

print("\nFirst 5 Rows:")
print(df.head())


# Dataset Description

print("\nStatistical Summary:")
print(df.describe())


# Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())


# Check Duplicate Records

print("\nDuplicate Records:")
print(df.duplicated().sum())


# Remove Duplicates

df = df.drop_duplicates()


print("\nFinal Dataset Shape:")
print(df.shape)


connection.close()