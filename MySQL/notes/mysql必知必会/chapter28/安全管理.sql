/*
MySQL用户账号和信息存储在名为mysql的MySQL数据库中。
*/
USE mysql;
SELECT USER FROM USER;

# 创建用户账号
CREATE USER ben IDENTIFIED BY '123456';

# 重命名账号
RENAME USER ben TO bforta;

# 删除用户账号
DROP USER bforta;

# 查看用户账号权限
SHOW GRANTS FOR bforta;	-- 结果为 grant usage on *.*  ，usage表示根本没有权限

# 设置权限
GRANT SELECT,INSERT ON test.* TO bforta;

# 撤销特定权限
REVOKE SELECT ON test.* FROM bforta;

/*
1. 整个服务器，使用GRANT ALL 和REVOKE ALL；
2. 整个数据库，使用ON database.*；
3. 特定的表，使用ON database.table；
4. 特定的列；
5. 特定的存储过程。
*/

# 更改口令
SET PASSWORD FOR bforta = PASSWORD('123abc');

SET PASSWORD = PASSWORD('123456');  -- 不指定用户名时，更新当前登录用户的口令。













