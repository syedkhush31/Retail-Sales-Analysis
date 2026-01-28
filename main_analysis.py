import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/train.csv")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Remove rows with missing dates
df = df.dropna(subset=["Order Date"])

# Extract Year and Month
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Monthly sales aggregation
monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

# Create Year-Month column for plotting
monthly_sales["YearMonth"] = pd.to_datetime(
    monthly_sales["Year"].astype(str) + "-" +
    monthly_sales["Month"].astype(str) + "-01"
)

# Sort chronologically
monthly_sales = monthly_sales.sort_values("YearMonth")

# -----------------------------
# LINE CHART: Monthly Sales Trend
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["YearMonth"], monthly_sales["Sales"])
plt.title("Monthly Sales Trend Over Time")
plt.xlabel("Time")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
