import pymssql
import warnings
print('''
pymssql模块使用

一、基本使用流程
pymssql的使用十分简单，基本就以下几个步骤：
1. 创建连接：使用connect()方法创建连接，返回Connection对象
2. 交互操作：使用Connection对象的Cursor对象的各种方法与数据库交互
3. 关闭连接

二、创建连接
pymssql.connect(服务器、用户名、密码、数据库)方法返回一个连接对象
提供用户名密码时，是用户验证登录，否则就是Windows身份认证。
其他常用选项
·database(str): 指定默认数据库
·as_dict(bool): True，查询结果返回的是字典，否则(默认)为列表
·auocommit(bool): 是否自动提交，默认为False，需手动调用commit提交
·port(str): 指定服务器端口，默认应该是1433.

三、交互操作
在连接建立成功后，与数据库的交互主要是通过Cursor对象进行的。
1.提交sql命令
  cursor.execute('sql语句')
2.调用存储过程
  如果要调用存储过程，使用Cursor对象的callproc方法
  cursor.callproc('pro_name',('param1',))
3.提交修改
  如果对数据进行了修改，且在连接时没有把autocommit设置为True,则需要
  手动调用commit进行提交修改。
  conn.commit()
4.获取结果
  如果只选的是有返回值的sql语句，则可以通过Cursor对象的fetch方法来
  获取结果，结果默认为元组类型.
  cursor.execute("select count(*) from persons")
  cnt = cursor.fetchone()[0]
  如果返回对多条记录，可以像这样遍历所有的结果
  cursor.execute('select * from persons')
  row = cursor.fetchone()
  while row:
      print("ID=%d, Name=%s" % (row[0], row[1]))
  或者：
  cursor.execute('select * from persons where salesrep=%s', 'John')
  for row in cursor:
      print('row = %r' % (row,))
      
      
  

''')
#建立连接并获取cursor
conn = pymssql.connect("192.168.2.107", "sa", "Aa123456", "otcwms")
cursor = conn.cursor()

sql = "SELECT top 10 * FROM vLProduct"
cursor.execute(sql)
row = cursor.fetchone()
print("用while循环遍历，每次获取一行数据")
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

print("使用for循环来迭代查询结果")
cursor.execute(sql)
for row in cursor:
    print("ID=%d, Name=%s" % (row[0], row[1]))

print(type(cursor))
print(isinstance(cursor,tuple))
print(isinstance(cursor,list))
print(isinstance(cursor,pymssql.Cursor))




cursor.close()
#conn.close()
print('''


''')
#conn = pymssql.connect("192.168.2.107", "sa", "Aa123456", "otcwms")
sql = "SELECT name from syscolumns where id=object_id('vCConsumingOutStockBill')"
cursor = conn.cursor()
cursor.execute(sql)
print("cursor.rownumber1 = %d" % cursor.rownumber)
print("rows = cursor.fetchall()后")
rows = cursor.fetchall()      
print("cursor.rownumber2 = %d" % cursor.rownumber)

#cursor.scroll(1)
print("使用for循环来迭代查询结果")
#for row in rows:
#    print("Name = %s" % row[0])


for row in cursor:
    print("Name1 = %s" % row[0])
    
cursor.close()
conn.close()
