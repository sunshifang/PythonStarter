import mysql.connector

try:
    mydb = mysql.connector.connect(
      host="cdb-gyvnhcni.bj.tencentcdb.com",
      port="10122",
      user="root",
      password="z4h4m2p4_pml",
      db=test_db
    )
    print("数据库服务器已连接……")
except:
    print("数据库服务器连接错误！")
    
print()
print("输出所有数据库列表：")
mycursor = mydb.cursor()
"""
mycursor.execute("DROP DATABASE IF EXISTS test_db")
mycursor.execute("CREATE DATABASE test_db")
"""
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites 
mycursor.execute(sql)
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


print("输出数据表")
mycursor.execute("SHOW TABLES")
 
for x in mycursor:
    print(x)

  

    

'''  



  
mycursor.commit()   
print()
print("创建并显示数据表")

sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
 
mycursor.execute(sql)

'''
