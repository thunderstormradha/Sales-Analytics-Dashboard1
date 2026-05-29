import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/sales_data.csv", encoding='latin1')
# First 5 rows
print(df.head())

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop Products:")
print(top_products)

# Region-wise Sales
region_sales = df.groupby('Region')['Sales'].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Category-wise Profit
category_profit = df.groupby('Category')['Profit'].sum()

print("\nCategory Profit:")
print(category_profit)

# Monthly Sales
monthly_sales = df.groupby('Ship Mode')['Sales'].sum()
print(monthly_sales)

# -----------------------------
# Charts
# -----------------------------

# Top Products Bar Chart
plt.figure(figsize=(10,5))
top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation=75)

plt.tight_layout()
plt.show()

# Region-wise Pie Chart
plt.figure(figsize=(7,7))

region_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Region-wise Sales")
plt.ylabel("")

plt.show()

# Category Profit Bar Chart
plt.figure(figsize=(8,5))

category_profit.plot(kind='bar')

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind='bar')

plt.title("Sales by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")

plt.show()