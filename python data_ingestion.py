import pandas as pd 
df = pd.read_csv("Amazon Sale Report.csv", dtype={23: str})
#data cleanig
df_cleaned = df.drop(columns=["Unnamed: 22","fulfilled-by"])

df_cleaned['promotion-ids'].fillna('No Promotion', inplace=True)
df_cleaned['Courier Status'].fillna('Unknown', inplace=True)
df_cleaned['currency'].fillna('Unkown', inplace=True)
df_cleaned['ship-city'].fillna('Unknown', inplace=True)
df_cleaned['ship-state'].fillna('Unknown', inplace=True)
df_cleaned['ship-country'].fillna('Unknown', inplace=True)

df_cleaned['Amount'].fillna(0, inplace=True)
print(df_cleaned.isnull().sum())

df_cleaned['Amount USD'] = df_cleaned['Amount'] * 0.012
print(df_cleaned[['Amount','Amount USD']].head())

df_cleaned['Total_sales'] = df_cleaned['Qty'] * df_cleaned['Amount']
df_cleaned['AOV'] = df_cleaned['Total_sales'] / df_cleaned['Order ID'].nunique()
print(df_cleaned[['Total_sales', 'AOV']].head())

#aggregation:
category_sales = df_cleaned.groupby('Category')['Total_sales'].sum().reset_index()
region_sales = df_cleaned.groupby('ship-state')['Total_sales'].sum().reset_index()
print("Total Sales by Category:\n", category_sales)
print("Total Sales by Category:\n", region_sales)
df_cleaned.to_csv(r'C:\Users\rpaya\OneDrive\Desktop\etpl_project\transformed_data.csv', index=False)



