/*
触发器是MySQL响应DELETE、INSERT、UPDATE语句而自动执行的一条MySQL语句
*/
/* 
在创建触发器时，需要给出4条信息:
1. 唯一的触发器名；
2. 触发器关联的表；
3. 触发器应该响应的活动（DELETE、INSERT或UPDATE）；
4. 触发器何时执行（处理之前或之后）
*/
# Not allowed to return a result set from a trigger 此错误需加上 INTO @ee 解决
CREATE TRIGGER newproduct AFTER INSERT ON products
FOR EACH ROW SELECT 'Product added' INTO @ee;

# 删除触发器
DROP TRIGGER newproduct;

/*
1. 在INSERT触发器代码内，可引用一个名为NEW的虚拟表，访问被插入的行；
2. 在BEFORE INSERT触发器中，NEW中的值也可以被更新（允许更改被插入的值）；
3. 对于AUTO_INCREMENT列，NEW在INSERT执行之前包含0，在INSERT执行之后包含新的自动生成值。
*/
CREATE TRIGGER neworder AFTER INSERT ON orders
FOR EACH ROW SELECT NEW.order_num INTO @ee;

INSERT INTO orders(order_date, cust_id)
VALUES(NOW(), 10001);

SELECT order_num FROM orders;

/*
1. 在DELETE触发器代码内，可以引用一个名为OLD的虚拟表，访问被删除的行；
2. OLD中的值全都是只读的，不能更新。
*/

CREATE TABLE `archive_orders` (
  `order_num` INT(11) NOT NULL AUTO_INCREMENT,
  `order_date` DATETIME NOT NULL,
  `cust_id` INT(11) NOT NULL,
  PRIMARY KEY (`order_num`)
) ENGINE=INNODB AUTO_INCREMENT=20013 DEFAULT CHARSET=latin1;

DELIMITER $$
CREATE TRIGGER deleteorder BEFORE DELETE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO archive_orders(order_num, order_date, cust_id)
    VALUES(OLD.order_num, OLD.order_date, OLD.cust_id);
END $$
DELIMITER ;

DELETE FROM orders WHERE order_num = 20010;
SELECT * FROM orders WHERE order_num = 20010;
SELECT * FROM orderitems WHERE order_num = 20010;
SELECT * FROM archive_orders;


/*
1. 在UPDATE触发器代码中，可以引用一个名为OLD的虚拟表访问以前（UPDATE语句前）
    的值，引用一个名为NEW的虚拟表访问新更新的值；
2. 在BEFORE UPDATE触发器中，NEW中的值可能也被更新（允许更改将要用于UPDATE语句中的值）；
3. OLD中的值全都是只读的，不能更新。
*/
CREATE TRIGGER updatevendor BEFORE UPDATE ON vendors
FOR EACH ROW SET NEW.vend_state = UPPER(NEW.vend_state);






