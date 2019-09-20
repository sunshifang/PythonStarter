import mysql.connector

mydb = mysql.connector.connect(
  host="cdb-gyvnhcni.bj.tencentcdb.com", 
  user="root",
  password="z4h4m2p4_pml"
)


#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='exam', charset='utf8')

#cur=conn.cursor() 
print(mydb)
