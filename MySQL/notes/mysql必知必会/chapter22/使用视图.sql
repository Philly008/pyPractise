/*
视图是虚拟的表，只包含使用时动态检索数据的查询。
    使用视图的原因：
1. 重用SQL语句；
2. 简化复杂的SQL操作；
3. 使用表的组成部分而不是整个表；
4. 保护数据；
5. 更改数据格式和表示。

视图用 CREATE VIEW语句来创建。
使用SHOW CREATE VIEW viewname; 来查看创建视图的语句。
用DROP删除视图，其语法为 DROP VIEW viewname;
更新视图 CREATE OR REPLACE VIEW
*/
# 使用视图简化复杂的联结
CREATE VIEW productcustomers AS
SELECT cust_name, cust_contact, prod_id
FROM customers, orders, orderitems
WHERE customers.`cust_id` = orders.`cust_id`
AND orderitems.`order_num` = orders.`order_num`;

SELECT * FROM productcustomers;

# 用视图重新格式化检索出的数据
CREATE VIEW vendorlocations AS
SELECT CONCAT(RTRIM(vend_name), ' (', RTRIM(vend_country), ')') AS vend_title
FROM vendors
ORDER BY vend_name;

SELECT * FROM vendorlocations;

# 用视图过滤不想要的数据
CREATE VIEW customeremaillist AS
SELECT cust_id, cust_name, cust_email
FROM customers
WHERE cust_email IS NOT NULL;

SELECT * FROM customeremaillist;

# 使用视图与计算字段
CREATE VIEW orderitemsexpanded AS 
SELECT order_num,
	prod_id,
	quantity,
	item_price,
	quantity*item_price AS expanded_price
FROM orderitems;

SELECT * FROM orderitemsexpanded WHERE order_num = 20005;



