/*
通配符wildcard：用来匹配值的一部分的特殊字符
搜索模式search pattern：由字面值、通配符或两者组合构成的搜索条件
*/
# 百分号（%）通配符：表示任何字符出现任意次数
SELECT prod_id, prod_name FROM products WHERE prod_name LIKE 'jet%';
SELECT prod_id, prod_name FROM products WHERE prod_name LIKE '%anvil%';

# 下划线（_）通配符：匹配单个字符
SELECT prod_id, prod_name FROM products WHERE prod_name LIKE '_ ton anvil';




