import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)

monthly_revenue = pd.read_sql_query("""
SELECT 
    substr(order_date, 1, 7) AS month,
    SUM(revenue) AS revenue
FROM orders
GROUP BY month
ORDER BY month
""", conn)

plt.figure(figsize=(10, 5))
plt.plot(monthly_revenue["month"], monthly_revenue["revenue"])
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/charts/monthly_revenue.png")

conn.close()

print("Dashboard chart created successfully")