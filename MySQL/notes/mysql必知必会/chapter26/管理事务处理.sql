/*
MyISAM引擎不支持明确的事务处理管理；
InnoDB引擎支持明确的事务处理管理。

事务处理（transaction processing）可以用来维护数据库的完整性，它保证成批的
MySQL操作要么完全执行，要么完全不执行。

事务（transaction）指一组SQL语句；
回退（rollback）指撤销指定SQL语句的过程；
提交（commit）指将未存储的SQL语句结果写入数据库表；
保留点（savepoint）指事务处理中设置的临时占位符（place-holder），你可以
	对它发布回退（与回退整个事务处理不同）。
*/
SELECT * FROM ordertotals;
START TRANSACTION;	# 标记事务的开始
DELETE FROM ordertotals;
SELECT * FROM ordertotals;
ROLLBACK;	# 回退MySQL语句
SELECT * FROM ordertotals;

# 事务处理用来管理INSERT、UPDATE和DELETE语句。不能回退SELECT、CREATE或DROP操作

START TRANSACTION;
DELETE FROM orderitems WHERE order_num = 20010;
DELETE FROM orders WHERE order_num = 20010;
COMMIT;	# 明确提交事务

# 保留点
SAVEPOINT delete1;
ROLLBACK TO delete1;	# 回退到保留点，会自动释放保留点
RELEASE SAVEPOINT delete1;	# 明确释放保留点

# 更改默认的提交行为，默认的MySQL行为是自动提交所有更改。
SET autocommit=0;







