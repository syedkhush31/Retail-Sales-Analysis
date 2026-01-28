import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Remove rows with missing dates
df = df.dropna(subset=["Order Date"])

# Extract Year and Month
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Verify extraction
print("Year-Month extraction check:")
print(df[["Order Date", "Year", "Month"]].head())

# Basic sanity check
print("\nUnique years:", sorted(df["Year"].unique()))
print("Unique months:", sorted(df["Month"].unique()))
