# E-Commerce Sales Data Warehouse on AWS

A cloud-based data warehouse pipeline to process, store, transform, and analyze e-commerce sales data using AWS S3, Glue, and Redshift. Built to demonstrate Cloud Data Engineering skills for ETL, cloud storage, and data warehousing.

## Overview
This project processes ~779,495 e-commerce sales records from the [Online Retail Dataset](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci). It:
- Cleans and structures data locally with Python and MySQL.
- Stores raw data in AWS S3.
- Transforms data with AWS Glue (e.g., aggregates sales by product).
- Loads data into AWS Redshift for analytics.
- Runs SQL queries to derive insights (e.g., top-selling products).
![image](https://github.com/user-attachments/assets/4a259e28-54b6-4f29-935f-e8ebeea24f12)
![image](https://github.com/user-attachments/assets/15fc77e5-2231-47dc-b25f-c04917c316b6)


## Architecture
```mermaid
graph TD
    A[Dataset<br>CSV] --> B[Python<br>process_data.py]
    B --> C[AWS S3<br>raw/]
    C --> D[AWS Glue<br>ecommerce-etl]
    D --> E[AWS S3<br>transformed/]
    C --> F[AWS Redshift<br>ecommerce]
