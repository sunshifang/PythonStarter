dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict)
print("str(dict): ",str(dict))
print("********访问字典********")
print("dict['Name']: ",dict['Name'])
print("dict['Age']: ",dict['Age'])
print("dict['Alice']: ")
#print(dict['Alice'])

print("********修改字典********")
print("更新Age：dict['Age']=8")
dict['Age']=8
print("添加信息：dict['School']='菜鸟教程'")
dict['School']='菜鸟教程'
print("修改后的字典为：", dict)
print("popitem: ",dict.popitem())

print("********删除字典元素********")

del dict['Name']
print("删除键'Name': del dict['Name']",dict)

dict.clear()
print("清空字典: dict.clear()",dict)

del dict
print("删除字典: del dict后再次查看dict会出错。",dict)
      
