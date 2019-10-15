import numpy as np
import numpy.matlib

print('1) np.matlib.empty((2,2))填充为随机数：')
print(np.matlib.empty((2,2)))
print()

print('2) numpy.matlib.zeros()创建用0填充的矩阵：')
print(np.matlib.zeros((2,2)))
print()

print('3) numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零')
print (np.matlib.eye(n =  4, M =  4, k =  0, dtype =  float))
print()

print('4) numpy.matlib.identity() 函数返回给定大小的单位矩阵')
print(np.matlib.identity(5,dtype=float))
print()

print('5) numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的')
print(np.matlib.rand(3,3))
print()

print('6) 矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的')
i = np.matrix('1,2;3,4')
print(i)
print()

j = np.asarray(i)
print('np.asarray(i): ')
print(j)
print()

k = np.asmatrix(j)
print('np.asmatrix(j): ')
print(k)
