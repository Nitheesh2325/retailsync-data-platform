import pandas as pd

# Read raw data
df = pd.read_csv("data/raw/orders.csv")

print("\nOriginal Records:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Remove invalid revenue values
df = df[df["revenue"] > 0]

# Remove invalid quantity values
df = df[df["quantity"] > 0]

print("Clean Records:", len(df))

# Save clean data to staging layer
df.to_csv(
    "data/staging/clean_orders.csv",
    index=False
)

print("\nClean Data Saved Successfully")
print(df.head())