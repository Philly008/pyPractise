# 从products表中检索一个名为prod_name的列
SELECT prod_name FROM products;

# 多条SQL语句必须以分号（;）分隔。SQL语句不区分大小写。在处理SQL语句时，其中所有空格都被忽略。

# 检索多个列
SELECT prod_id, prod_name, prod_price FROM products;

# 检索所有列
SELECT * FROM products;

# 检索不同的行
SELECT DISTINCT vend_id FROM products;

# 限制结果
SELECT prod_name FROM products LIMIT 5, 5;	# LIMIT 5, 5 指示MySQL返回从行5开始的5行
SELECT prod_name FROM products LIMIT 5;		# 返回前5行
SELECT prod_name FROM products LIMIT 1, 1;	# 检索出第二行
SELECT prod_name FROM products LIMIT 4 OFFSET 3;	# 从行3开始取4行

# 使用完全限定的表名
SELECT products.`prod_name` FROM products;
SELECT products.prod_name FROM test.`products`;














