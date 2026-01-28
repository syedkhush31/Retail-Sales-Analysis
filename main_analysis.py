import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load & Clean Data
# -----------------------------
df = pd.read_csv("data/train.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df = df.dropna(subset=["Order Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# -----------------------------
# Monthly Sales Aggregation
# -----------------------------
monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["YearMonth"] = pd.to_datetime(
    monthly_sales["Year"].astype(str) + "-" +
    monthly_sales["Month"].astype(str) + "-01"
)

monthly_sales = monthly_sales.sort_values("YearMonth")

# -----------------------------
# Line Chart: Monthly Sales Trend
# -----------------------------
plt.figure(figsize=(11, 5))
plt.plot(
    monthly_sales["YearMonth"],
    monthly_sales["Sales"],
    linewidth=2.5,
    marker="o"
)

plt.title("Monthly Sales Trend (2015–2018)", fontsize=14)
plt.xlabel("Time", fontsize=11)
plt.ylabel("Total Sales", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# -----------------------------
# Category-wise Sales Analysis
# -----------------------------
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

print("\nCategory-wise Total Sales:")
print(category_sales)

# -----------------------------
# Bar Chart: Category-wise Sales
# -----------------------------
colors = ["#4C72B0", "#55A868", "#C44E52"]

plt.figure(figsize=(8, 5))
bars = plt.bar(
    category_sales["Category"],
    category_sales["Sales"],
    color=colors
)

plt.title("Total Sales by Product Category", fontsize=14)
plt.xlabel("Category", fontsize=11)
plt.ylabel("Total Sales", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.show()
