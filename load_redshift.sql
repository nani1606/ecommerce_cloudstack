COPY ecommerce.products
FROM 's3://krishna-ecommerce-data/raw/products.csv'
IAM_ROLE 'arn:aws:iam::YOUR_ACCOUNT_ID:role/RedshiftRole-ecommerce'
CSV
IGNOREHEADER 1;

COPY ecommerce.customers
FROM 's3://krishna-ecommerce-data/raw/customers.csv'
IAM_ROLE 'arn:aws:iam::YOUR_ACCOUNT_ID:role/RedshiftRole-ecommerce'
CSV
IGNOREHEADER 1;

COPY ecommerce.sales (invoice_no, stock_code, customer_id, quantity, unit_price, invoice_date)
FROM 's3://krishna-ecommerce-data/raw/sales.csv'
IAM_ROLE 'arn:aws:iam::YOUR_ACCOUNT_ID:role/RedshiftRole-ecommerce'
CSV
IGNOREHEADER 1;