# 创建表，每个表只允许一个 AUTO_INCREMENT列，而且它必须被索引。
CREATE TABLE customers
(
	cust_id		INT 	NOT NULL AUTO_INCREMENT,
	cust_name	CHAR(50)	NOT NULL,
	cust_address	CHAR(50)	NULL,
	quantity 	INT 	NOT NULL DEFAULT 1,
	PRIMARY KEY(cust_id)
) ENGINE=INNODB;

# 返回最后一个 AUTO_INCREMENT值
SELECT LAST_INSERT_ID();

# 引擎类型
/*
InnoDB 是一个可靠的事务处理引擎，它不支持全文本搜索；
MEMORY 在功能等同于MyISAM，但由于数据存储在内存（不是磁盘）中，速度很快；
MyISAM 是一个性能极高的引擎，它支持全文本搜索，但不支持事务处理。
*/

# 更新表
# 给表添加一个列
ALTER TABLE vendors ADD vend_phone CHAR(20);

# 删除列
ALTER TABLE vendors DROP COLUMN vend_phone;

# 定义外键
ALTER TABLE orderitems
ADD CONSTRAINT fk_orderitems_orders
FOREIGN KEY(order_num) REFERENCES orders(order_num);

# 删除表
DROP TABLE customers2;

# 重命名表
RENAME TABLE customers2 TO customers,
	venders2 TO vendors,
	products2 TO products;
	






