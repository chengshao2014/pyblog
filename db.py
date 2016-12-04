#!/usr/bin/python
#encoding:utf-8
import MySQLdb as db
conn = db.connect(
		host = 'localhost',
		user = 'root',
		passwd = '123456',
		db = 'test',
		port = 3306,
		charset = 'utf8'
	)
#创建游标
#发送python传递给Mysql的指令
#接收MySQL返回给Python的数据
cur = conn.cursor()
cur.execute("SELECT * FROM t1")
data = cur.fetchall()
print data

cur.close()
