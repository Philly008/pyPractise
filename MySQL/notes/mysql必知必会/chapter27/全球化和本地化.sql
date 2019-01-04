/*
字符集为字母和符号的集合；
编码为某个字符集成员的内部表示；
校对为规定字符如何比较的指令。
*/
# 查看所支持的字符集完整列表
SHOW CHARACTER SET;

# 查看所支持校对的完整列表
SHOW COLLATION;

# 查看所有的字符集和校对
SHOW VARIABLES LIKE 'character%';
SHOW VARIABLES LIKE 'collation%';

# 给表指定字符集和校对
CREATE TABLE mytable
(
	column1 INT,
	column2 VARCHAR(10)
) DEFAULT CHARACTER SET hebrew
  COLLATE hebrew_general_ci;
  
# 允许对每个列设置字符集和校对
CREATE TABLE mytable2
(
	column1 INT,
	column2 VARCHAR(10),
	column3 VARCHAR(10) CHARACTER SET latin1 COLLATE latin1_general_ci
) DEFAULT CHARACTER SET hebrew
  COLLATE hebrew_general_ci;

# 指定校对顺序排序
SELECT * FROM customers
ORDER BY cust_name, cust_city COLLATE latin1_general_cs;



