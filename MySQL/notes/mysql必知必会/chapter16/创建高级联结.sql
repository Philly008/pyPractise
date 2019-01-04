# 使用表别名，主要原因是能在单条SELECT语句中不止一次引用相同的表
SELECT cust_name, cust_contact
FROM customers AS c, orders AS o, orderitems AS oi
WHERE c.cust_id = o.`cust_id`
AND oi.`order_num` = o.`order_num`
AND prod_id = 'TNT2';

# 自联结
SELECT p1.prod_id, p1.prod_name 
FROM products AS p1, products AS p2
WHERE p1.`vend_id` = p2.`vend_id`
AND p2.`prod_id` = 'DTNTR';

# 自然联结是这样一种联结，其中你只能选择那些唯一的列。这一般是通过对表
# 使用通配符（SELECT *），对所有其他表的列使用明确的子集来完成的。
SELECT c.*, o.order_num, o.order_date, oi.prod_id, oi.quantity, oi.item_price
FROM customers AS c, orders AS o, orderitems AS oi
WHERE c.cust_id = o.`cust_id`
AND oi.`order_num` = o.`order_num`
AND prod_id = 'FB';

# 外部联结：联结包含了那些再相关表中没有关联行的行。
SELECT customers.cust_id, orders.`order_num`
FROM customers LEFT OUTER JOIN orders
ON customers.cust_id = orders.`cust_id`;

SELECT customers.cust_id, orders.`order_num`
FROM customers RIGHT OUTER JOIN orders
ON customers.cust_id = orders.`cust_id`;

# 使用带聚集函数的联结
SELECT customers.cust_name,
	customers.`cust_id`,
	COUNT(orders.`order_num`) AS num_ord
FROM customers LEFT OUTER JOIN orders
ON customers.`cust_id` = orders.`cust_id`
GROUP BY customers.cust_id;






