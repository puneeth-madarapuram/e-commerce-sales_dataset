import pandas as pd
df = pd.read_csv("./data/E-Commerce.csv", encoding="latin1")

print(df.info())

# 1.what are the most popular products?
popular_products = df['Description'].value_counts().head(10)
print("Most Popular Products:")
print(popular_products)

popular_products.to_csv("./reports/exports/the_most_popular_products.csv")

# 2.which country has the highest number of orders?
country_orders = df['Country'].value_counts().head(10)
print("\nCountries with Highest Number of Orders:")
print(country_orders)

country_orders.to_csv("./reports/exports/countries_with_highest_number_of_orders.csv")

# 3.what is the total revenue generated from each country?
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTotal Revenue by Country:")    
print(country_revenue)

country_revenue.to_csv("./reports/exports/total_revenue_by_country.csv")

# 4.Which customers have made the highest number of purchases?
top_customers = df['CustomerID'].value_counts().head(10)
print("Top 10 customers with highest number of purchases:")
print(top_customers)

top_customers.to_csv("./reports/exports/top_10_customers_by_purchases.csv")

# 5.which year had the highest sales?
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year'] = df['InvoiceDate'].dt.year 
yearly_sales = df.groupby('Year')['UnitPrice'].sum().sort_values(ascending=False)
print("\nYearly Sales:")
print(yearly_sales)

yearly_sales.to_csv("./reports/exports/yearly_sales.csv")

# 6.What are the top 10 products by sales?
top_products = df.groupby('Description')['UnitPrice'].sum().sort_values(ascending=False).head(10)
print("Top 10 products by sales:")
print(top_products)

top_products.to_csv("./reports/exports/top_10_products_by_sales.csv")

# 7.Are there any patterns in order cancellations or returns?
cancellations = df[df['InvoiceNo'].str.startswith('C')]
print(f"Total Cancellations/Returns: {len(cancellations)}")
print(cancellations.head())

cancellations.to_csv("./reports/exports/order_cancellations_and_returns.csv")

# 8.What are the top-selling products or categories?
top_products = df['Description'].value_counts().head(10)
print("Top 10 Selling Products:")
print(top_products)

top_products.to_csv("./reports/exports/top_10_selling_products.csv")

# 9.total amount spent by each customer?
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
customer_spending = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
print("\nTotal Amount Spent by Each Customer:")
print(customer_spending)

customer_spending.to_csv("./reports/exports/total_amount_spent_by_each_customer.csv")

# 10.monthly sales trends?
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum().sort_index()
print("\nMonthly Sales Trends:")
print(monthly_sales)

monthly_sales.to_csv("./reports/exports/monthly_sales_trends.csv")








