/*
存储过程简单来说就是为以后的使用而保存的一条或多条MySQL语句的集合。
使用存储过程有3个主要的好处，即简单、安全、高性能。
*/
# 执行存储过程
CALL productpricing(@pricelow,
	@pricehigh,
	@priceaverage);
	
# 创建存储过程
DELIMITER //	# 临时使用 // 作为新的语句结束分隔符
CREATE PROCEDURE productpricing()
BEGIN
    SELECT AVG(prod_price) AS priceaverage
    FROM products;
END //
DELIMITER ;

# 调用存储过程
CALL productpricing();

# 删除存储过程
DROP PROCEDURE IF EXISTS productpricing;

# 使用参数
DELIMITER //
CREATE PROCEDURE productpricing(
    OUT pl DECIMAL(8,2),
    OUT ph DECIMAL(8,2),
    OUT pa DECIMAL(8,2)
    )
BEGIN
    SELECT MIN(prod_price)
    INTO pl
    FROM products;
    SELECT MAX(prod_price)
    INTO ph
    FROM products;
    SELECT AVG(prod_price)
    INTO pa
    FROM products;
END //
DELIMITER ;

/*
MySQL支持 IN（传递给存储过程）、OUT（从存储过程传出）
和INOUT（对存储过程传入和传出）类型的参数
*/
# 所有MySQL变量都必须以@开始。
CALL productpricing(@pricelow,
    @pricehigh,
    @priceaverage);
SELECT @pricehigh, @pricelow, @priceaverage;

DELIMITER //
CREATE PROCEDURE ordertotal(
    IN onumber INT,
    OUT ototal DECIMAL(8,2)
)
BEGIN
    SELECT SUM(item_price*quantity)
    FROM orderitems
    WHERE order_num = onumber
    INTO ototal;
END //
DELIMITER ;

CALL ordertotal(20005, @total);
SELECT @total;
CALL ordertotal(20009, @total);
SELECT @total;

# 建立智能存储过程
DROP PROCEDURE IF EXISTS ordertotal;
DELIMITER //
-- Name: ordertotal
-- Parameters: onumber = order number
--		taxable = 0 if not taxable, 1 if taxable
--		ototal = order total variable
CREATE PROCEDURE ordertotal(
    IN onumber INT,
    IN taxable BOOLEAN,
    OUT ototal DECIMAL(8,2)
) COMMENT 'Obtain order total, optionally adding tax'
BEGIN
    -- Declare variable for total
    DECLARE total DECIMAL(8,2);
    -- Declare tax percentage
    DECLARE taxrate INT DEFAULT 6;
    
    -- Get the order total
    SELECT SUM(item_price*quantity)
    FROM orderitems
    WHERE order_num = onumber
    INTO total;
    
    -- Is this taxable?
    IF taxable THEN
      -- Yes, so add taxrate to the total
      SELECT total+(total/100*taxrate) INTO total;
    END IF;
    -- And finally, save to out variable
    SELECT total INTO ototal;
END //
    
CALL ordertotal(20005, 0, @total);
SELECT @total;

CALL ordertotal(20005, 1, @total);
SELECT @total;

# 检查存储过程
SHOW CREATE PROCEDURE ordertotal;
SHOW PROCEDURE STATUS LIKE 'ordertotal';










