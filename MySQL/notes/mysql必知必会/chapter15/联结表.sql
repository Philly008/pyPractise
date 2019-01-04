# 创建联结
SELECT vend_name, prod_name, prod_price
FROM vendors, products
WHERE vendors.`vend_id` = products.`vend_id`
ORDER BY vend_name, prod_name;


# 内部联结
SELECT vend_name, prod_name, prod_price
FROM vendors INNER JOIN products
ON vendors.vend_id = products.`vend_id`
ORDER BY vend_name, prod_name;

# 联结多个表
SELECT cust_name, cust_contact
FROM customers, orders, orderitems
WHERE customers.cust_id = orders.`cust_id`
AND orderitems.`order_num` = orders.`order_num`
AND prod_id = 'TNT2';


