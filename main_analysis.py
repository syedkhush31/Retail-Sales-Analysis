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

# -----------------------------
# Monthly Sales Aggregation
# -----------------------------
monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
    .sort_values(["Year", "Month"])
)

print("Monthly Sales (first 10 rows):")
print(monthly_sales.head(10))

print("\nTop 5 months by sales:")
print(monthly_sales.sort_values("Sales", ascending=False).head())

print("\nBottom 5 months by sales:")
print(monthly_sales.sort_values("Sales").head())
