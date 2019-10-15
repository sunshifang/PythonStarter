import numpy as np

print('NumPy字节交换')
a = np.array([1,256,8755],dtype=np.int16)
print('我们的数组是：')
print(a)
print('以16进制表示内存数据map(hex,a)：')
print(map(hex,a))
print('#byteswap函数通过传入true来原地交换')
print('调用byteswap函数：')
print(a.byteswap(True))
print('十六进制形式：')
print(map(hex,a))
print('*******************************************')
print()

print('NumPy的副本和视图')
a = np.arange(6)
print('我们的数组是：')
print(a)
print('调用id()函数：')
print(id(a))
print('a赋值给b(b=a)：')
b = a
print(b)
print('b拥有相同的id（）：')
print(id(b))
print('修改b的形状(b.shape=3,2): ')
b.shape=3,2
print(b)
print('a的形状也同时被修改了：')
print(a)
print('*******************************************')
print()

# 最开始 a 是个 3X2 的数组
print('修改视图不会修改原数组：')
a = np.arange(6).reshape(3,2)  
print ('数组 a：')
print (a)
print ('创建 a 的视图：')
b = a.view()  
print (b)
print ('两个数组的 id() 不同：')
print ('a 的 id()：')
print (id(a))
print ('b 的 id()：' )
print (id(b))
# 修改 b 的形状，并不会修改 a
b.shape =  2,3
print ('b 的形状：')
print (b)
print ('a 的形状：')
print (a)
print()

print('使用切片创建视图修改数据会影响到原始数组：')
arr = np.arange(12)
print('我们的数组：')
print(arr)
print('创建切片：')
a = arr[3:]
b = arr[3:]
a[1] = 123
b[2] = 234
print(arr)
print(id(a),id(b),id(arr[3:]))
print()

print('副本或深拷贝')
print('ndarray.copy()函数创建一个副本，对副本数据进行修改，不会影响原始数据，他们物理内存不在同一位置。')
a = np.array([[10,10],[2,3],[4,5]])
print('数组 a: ')
print(a)
b = a.copy()
print('数组b=a.copy(): ')
print(b)
print('#b与a不共享任何内容')
print('我们能够写入b来写入a吗？')
print(b is a)
print('修改b的内容：')
b[0,0] = 100
print(b)
print('a保持不变：')
print(a)


                
             



