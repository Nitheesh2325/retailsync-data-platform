import pandas as pd
import random
from datetime import datetime, timedelta
import os

os.makedirs("data/raw", exist_ok=True)

companies = [
    "Amazon", "Walmart", "Target", "Costco", "Best Buy",
    "Apple", "Microsoft", "Google", "Nike", "Adidas",
    "Samsung", "Dell", "HP", "Lenovo", "Sony",
    "Home Depot", "Lowe's", "CVS", "Walgreens", "Starbucks"
]

cities = ["New York", "Chicago", "Dallas", "Atlanta", "Los Angeles"]

products = ["Laptop", "Phone", "Headphones", "Monitor", "Keyboard", "Mouse"]

first_names = [
    "John", "Michael", "David", "Sarah", "Emily",
    "Jessica", "Daniel", "James", "Robert", "Sophia"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Wilson", "Taylor"
]

states = ["California", "Texas", "New York", "Illinois", "Georgia"]

orders = []

for i in range(1, 100001):
    order_id = i
    customer_id = random.randint(1000, 50000)

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    customer_name = first_name + " " + last_name
    customer_email = (
        first_name.lower()
        + "."
        + last_name.lower()
        + str(customer_id)
        + "@gmail.com"
    )

    company = random.choice(companies)
    city = random.choice(cities)
    state = random.choice(states)
    product = random.choice(products)

    quantity = random.randint(1, 5)
    price = random.randint(50, 1500)
    revenue = quantity * price

    order_date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))

    orders.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "company": company,
        "city": city,
        "state": state,
        "product": product,
        "quantity": quantity,
        "revenue": revenue,
        "order_date": order_date.date()
    })

df = pd.DataFrame(orders)

from config import RAW_DATA_PATH

df.to_csv(RAW_DATA_PATH, index=False)

print("100,000 Retail Orders Created Successfully")
print(df.head())
print(df.shape)