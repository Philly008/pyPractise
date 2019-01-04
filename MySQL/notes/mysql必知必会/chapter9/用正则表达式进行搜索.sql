# 基本字符匹配
SELECT prod_name FROM products WHERE prod_name REGEXP '1000'
ORDER BY prod_name;	# 检索列prod_name包含文本1000的所有行

# . 匹配任意一个字符
SELECT prod_name FROM products WHERE prod_name REGEXP '.000' ORDER BY prod_name;
SELECT prod_name FROM products WHERE prod_name
REGEXP BINARY 'JetPack .000';	# REGEXP BINARY 匹配区分大小写，默认 REGEXP不区分大小写

# 进行OR匹配
SELECT prod_name FROM products WHERE prod_name REGEXP '1000|2000'
ORDER BY prod_name;

# 匹配几个字符之一
SELECT prod_name FROM products WHERE prod_name REGEXP '[123] Ton'
ORDER BY prod_name;
# 尽管[123] 匹配字符1、2或3，但[^123] 却匹配除这些字符外的任何东西。

# 匹配范围
SELECT prod_name FROM products WHERE prod_name REGEXP '[1-5] Ton'
ORDER BY prod_name;

# 匹配特殊字符，必须用 \\ 为前导
SELECT vend_name FROM vendors WHERE vend_name REGEXP '\\.'
ORDER BY vend_name;

# 匹配字符类
/*
[:alnum:] 任意字母和数字（同[a-zA-Z0-9]）
[:alpha:] 任意字符（同[a-zA-Z]）
[:blank:] 空格和制表（同[\\t]）
[:cntrl:] ASCII控制字符（ASCII 0到31和127）
[:digit:] 任意数字（同[0-9]）
[:graph:] 与[:print:]相同，但不包括空格
[:lower:] 任意小写字母（同[a-z]）
[:print:] 任意可打印字符
[:punct:] 既不在[:alnum:]又不在[:cntrl:]中的任意字符
[:space:] 包括空格在内的任意空白字符（同[\\f\\n\\r\\t\\v]）
[:upper:] 任意大写字母（同[A-Z]）
[:xdigit:] 任意十六进制数字（同[a-fA-F0-9]）
*/

# 匹配多个实例
/*
* 	0个或多个匹配
+ 	1个或多个匹配（等于{1,}）
? 	0个或1个匹配（等于{0,1}）
{n} 	指定数目的匹配
{n,} 	不少于指定数目的匹配
{n,m} 	匹配数目的范围（m不超过255）
*/
SELECT prod_name FROM products WHERE prod_name REGEXP
'\\([0-9] sticks?\\)' ORDER BY prod_name;
SELECT prod_name FROM products WHERE prod_name REGEXP
'[[:digit:]]{4}' ORDER BY prod_name;	# 匹配连在一起的4位数字

# 定位符
/*
^ 	文本的开始
$ 	文本的结尾
[[:<:]] 词的开始
[[:>:]] 词的结尾
*/
SELECT prod_name FROM products WHERE prod_name REGEXP
'^[0-9\\.]' ORDER BY prod_name;

SELECT 'hello' REGEXP '[0-9]';







