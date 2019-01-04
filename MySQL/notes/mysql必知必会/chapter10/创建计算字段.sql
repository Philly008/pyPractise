# 拼接字段 concatenate 将值联结到一起构成单个值
# concat()拼接串，即把多个串连接起来形成一个较长的串。
SELECT CONCAT(vend_name, ' (', vend_country, ')') FROM vendors
ORDER BY vend_name;

# rtrim()删除数据右侧多余的空格
SELECT CONCAT(RTRIM(vend_name), ' (', RTRIM(vend_country), ')')
FROM vendors ORDER BY vend_name;

# 使用别名
SELECT CONCAT(RTRIM(vend_name), ' (', RTRIM(vend_country), ')') AS vend_title
FROM vendors ORDER BY vend_name;

# 执行算数计算
SELECT prod_id, quantity, item_price,
	quantity*item_price AS expanded_price
FROM orderitems WHERE order_num = 20005;

SELECT NOW();




