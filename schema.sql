-- MySQL Schema (Step 1)
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE products (
    stock_code VARCHAR(50) PRIMARY KEY,
    description VARCHAR(255)
);

CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_no VARCHAR(50),
    stock_code VARCHAR(50),
    customer_id VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(10,2),
    invoice_date DATETIME
);

-- Redshift Schema (Step 4)
CREATE SCHEMA ecommerce;

CREATE TABLE ecommerce.products (
    stock_code VARCHAR(50) PRIMARY KEY,
    description VARCHAR(255)
);

CREATE TABLE ecommerce.customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE ecommerce.sales (
    sale_id INTEGER IDENTITY(1,1) PRIMARY KEY,
    invoice_no VARCHAR(50),
    stock_code VARCHAR(50),
    customer_id VARCHAR(50),
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    invoice_date TIMESTAMP
);