import sqlite3
import pandas as pd

conn = sqlite3.connect("retailsync.db")

queries = {
    "Top 10 Companies by Revenue": """
        SELECT company, SUM(revenue) AS total_revenue
        FROM orders
        GROUP BY company
        ORDER BY total_revenue DESC
        LIMIT 10;
    """,

    "Top 10 Products": """
        SELECT product, COUNT(*) AS total_orders
        FROM orders
        GROUP BY product
        ORDER BY total_orders DESC
        LIMIT 10;
    """,

    "Monthly Revenue": """
        SELECT substr(order_date,1,7) AS month,
               SUM(revenue) AS revenue
        FROM orders
        GROUP BY month
        ORDER BY month;
    """
}

for title, query in queries.items():
    print("\n" + "="*60)
    print(title)
    print("="*60)
    print(pd.read_sql_query(query, conn))

conn.close()