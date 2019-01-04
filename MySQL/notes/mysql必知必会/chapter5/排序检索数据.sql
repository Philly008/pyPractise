# 排序数据
SELECT prod_name FROM products ORDER BY prod_name;
SELECT prod_name FROM products ORDER BY prod_id;

# 按多个列排序
SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price, prod_name;

# 指定排序方向
SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC;	# 降序排列
SELECT prod_id, prod_price, prod_name FROM products ORDER BY prod_price DESC, prod_name;
SELECT prod_price FROM products ORDER BY prod_price DESC LIMIT 1;	# 找出最昂贵物品









