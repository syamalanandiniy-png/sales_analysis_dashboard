
import pandas as pd

# Step 1: Read the sales CSV file
df = pd.read_csv("data/sales_data.csv")

# Step 2: Display the first 5 rows
print("SALES DATA")
print(df.head())

# Step 3: Display total number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Step 4: Display column information
print("\nDATASET INFORMATION")
print(df.info())

# Step 5: Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Step 6: Calculate revenue for each order
df["Revenue"] = df["Quantity"] * df["Price"]

# Step 7: Calculate total revenue
total_revenue = df["Revenue"].sum()
print("\nTOTAL SALES REVENUE")
print("Rs.", total_revenue)

# Step 8: Count total orders
total_orders = df["Order_ID"].nunique()
print("\nTOTAL ORDERS")
print(total_orders)

# Step 9: Calculate product-wise quantity
product_sales = df.groupby("Product")["Quantity"].sum()

print("\nPRODUCT-WISE SALES")
print(product_sales)

# Step 10: Find the best-selling product
best_product = product_sales.idxmax()

print("\nBEST-SELLING PRODUCT")
print(best_product)

# Step 11: Calculate city-wise revenue
city_sales = df.groupby("City")["Revenue"].sum()

print("\nCITY-WISE REVENUE")
print(city_sales)

# Step 12: Find the city with highest revenue
top_city = city_sales.idxmax()

print("\nTOP PERFORMING CITY")
print(top_city)

# Step 13: Convert Date column into date format
df["Date"] = pd.to_datetime(df["Date"])

# Step 14: Extract month
df["Month"] = df["Date"].dt.strftime("%B")

# Step 15: Calculate monthly revenue
monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMONTHLY REVENUE")
print(monthly_sales)

# Step 16: Check duplicate records
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Step 17: Remove duplicate records
df = df.drop_duplicates()

# Step 18: Check missing values
print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Step 19: Remove rows with missing values
df = df.dropna()

# Step 20: Check data after cleaning
print("\nCLEANED DATA")
print(df.head())

print("\nFINAL DATASET SHAPE")
print(df.shape)

# Step 21: Save cleaned data
df.to_csv("output/cleaned_sales_data.csv", index=False)

print("\nCleaned sales data saved successfully!")
