import pandas as pd

# Read raw orders data
df = pd.read_csv("data/raw/orders.csv")

print("\nRetail Orders Loaded")
print("Total Records:", len(df))

# Check for missing values
missing_values = df.isnull().sum()

print("\nMissing Values Report")
print(missing_values)

# Check for duplicate records
duplicates = df.duplicated().sum()

print("\nDuplicate Records:", duplicates)

# Save quality report
quality_report = pd.DataFrame({
    "column": missing_values.index,
    "missing_values": missing_values.values
})

quality_report.to_csv(
    "logs/data_quality_report.csv",
    index=False
)

print("\nData Quality Report Saved Successfully")