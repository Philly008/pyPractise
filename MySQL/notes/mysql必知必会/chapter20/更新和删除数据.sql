# 更新数据
UPDATE customers
SET cust_name = 'The Fudds',
	cust_email = 'eleme@fudd.com'
WHERE cust_id = 10005;

# 删除数据
DELETE FROM customers WHERE cust_id = 10006;

# 从表中删除所有行，可使用 truncate table 语句，更快
TRUNCATE TABLE customers;


