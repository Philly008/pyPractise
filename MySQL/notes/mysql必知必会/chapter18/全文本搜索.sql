# MyISAM 支持全文本搜索，InnoDB 不支持全文本搜索
# 启用全文本搜索支持
CREATE TABLE productnotes
(
  note_id	INT 	NOT NULL AUTO_INCREMENT,
  prod_id	CHAR(10)	NOT NULL,
  note_date	DATETIME	NOT NULL,
  note_text	TEXT		NULL,
  PRIMARY KEY(note_id),
  FULLTEXT(note_text)
) ENGINE=MYISAM;

# 不要在导入数据时使用FULLTEXT
# 进行全文本搜索：match() 指定被搜索的列；against()指定要使用的搜索表达式
SELECT note_text
FROM productnotes
WHERE MATCH(note_text) AGAINST('rabbit');

# 全文本搜索的一个重要部分就是对结果排序。具有较高等级的行先返回
SELECT note_text,
	MATCH(note_text) AGAINST('rabbit') AS rank
FROM productnotes;

# 使用查询扩展
SELECT note_text
FROM productnotes
WHERE MATCH(note_text) AGAINST('anvils' WITH QUERY EXPANSION);




