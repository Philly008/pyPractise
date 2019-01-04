# 分组允许把数据分为多个逻辑组，以便能对每个组进行聚集计算
# 分组是在SELECT语句的GROUP BY子句中建立的。
# 除聚集计算语句外，SELECT语句中的每个列都必须在GROUP BY子句中给出
SELECT vend_id, COUNT(*) AS num_prods FROM products GROUP BY vend_id;

# 使用WITH ROLLUP关键字，可以得到每个分组以及每个分组汇总级别的值
SELECT vend_id, COUNT(*) AS num_prods FROM products
GROUP BY vend_id WITH ROLLUP;

# 过滤分组，WHERE过滤行，HAVING过滤分组
SELECT cust_id, COUNT(*) AS orders FROM orders
GROUP BY cust_id HAVING COUNT(*) >=2;
SELECT vend_id,COUNT(*) AS num_prods FROM products WHERE prod_price >= 10
GROUP BY vend_id HAVING COUNT(*) >= 2; 

# 分组与排序
SELECT order_num, SUM(quantity*item_price) AS ordertotal FROM orderitems
GROUP BY order_num HAVING SUM(quantity*item_price) >= 50 ORDER BY ordertotal;

# SELECT子句顺序
/*
子 句 		说 明 					是否必须使用
SELECT 		要返回的列或表达式 			是
FROM 		从中检索数据的表 			仅在从表选择数据时使用
WHERE 		行级过滤 				否
GROUP BY 	分组说明 				仅在按组计算聚集时使用
HAVING 		组级过滤 				否
ORDER BY 	输出排序顺序 				否
LIMIT 		要检索的行数 				否
*/



