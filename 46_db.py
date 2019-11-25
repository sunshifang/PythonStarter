print('''
Python操作SqlSeve数据库--pymssql
''')
import pyodbc
cnxn =pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.2.107;PORT=1433;DATABASE=otcwms;UID=sa;PWD=Aa123456')
cursor  =  cnxn.cursor()
print(cursor)
cursor.execute("select * from lproduct")
row = cursor.fetchone()
if row:
    print(row)

