import pandas as pd
import mysql.connector
import os

# MySQL credentials
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "admin123")
MYSQL_DB = "ecommerce_db"

# Read and clean CSV
df = pd.read_csv("online_retail_II.csv")
df = df.dropna(subset=["Customer ID"]).query("Quantity > 0")
df = df.dropna().drop_duplicates()
df["Customer ID"] = df["Customer ID"].astype(str)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Extract dimensions
products = df[["StockCode", "Description"]].drop_duplicates(subset=["StockCode"]).rename(columns={"StockCode": "stock_code", "Description": "description"})
customers = df[["Customer ID", "Country"]].drop_duplicates(subset=['Customer ID']).rename(columns={"Customer ID": "customer_id", "Country": "country"})
sales = df[["Invoice", "StockCode", "Customer ID", "Quantity", "Price", "InvoiceDate"]].rename(
    columns={"Invoice": "invoice_no", "StockCode": "stock_code", "Customer ID": "customer_id", "Price": "unit_price", "InvoiceDate": "invoice_date"}
)

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
cursor = conn.cursor()

# Bulk insert
cursor.executemany("INSERT INTO products (stock_code, description) VALUES (%s, %s)", 
    [(row["stock_code"], row["description"]) for _, row in products.iterrows()])
conn.commit()
print(f"Inserted {products.shape[0]} products")

cursor.executemany("INSERT INTO customers (customer_id, country) VALUES (%s, %s)", 
    [(row["customer_id"], row["country"]) for _, row in customers.iterrows()])
conn.commit()
print(f"Inserted {customers.shape[0]} customers")

sales_data = [(row["invoice_no"], row["stock_code"], row["customer_id"], row["quantity"], row["unit_price"], row["invoice_date"]) 
              for _, row in sales.iterrows()]
batch_size = 10000
for i in range(0, len(sales_data), batch_size):
    cursor.executemany(
        "INSERT INTO sales (invoice_no, stock_code, customer_id, quantity, unit_price, invoice_date) VALUES (%s, %s, %s, %s, %s, %s)",
        sales_data[i:i+batch_size]
    )
    conn.commit()
    print(f"Inserted {min(i+batch_size, len(sales_data))} sales")

cursor.close()
conn.close()

# Save CSVs
products.to_csv("products.csv", index=False)
customers.to_csv("customers.csv", index=False)
sales.to_csv("sales.csv", index=False)
print("CSVs saved")