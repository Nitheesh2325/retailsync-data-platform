import sqlite3
import pandas as pd
from logger import logger

conn = sqlite3.connect("retailsync.db")
logger.info("Business Reports Completed Successfully")

print("\nTOP 5 COMPANIES BY REVENUE")

query1 = """
SELECT
    company,
    ROUND(SUM(revenue),2) AS total_revenue
FROM orders
GROUP BY company
ORDER BY total_revenue DESC
LIMIT 5
"""

result1 = pd.read_sql(query1, conn)

print(result1)

print("\nTOP 5 PRODUCTS")

query2 = """
SELECT
    product,
    COUNT(*) AS total_orders
FROM orders
GROUP BY product
ORDER BY total_orders DESC
LIMIT 5
"""

result2 = pd.read_sql(query2, conn)

print(result2)

conn.close()