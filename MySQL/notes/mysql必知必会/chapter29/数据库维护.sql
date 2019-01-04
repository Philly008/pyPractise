/* 备份数据:
1. mysqldump转储所有数据库内容到某个外部文件；
2. mysqlhotcopy从一个数据库复制所有数据；
3. backup table或select into outfile转储所有数据到某个外部文件；可以用restore table来复原。
4. 为了保证所有数据被写到磁盘，在备份前使用FLUSH TABLES语句。
*/
USE test;
# 检查表键是否正确
ANALYZE TABLE orders;

/*
CHANGED检查自最后一次检查以来改动过的表。 EXTENDED执行最
彻底的检查， FAST只检查未正常关闭的表， MEDIUM检查所有被删
除的链接并进行键检验， QUICK只进行快速扫描。
*/
CHECK TABLE orders, orderitems;

# 诊断启动问题
mysqld --help	# 显示帮助
mysqld --safe-MODE	# 装载减去某些最佳配置的服务器
mysqld --verbose	# 显示全文本信息
mysqld --version	# 显示版本信息然后退出

/*
查看日志文件：
1. 错误日志：data/hostname.err
2. 查询日志：data/hostname.log
3. 二进制日志：data/hostname-bin
4. 缓慢查询日志：data/hostname-slow.log
*/
# 刷新日志
FLUSH LOGS;




