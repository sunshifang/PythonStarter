import numpy as np

print("一、创建数组")
print('1. x = np.empty([3,2], dtype = int)')
x = np.empty([3,2], dtype = int) 
print (x)
print()


print('2. x = np.zeros(5)')
x = np.zeros(5)
print (x)
print()

y = np.zeros((5,), dtype = np.int) 
print(y)
print()

z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print(z)
print()

print('3. x = np.ones(5)')
# 默认为浮点数
x = np.ones(5) 
print(x)
print()
 
# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)
print()

print("二、从已有数组创建数组")
print("1. numpy.asarray")
x =  [1,2,3] 
a = np.asarray(x,dtype=float)  
print ("a = np.asarray(x) → ", a)
print()

print("2. 将元组转换为 ndarray")
x =  (1,2,3) 
a = np.asarray(x)  
print (a)
print()

print("3.将元组列表转换为 ndarray")
x =  [(1,2,3),(4,5)] 
a = np.asarray(x)  
print (a)
print()

print("4.动态创建数组 numpy.frombuffer")
s =  b'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print (a)
print()
'''
#Python2.x会报错！
s =  'Hello World'
a = np.frombuffer(s, dtype =  'S1')
print (a)
'''
print("5.使用迭代器创建数组")
# 使用range函数创建列表对象
list=range(5)
it = iter(list)

# 使用迭代器创建ndarray
x=np.fromiter(it, dtype=float)
print(x)
print()

print("三、从数值范围创建数组")
print("1.生成0到5的数组")
x = np.arange(5)  
print (x)
print()

print("2.生成0到5的数组,设置返回类型")
x = np.arange(5, dtype = float)  
print (x)
print()

print("3.生成0到5的数组,设置起始及终止步长")
x = np.arange(10,20,2,dtype=float)  
print (x)
print()

print("4.用函数创建数组 numpy.linspace")
a = np.linspace(1,10,10,2)
print(a)
print()

print("5.用函数创建等比数列 numpy.logspace")
a = np.logspace(1.0,2.0,num=10)
print("np.logspace(1.0,2.0,num=10) 的结果为：")
print(a)
print()
a = np.logspace(0,9,10,base=2)
print("np.logspace(1.0,2.0,num=10) 的结果为：")
print(a)
print()


