import sqlite3
import pandas as pd

df_cleaned = pd.read_csv("transformed_data.csv")


conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()


create_table_query = '''
CREATE TABLE IF NOT EXISTS sales_data (
    OrderID TEXT,
    Date TEXT,
    Status TEXT,
    Fulfilment TEXT,
    Sales_Channel TEXT,  -- Replaced the space with an underscore
    SKU TEXT,
    Category TEXT,
    Qty INTEGER,
    Amount REAL,
    Amount_USD REAL,
    ship_city TEXT,
    ship_state TEXT,
    ship_postal_code TEXT,
    ship_country TEXT,
    promotion_ids TEXT,
    B2B BOOLEAN,
    Total_Sales REAL,
    AOV REAL
);
'''
cursor.execute(create_table_query)
print("Table created successfully!")


for index, row in df_cleaned.iterrows():
    cursor.execute('''
        INSERT INTO sales_data (OrderID, Date, Status, Fulfilment, Sales_Channel, SKU, Category, Qty, Amount, Amount_USD,
                                ship_city, ship_state, ship_postal_code, ship_country, promotion_ids, B2B, Total_Sales, AOV)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        row['Order ID'], row['Date'], row['Status'], row['Fulfilment'], row['Sales Channel'], row['SKU'], 
        row['Category'], row['Qty'], row['Amount'], row['Amount USD'], row['ship-city'], row['ship-state'], 
        row['ship-postal-code'], row['ship-country'], row['promotion-ids'], row['B2B'], 
        row['Total_sales'], row['AOV']
    ))


conn.commit()
print("Data inserted successfully into the database!")


cursor.execute('SELECT * FROM sales_data LIMIT 5')
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()
print("Database connection closed.")

