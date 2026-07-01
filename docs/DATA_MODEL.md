# RetailSync Enterprise Data Model

## Dataset Information

Rows:
100,000+

Purpose:
Simulate a real enterprise retail order system.

---

## Table: orders

| Column | Data Type | Description |
|---------|-----------|-------------|
| order_id | INTEGER | Unique order ID |
| customer_id | INTEGER | Unique customer ID |
| customer_name | TEXT | Customer full name |
| customer_email | TEXT | Customer email |
| company | TEXT | Retail company |
| city | TEXT | Customer city |
| state | TEXT | Customer state |
| zip_code | TEXT | ZIP code |
| country | TEXT | Country |
| order_date | DATE | Date order placed |
| region | TEXT | Sales region |
| product_id | INTEGER | Product ID |
| product | TEXT | Product name |
| category | TEXT | Product category |
| brand | TEXT | Product brand |
| unit_price | FLOAT | Price per item |
| quantity | INTEGER | Quantity ordered |
| discount | FLOAT | Discount amount |
| tax | FLOAT | Tax amount |
| shipping_cost | FLOAT | Shipping cost |
| profit | FLOAT | Profit earned |
| warehouse | TEXT | Warehouse location |
| shipping_method | TEXT | Shipping method |
| order_status | TEXT | Order status |
| delivery_date | DATE | Delivery date |
| payment_method | TEXT | Payment method |
| customer_segment | TEXT | Customer segment |
| sales_rep | TEXT | Sales representative |