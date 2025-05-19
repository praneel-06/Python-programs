import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "supermarket_sales.csv"
df = pd.read_csv(file_path)

# 1. Basic Data Exploration
print("First 5 rows:")
print(df.head())
print("\nNumber of rows and columns:")
print(df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# 2. Sales Analysis
# Total revenue
total_revenue = df['Total'].sum()
print(f"Total Revenue: {total_revenue}")

# Branch with highest sales
highest_sales_branch = df.groupby('Branch')['Total'].sum().idxmax()
print(f"Branch with highest sales: {highest_sales_branch}")

# Most sold product category
most_sold_category = df['Product line'].value_counts().idxmax()
print(f"Most sold product category: {most_sold_category}")

# Average transaction amount
average_transaction = df['Total'].mean()
print(f"Average transaction amount: {average_transaction}")

# 3. Customer Behavior
# Unique customers
unique_customers = df['Invoice ID'].nunique()
print(f"Number of unique customers: {unique_customers}")

# Sales by Customer Type
customer_type_sales = df.groupby('Customer type')['Total'].sum()
print("\nTotal Sales by Customer Type:")
print(customer_type_sales)

# Most preferred payment method
preferred_payment = df['Payment'].value_counts().idxmax()
print(f"Most preferred payment method: {preferred_payment}")

# 4. Trend Analysis
# Day of the week with highest sales
df['Date'] = pd.to_datetime(df['Date'])
df['DayOfWeek'] = df['Date'].dt.day_name()
day_with_highest_sales = df.groupby('DayOfWeek')['Total'].sum().idxmax()
print(f"Day with highest sales: {day_with_highest_sales}")

# Line chart for daily sales trend
daily_sales = df.groupby('Date')['Total'].sum()
plt.figure(figsize=(12, 5))
daily_sales.plot(title='Daily Sales Trend', marker='o')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Month with highest total sales
df['Month'] = df['Date'].dt.month_name()
month_with_highest_sales = df.groupby('Month')['Total'].sum().idxmax()
print(f"Month with highest sales: {month_with_highest_sales}")

# 5. Customer Satisfaction
# Average rating
average_rating = df['Rating'].mean()
print(f"Average customer rating: {average_rating}")

# Branch with highest customer rating
highest_rating_branch = df.groupby('Branch')['Rating'].mean().idxmax()
print(f"Branch with highest rating: {highest_rating_branch}")

# Bar chart for average rating per product category
product_categories = df.groupby('Product line')['Rating'].mean()
plt.figure(figsize=(10, 5))
plt.bar(product_categories.index, product_categories.values, color='skyblue')
plt.xticks(rotation=45)
plt.xlabel('Product Line')
plt.ylabel('Average Rating')
plt.title('Average Rating per Product Line')
plt.show()
