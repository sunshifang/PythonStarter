import numpy as np

print('NumPy排序')
a = np.array([[3,7],[9,1]])
print('我们的数组是：')
print(a)
print('执行np.sort(a)后：')
print(np.sort(a))
print('执行np.sort(a,axis=0)后：')
print(np.sort(a,axis=0))
print()
print('在sort函数中排序字段')
dt = np.dtype([('name', 'S10'),('age', int)])
#dt = np.dtype([('name', 'S10'),('age', int)]) #小写的s10会出错
a = np.array([('raju',21),('anil',25),('ravi',17),('amar',27)],dtype=dt)
print('我们的字段数组是：')
print(a)
print("按name排序(np.sort(a,order='name'))：")
print(np.sort(a,order='name'))

                
             



