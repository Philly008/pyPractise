# 使用where子句
SELECT prod_name, prod_price FROM products WHERE prod_price = 2.50;

# WHERE子句操作符
# 检查单个值
SELECT prod_name, prod_price FROM products WHERE prod_name = 'fuses';
SELECT prod_name, prod_price FROM products WHERE prod_price < 10;
SELECT prod_name, prod_price FROM products WHERE prod_price <= 10;

# 不匹配检查
SELECT vend_id, prod_name FROM products WHERE vend_id <> 1003;
SELECT vend_id, prod_name FROM products WHERE vend_id != 1003;

# 范围值检查
SELECT prod_name, prod_price FROM products WHERE prod_price BETWEEN 5 AND 10;

# 空值检查
SELECT cust_id FROM customers WHERE cust_email IS NULL;













