# RetailSync Data Platform

## Project Overview

RetailSync Data Platform is a simulated enterprise retail analytics platform designed to demonstrate modern Data Engineering practices.

The platform processes retail order data from multiple sales channels, applies data quality validation rules, transforms raw business data into trusted analytical datasets, and generates key business performance metrics.

This project was designed to simulate a real-world retail environment where Data Engineers are responsible for building reliable data pipelines, improving data quality, and supporting business decision-making.

---

## Business Problem

RetailSync receives customer orders from:

* Website
* Mobile Application
* Marketplace Partners

Business teams reported several challenges:

* Duplicate orders appearing in reports
* Missing customer information
* Invalid transaction records
* Revenue discrepancies between systems
* Lack of trusted business KPIs

The Data Engineering team was tasked with building a centralized data platform to improve data quality and provide accurate reporting.

---

## Project Objectives

* Build a production-style ETL pipeline
* Validate incoming retail order data
* Identify and handle bad records
* Create clean analytical datasets
* Generate business KPIs
* Demonstrate Data Engineering best practices

---

## Data Sources

The platform processes:

* Orders Data
* Customer Data
* Product Data

---

## Planned Data Volume

* 100,000+ Orders
* 10,000+ Customers
* 1,000+ Products

---

## Data Quality Rules

The platform will identify:

* Duplicate Orders
* Missing Customer IDs
* Missing Product IDs
* Negative Revenue Values
* Invalid Dates
* Cancelled Orders

---

## Business KPIs

The platform will generate:

* Daily Revenue
* Monthly Revenue
* Average Order Value
* Top Products
* Top Categories
* Top Regions
* Cancellation Rate

---

## Technologies

* Python
* Pandas
* SQL
* SQLite
* VS Code
* Git

---

## Expected Outcome

The final platform will simulate a realistic enterprise data engineering workflow including ingestion, validation, transformation, analytics, monitoring, and reporting.
