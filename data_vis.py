import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Data Visualization for Total sales by product
df_cleaned = pd.read_csv("transformed_data.csv")
category_sales = df_cleaned.groupby('Category')['Total_sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Total_sales', data=category_sales)
plt.title('Total Sales by Product Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Data Visualization for Total sales by Region
region_sales = df_cleaned.groupby('ship-state')['Total_sales'].sum().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x='ship-state', y='Total_sales', data=region_sales)
plt.title('Total sales by region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# top 10 products by total sales:
top_products = df_cleaned.groupby('SKU')['Total_sales'].sum().reset_index()
top_products = top_products.nlargest(10, 'Total_sales')  # Get the top 10 products

plt.figure(figsize=(10, 6))  # Set a valid figure size
sns.barplot(x='SKU', y='Total_sales', data=top_products)
plt.title('Top 10 products by total sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

