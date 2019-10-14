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

print("四、切片操作")
print("1.实例")
a = np.arange(10)
s = slice(2,7,2)
print("a = np.arrange(10) 的结果为：",a)
print("s = slice(2,7,2) 的结果为：",slice(2,7,2))
print("a[s] 的结果为:",a[s])
print()

print("2.也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作：")
b = a[2:7:2]
print("b = a[2:7:2] 的结果为： ",b)
print("b = a[5]的结果为：",a[5])
print("b = a[2:]的结果为：",a[2:])
print()

print("3.多维数组的切片同样适用")
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print("np.array([[1,2,3],[3,4,5],[4,5,6]])的结果为：")
print(a)
print("a[1:]的结果为：",a[1:])
print()

print("4.切片中使用省略号")
print("a的内容是：")
print(a)
print("a[...,1]的结果为：",a[...,1])
print("a[1,...]的结果为：",a[1,...])
print("a[...,1:]的结果为：")
print(a[...,1:])
print()

print("五、NumPy广播(Broadcast)")
print("1.如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同")
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print("a = np.array([1,2,3,4])")
print("b = np.array([10,20,30,40])")
print("a * b = ",c)
print()

print("2.当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制")
a = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
b = np.array([1,2,3])
c = a + b
print("a = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])")
print("b = np.array([1,2,3])")
print("a + b 的结果是：")
print(c)
print()

print("六、NumPy迭代数组")
a = np.arange(6).reshape(2,3)
print("原数组是：")
print(a)
print("\n")
print('迭代输出元素：')
for x in np.nditer(a):
    print(x,end='\ ')
print('\n')
print()

print("七、数组操作")
print("1.修改数组形状")
print("1) numpy.reshape(arr,newshape,order='C'")
a = np.arange(8)
print("原始数组：")
print(a)
b = a.reshape(4,2)
print('执行reshape(4,2)后的数组：')
print(b)
print()

print("2) numpy.ndarray.flat数组迭代器")
a = np.arange(9).reshape(3,3)
print('原始数组：')
for row in a:
    print(row)
print('迭代后的数组：')
for element in a.flat:
    print(element)
print()

print("3) numpy.ndarray.flatten 返回数组拷贝，不影响原数组")
a = np.arange(8).reshape(2,4)
print('原数组：')
print(a)
print('展开的数组a.flatten：')
print(a.flatten())
print()
print('以 F 风格顺序展开的数组：')
print(a.flatten(order = 'F'))
print()

print("4) numpy.ravel展开的数组元素，顺序通常是'C风格',返回的是数组视图，修改会影响原数组")
a = np.arange(8).reshape(2,4)
print('原数组：')
print(a)
print('a.ravel()后',a.ravel())
print('以F风格顺序调用avel函数后：')
print(a.ravel(order='F'))
print()

print("2.翻转数组")
print("1)numpy.transpose(arr,axes)对换数组的维度")
a = np.arange(12).reshape(3,4)
print('原数组：')
print(a)
print('np.transpose(a)对换数组后：')
print(np.transpose(a))
print()

print("2)numpy.ndarray.T对换数组的维度与numpy.transpose类似")
a = np.arange(12).reshape(3,4)
print('原数组：')
print(a)
print('a.T转置数组后：')
print(a.T)
print()

print("3)numpy.rollaxis向后滚动特定的轴到一个特定的位置")
a = np.arange(8).reshape(2,2,2)
print('原数组：')
print(a)
print("执行np.rollaxis(a,2)后：")
print(np.rollaxis(a,2))
print()
print("执行np.rollaxis(a,2,1)后：")
print(np.rollaxis(a,2,1))
print()

print("4)numpy.swapaxes 函数用于交换数组的两个轴")
a = np.arange(8).reshape(2,2,2)
print('原数组：')
print(a)
print("执行np.swapaxes(a,2,0)后：")
print(np.swapaxes(a,2,0))
print()

print("3.修改数组维度")
print("1)numpy.broadcast将一个数组广播到另一个数组")
x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
print("x=[[1],[2],[3]]")
print("y=[4,5,6]")
print()
print("对y广播x b=n.broadcast(x,y)")
b = np.broadcast(x,y)
print("b拥有iterator属性，基于自身组件的迭代器元组")
r,c = b.iters
counter = 0
while counter<9:
    print(next(r),next(c))
    counter += 1
print()

print('广播对象的形状：')
print(b.shape)
print()

print("手动使用broadcast蒋x与y相加：")
b = np.broadcast(x,y)
c = np.empty(b.shape)
print(c.shape)
print()
c.flat = [u+v for (u,v) in b]

print('调用flat函数：')
print(c)
print()

print("x与y的和：")
print(x+y)
print()
print("……")
print()

print("4.连接数组")
print("1)numpy.concatenate()沿指定轴连接相同形状的两个或多个数组")
a = np.array([[1,2],[3,4]])
print('第一个数组：')
print(a)
b = np.array([[5,6],[7,8]])
print('第二个数组：')
print(b)
print('沿轴0连接两个数组：')
print(np.concatenate((a,b)))
print('沿轴1连接两个数组：')
print(np.concatenate((a,b),axis=1))
print()

print("5.分割数组")
print("1)numpy.split(ary,indices_or_sections,axis)")
a = np.arange(9)
print('第一个数组：')
print(a)
print('np.split(a,[4,7])将数组在一维数组中表明的位置分割：')
b = np.split(a,[4,7])
print(b)
print('原数组不变')
print(a)
print()

print('6.数组元素的添加与删除')
print('1)numpy.resize返回指定形状的新数组')
a = np.array([[1,2,3],[4,5,6]])
print('第一个数组：')
print(a)
print('第一个数组的形状：')
print(a.shape)
print('执行np.resize(a,(3,2))后：')
b = np.resize(a,(3,2))
print('第二个数组：')
print(b)
print('第二个数组的形状：')
print(b.shape)
print('修改第二个数组的大小b=np.resize(a,(3,3))：')
b = np.resize(a,(3,3))
print(b)
print()
print('修改第二个数组的大小b=np.resize(a,(4,3))：')
b = np.resize(a,(4,3))
print(b)

print('修改第二个数组的大小b=np.resize(a,(3,4))：')
b = np.resize(a,(3,4))
print(b)
print()

print('7.NumPy位运算')
print('1）numpy.bitwise_and对数组中整数的二进制形式执行位与运算')
print('13和17的二进制形式：')
a,b = 13,17
print(bin(a), bin(b))
print('13和17的位与：')
print(np.bitwise_and(13,17))
print()

print('8.NumPy字符串函数')
print('1)numpy.char.add连接两个字符串')
print("连接两个字符串np.char.add(['hello'],['xyz'])")
print(np.char.add(['hello'],['xyz']))
print()

print('9.NumPy数学函数')
print('1)三角函数sin(),cos(),tan()')
a = np.array([0,30,45,60,90])
print('打印角度的数组(通过乘pi/180转化为弧度)：')
print(a)
print()
print('数组中角度的正弦值：')
print(np.sin(a*np.pi/180))
print('数组中角度的余弦值：')
print(np.cos(a*np.pi/180))
print('数组中角度的正切值：')
print(np.tan(a*np.pi/180))



      










             



