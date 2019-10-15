import numpy as np
import numpy.matlib

print('numpy.save() 函数将数组保存到以 .npy 为扩展名的文件中')
a = np.array([1,2,3,4,5])
np.save('tmp/outfile.npy',a)

b = np.load('tmp/outfile.npy')
print(b)
print()

a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0,1.0,0.1)
c = np.sin(b)
np.savez('runoob.npz',a,b,sin_array = c)
r = np.load('runoob.npz')
print(r.files)
print(r["arr_0"])
print(r["arr_1"])
print(r["sin_array"])
print()

print('savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据')
a = np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b = np.loadtxt('out.txt')
print(b)
print()

print('使用delimiter参数：')
a = np.arange(0,10,0.5).reshape(4,-1)
print(a)
np.savetxt("out.txt",a,fmt="%d",delimiter=",")
b = np.loadtxt("out.txt",delimiter=",")
print(b)
