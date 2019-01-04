# 插入完整的行
INSERT INTO customers( cust_name,
	cust_address,
	cust_city,
	cust_state,
	cust_zip,
	cust_country,
	cust_contact,
	cust_email
	)
VALUES(
	'Pep E. LaPew',
	'100 Main',
	'Los Angeles',
	'CA',
	'90046',
	'USA',
	NULL,
	NULL);
	
# 插入多个行
INSERT INTO customers(cust_name,
	cust_address,
	cust_city,
	cust_state,
	cust_zip,
	cust_country)
VALUES('Pep E. LaPew',
	'100 Main',
	'Los Angeles',
	'CA',
	'90046',
	'USA'),
	('2Pep E. LaPew',
	'2100 Main',
	'2Los Angeles',
	'2CA',
	'290046',
	'2USA');
	
# 插入检索出的数据
INSERT INTO customers(cust_contact,
	cust_email,
	cust_name)
SELECT cust_contact,
	cust_email,
	cust_name
FROM custnew;






