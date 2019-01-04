/*
游标（cursor）是一个存储在MySQL服务器上的数据库查询，它不是一条SELECT语句，
而是被该语句检索出来的结果集。
    使用游标：
1. 在能够使用游标前，必须声明它；
2. 一旦声明后，必须打开游标以供使用；
3. 对于填有数据的游标，根据需要取出各行；
4. 在结束游标使用时，必须关闭游标。
*/
# 创建游标
DELIMITER //
CREATE PROCEDURE processorders()
BEGIN
    -- Declare local variables
    DECLARE done BOOLEAN DEFAULT 0;
    DECLARE o INT;
    DECLARE t DECIMAL(8,2);
    
    -- Declare the cursor
    DECLARE ordernumbers CURSOR
    FOR
    SELECT order_num FROM orders;
    -- Declare continue handler
    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done=1;

    -- Create a table to store the results
    CREATE TABLE IF NOT EXISTS ordertotals
    (order_num INT, total DECIMAL(8,2));    
    
    -- Open the cursor
    OPEN ordernumbers;
    
    -- Loop throughall rows
    REPEAT
    
        -- Get order number
        FETCH ordernumbers INTO o;  # 使用FETCH检索当前order_num到声明的名为o的变量中
        
        -- Get the total for this order
        CALL ordertotal(o, 1, t);
        
        -- Insert order and total into ordertotals
        INSERT INTO ordertotals(order_num, total)
        VALUES(o, t);
    
    -- End of loop
    UNTIL done END REPEAT;
    
    -- Close the cursor
    CLOSE ordernumbers;
END //
DELIMITER ;

# 打开和关闭游标
OPEN ordernumbers;
CLOSE ordernumbers;

CALL processorders();
SELECT * FROM ordertotals;








