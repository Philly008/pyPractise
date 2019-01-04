# 文本处理函数
/*
Left() 返回串左边的字符
Length() 返回串的长度
Locate() 找出串的一个子串
Lower() 将串转换为小写
LTrim() 去掉串左边的空格
Right() 返回串右边的字符
RTrim() 去掉串右边的空格
Soundex() 返回串的SOUNDEX值
SubString() 返回子串的字符
Upper() 将串转换为大写
*/
SELECT vend_name, UPPER(vend_name) AS vend_name_upcase
FROM vendors ORDER BY vend_name;

# soundex是一个将任何文本串转换为描述其语音表示的字母数字模式的算法。对串进行发音比较而不是字母比较。
SELECT cust_name, cust_contact FROM customers WHERE 
SOUNDEX(cust_contact) = SOUNDEX('Y Lie');

# 日期和时间处理函数
/*
AddDate() 增加一个日期（天、周等）
AddTime() 增加一个时间（时、分等）
CurDate() 返回当前日期
CurTime() 返回当前时间
Date() 返回日期时间的日期部分
DateDiff() 计算两个日期之差
Date_Add() 高度灵活的日期运算函数
Date_Format() 返回一个格式化的日期或时间串
Day() 返回一个日期的天数部分
DayOfWeek() 对于一个日期，返回对应的星期几
Hour() 返回一个时间的小时部分
Minute() 返回一个时间的分钟部分
Month() 返回一个日期的月份部分
Now() 返回当前日期和时间
Second() 返回一个时间的秒部分
Time() 返回一个日期时间的时间部分
Year() 返回一个日期的年份部分
*/
SELECT cust_id, order_num FROM orders WHERE DATE(order_date) = '2005-09-01';

# 检索出order_date为2005年9月的所有行
SELECT cust_id, order_num FROM orders
WHERE YEAR(order_date) = 2005 AND MONTH(order_date) = 9;

/*
Abs() 返回一个数的绝对值
Cos() 返回一个角度的余弦
Exp() 返回一个数的指数值
Mod() 返回除操作的余数
Pi() 返回圆周率
Rand() 返回一个随机数
Sin() 返回一个角度的正弦
Sqrt() 返回一个数的平方根
Tan() 返回一个角度的正切
*/












