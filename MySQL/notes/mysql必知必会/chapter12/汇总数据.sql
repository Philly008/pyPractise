# 聚集函数aggregate function：运行在行组上，计算和返回单个值的函数。
/*
AVG() 返回某列的平均值
COUNT() 返回某列的行数
MAX() 返回某列的最大值
MIN() 返回某列的最小值
SUM() 返回某列值之和
*/
SELECT AVG(prod_price) AS avg_price FROM products;
SELECT AVG(prod_price) AS avg_price FROM products WHERE vend_id = 1003;

# 使用COUNT(*)对表中行的数目进行计数，不管表列中包含的是空值（NULL）还是非空值。
# 使用COUNT(column)对特定列中具有值的行进行计数，忽略NULL值。
SELECT COUNT(*) AS num_cust FROM customers;	# 5
SELECT COUNT(1) AS num_cust FROM customers;	# 5
SELECT COUNT(cust_email) AS num_cust FROM customers;

SELECT MAX(prod_price) AS max_price FROM products;

SELECT MIN(prod_price) AS min_price FROM products;

SELECT SUM(quantity) AS items_ordered FROM orderitems WHERE order_num = 20005;
SELECT SUM(item_price*quantity) AS total_price
FROM orderitems WHERE order_num = 20005;

SELECT AVG(DISTINCT prod_price) AS avg_price FROM products
WHERE vend_id = 1003;

SELECT prod_price FROM products WHERE vend_id = 1003;

# 组合聚集函数
SELECT COUNT(*) AS num_items,
	MIN(prod_price) AS price_min,
	MAX(prod_price) AS price_max,
	AVG(prod_price) AS price_avg
FROM products;



