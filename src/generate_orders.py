import pandas as pd
import random
from datetime import datetime, timedelta

orders = []

companies = [
    "Amazon",
    "Walmart",
    "Target",
    "Costco",
    "Best Buy"
]

cities = [
    "New York",
    "Chicago",
    "Dallas",
    "Atlanta",
    "Los Angeles"
]

products = [
    "Laptop",
    "Phone",
    "Headphones",
    "Monitor",
    "Keyboard",
    "Mouse"
]

for i in range(1, 100001):

    order_id = i

    customer_id = random.randint(1000, 50000)

    company = random.choice(companies)

    city = random.choice(cities)

    product = random.choice(products)

    quantity = random.randint(1, 5)

    price = random.randint(50, 1500)

    revenue = quantity * price

    order_date = (
        datetime(2025, 1, 1)
        + timedelta(days=random.randint(0, 365))
    )

    orders.append([
        order_id,
        customer_id,
        company,
        city,
        product,
        quantity,
        revenue,
        order_date
    ])

df = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "customer_id",
        "company",
        "city",
        "product",
        "quantity",
        "revenue",
        "order_date"
    ]
)

df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("100,000 Retail Orders Created Successfully")
print(df.head())