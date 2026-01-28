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

# Line chart: Monthly sales trend
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

plt.figure(figsize=(8, 5))
bars = plt.bar(
    category_sales["Category"],
    category_sales["Sales"],
    color=["#4C72B0", "#55A868", "#C44E52"]
)

plt.title("Total Sales by Product Category", fontsize=14)
plt.xlabel("Category", fontsize=11)
plt.ylabel("Total Sales", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.6)

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

# -----------------------------
# Region-wise Sales Analysis
# -----------------------------
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=True)
)

plt.figure(figsize=(9, 5))
bars = plt.barh(
    region_sales["Region"],
    region_sales["Sales"],
    color="#8172B2"
)

plt.title("Total Sales by Region", fontsize=14)
plt.xlabel("Total Sales", fontsize=11)
plt.ylabel("Region", fontsize=11)
plt.grid(axis="x", linestyle="--", alpha=0.6)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f"{width:,.0f}",
        va="center",
        fontsize=10
    )

plt.tight_layout()
plt.show()

# -----------------------------
# Sub-Category Sales Analysis
# -----------------------------
subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

print("\nTop 10 Sub-Categories by Sales:")
print(subcategory_sales.head(10))

# Take top 10 for clear visualization
top_subcategories = subcategory_sales.head(10)

plt.figure(figsize=(10, 6))
bars = plt.barh(
    top_subcategories["Sub-Category"],
    top_subcategories["Sales"],
    color="#64B5CD"
)

plt.title("Top 10 Sub-Categories by Sales", fontsize=14)
plt.xlabel("Total Sales", fontsize=11)
plt.ylabel("Sub-Category", fontsize=11)
plt.grid(axis="x", linestyle="--", alpha=0.6)

for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f"{width:,.0f}",
        va="center",
        fontsize=10
    )

plt.tight_layout()
plt.show()
