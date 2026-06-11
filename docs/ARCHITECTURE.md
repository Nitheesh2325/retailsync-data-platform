# RetailSync Data Platform Architecture

## Business Flow

Website Orders
        ↓
Mobile App Orders
        ↓
Marketplace Orders
        ↓

Raw Layer
(data/raw)

        ↓

Validation Layer
(Data Quality Checks)

        ↓

Staging Layer
(data/staging)

        ↓

Transformation Layer

        ↓

Curated Layer
(data/curated)

        ↓

SQLite Data Warehouse

        ↓

Business Analytics

        ↓

KPI Reports
