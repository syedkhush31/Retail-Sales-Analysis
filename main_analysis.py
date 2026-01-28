import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

print("Rows before removing missing dates:", df.shape[0])

# Remove rows with missing Order Date
df = df.dropna(subset=["Order Date"])

print("Rows after removing missing dates:", df.shape[0])

# Verify date range
print("\nDate range after cleaning:")
print("Min date:", df["Order Date"].min())
print("Max date:", df["Order Date"].max())
