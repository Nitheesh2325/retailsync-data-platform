import pandas as pd
import sqlite3

# Connect database
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)
print("Connected to SQLite")

# Read clean data
df = pd.read_csv("data/staging/clean_orders.csv")

# Load into database
df.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

print("Orders Loaded Successfully")

# Verify
result = pd.read_sql(
    "SELECT COUNT(*) as total_orders FROM orders",
    conn
)

print(result)

conn.close()