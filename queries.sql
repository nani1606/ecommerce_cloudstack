-- Top 5 products by quantity sold
SELECT p.description, SUM(s.quantity) as total_sold
FROM ecommerce.sales s
JOIN ecommerce.products p ON s.stock_code = p.stock_code
GROUP BY p.description
ORDER BY total_sold DESC
LIMIT 5;

-- Sales by country
SELECT c.country, COUNT(s.sale_id) as total_orders
FROM ecommerce.sales s
JOIN ecommerce.customers c ON s.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_orders DESC
LIMIT 5;