
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv",encoding="latin1")

print("Sample Data:")
print(df.head())


print("\nDataset Info:")
print(df.info())


print("\nSummary Statistics:")
print(df.describe())

# Group by PRODUCTLINE instead of Product
sales_by_productline = df.groupby("PRODUCTLINE")["SALES"].sum().reset_index()

print("\nTotal Sales by Product Line:")
print(sales_by_productline)

plt.figure(figsize=(8,5))
plt.bar(sales_by_productline["PRODUCTLINE"], sales_by_productline["SALES"], color="skyblue")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.title("Sales by Product Line")
plt.xticks(rotation=45)
plt.show()

sales_by_region = df.groupby("Region")["Sales"].sum().reset_index()

print("\nTotal Sales by Region:")
print(sales_by_region)

plt.figure(figsize=(6,5))
plt.pie(sales_by_region["Sales"], labels=sales_by_region["Region"], autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution by Region")
plt.show()