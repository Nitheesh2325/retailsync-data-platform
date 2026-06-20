# RetailSync Data Platform

## Overview

RetailSync Data Platform is an end-to-end Data Engineering project built using Python, Pandas, SQLite, SQL, and GitHub.

This project simulates a real-world retail data pipeline that ingests retail order data, performs quality validation, cleans data, loads it into a database, generates business analytics, and creates operational logs.

---

## Architecture

Raw Retail Data
↓
Data Quality Validation
↓
Data Cleaning
↓
SQLite Database
↓
SQL Analytics
↓
Business Reports
↓
Operational Logging

---

## Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Git
- GitHub

---

## Project Structure

retailsync-data-platform/

├── data/
│ ├── raw/
│ ├── staging/
│ └── curated/

├── docs/

├── logs/

├── sql/
│ └── create_orders_table.sql

├── src/
│ ├── generate_orders.py
│ ├── data_quality.py
│ ├── data_cleaning.py
│ ├── load_to_sqlite.py
│ ├── business_reports.py
│ └── logger.py

├── requirements.txt

├── retailsync.db

└── README.md

---

## Features

### Data Generation

- Simulates retail order data
- Generates realistic transactions

### Data Quality Validation

- Detects missing values
- Detects duplicates
- Validates data consistency

### Data Cleaning

- Removes invalid records
- Cleans null values
- Standardizes data

### Database Integration

- Loads data into SQLite
- Creates structured tables

### SQL Analytics

- Revenue analysis
- Product analysis
- Company performance analysis

### Business Reporting

- Top companies by revenue
- Top selling products
- Business insights

### Operational Logging

- Pipeline execution logs
- Success and failure tracking

---

## Example Business Questions Answered

1. Which company generated the highest revenue?
2. What are the top-selling products?
3. How many orders were processed?
4. What is the total revenue generated?

---

## Skills Demonstrated

- Data Engineering
- ETL Development
- Data Validation
- Data Cleaning
- SQL Analytics
- Database Management
- Python Development
- Git Version Control

---

## Future Improvements

- REST API Integration
- Azure Data Storage
- AWS S3 Integration
- Apache Airflow Scheduling
- Power BI Dashboard
- Streamlit Dashboard

---

## Author

Nitheesh Chand

Data Engineering Portfolio Project