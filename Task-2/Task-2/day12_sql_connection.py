import pyodbc
import pandas as pd


# Connect to SQL Server

connection = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-B99NA699\\SQLEXPRESS;"
    "Database=StudentPerformanceDB;"
    "Trusted_Connection=yes;"
)

print("Database Connected Successfully")


# Fetch data from SQL table

query = "SELECT * FROM StudentPerformance"

df = pd.read_sql(query, connection)


print("\nFirst 5 Rows:")
print(df.head())


print("\nDataset Shape:")
print(df.shape)


# Close connection

connection.close()