import numpy as np
import pandas as pd

#df = pd.DataFrame(pd.read_excel('bill.xlsx'))

#d = pd.DataFrame([[1,2,3],[4,5,6]],columns = ['a','b','c'])
#print(d)

#df=pd.read_excel('bill.xlsx')#这个会直接默认读取到这个Excel的第一个表单
#data=df.head(2)#默认读取前5行的数据
#data=df.values
#print(data[0])
#print("获取到所有的值:\n{0}".format(data))#格式化输出
print("************************************************")
print("      Python利用pandas处理Excel数据的应用")
print("************************************************")


df=pd.read_excel('bill.xlsx')#默认读取工作薄的第一个工作表

print("一、pandas读取Excel文件")
print("1.打开工作表")
print("  可同时打开多个工作表，sheet_name是一个工作表名的数组")
print("  也可以通过工作表索引来指定一个或多个工作表")
print("  df=pd.read_excel('bill.xlsx',sheet_name='sheetName') #打开工作表")
data=df.head(3)
print("  读取到指定行数的数据/n{0}".format(data))
print("")

print("2.保存读取到的数据")
print("  data=df.head([rowNUm]) #指定行数的数据保存在data变量中")
print("  data=df.values #所有的数据保存在data变量中，data是一个列表")
print("  读取指定的单行，数据保存在列表里面")

data=df.loc[0].values #0表示第一行，values读取数据不包含表头
print("读取指定行的数据：\n{0}".format(data))
print("")

print("二、操作Excel的行和列")
print("1.读取指定的单行，数据保存在列表里面")
print("  data=df.loc[0].values #0表示第一行，values读取数据不包含表头")
print("")

print("2.读取指定的多行")
print("  data=df.loc[[1,2]].values #数据在loc[]里面指定")
data=df.loc[[1,3]].values
print(" 读取指定多行的数据：\n{0}".format(data))
print("")

print("3.读取指定的行列")
print("  data=df.iloc[1,2] #读取第一行第二列的值，不需要嵌套列表")
data=df.iloc[1,2]
print("  读取指定行列(单元格)的数据：{0}".format(data))
print("")

print("4.读取指定的多行多列值")
print("  data=df.iloc[[1,2],[1,5]]")
data=df.iloc[[1,2],[1,5]]
print("  读取指定多行多列(单元格)的数据：\n{0}".format(data))
print("")

print("5.获取所有行的指定列")
print("  data=df.iloc[:,[0,1,6]]")
data=df.iloc[:,[0,1,6]]
print(data)
print("")

print("6.获取行号")
print("  df.index.values")
print(df.index.values)
print("")

print("7.获取列名")
print("  df.columns.values")
print(df.columns.values)
print("")

print("8.获取指定行数的值")
print("  df.sample(3).values #这个方法类似于head()方法以及df.vlaues方法")
print(df.sample(3).values)
print("")

print("9.获取指定列的值")
print("  df['指示编号'].values")
print(df['指示编号'].values)
print(df['资材编号'].values)
print(df['单据编号'].values)
print("")

print("三、pandas处理Excel数据成为字典")
print("  row_data=df.loc[iColNo,[0,1,2,3,4]].to_dict()")
test_data=[]
for i in df.index.values:
    row_data=df.loc[i,["单据编号","指示编号","资材编号","计划数量"]].to_dict()
    test_data.append(row_data)
print("  最终获取的数据是：{0}".format(test_data))
    


