import numpy as np

print('1. 使用标量类型')
print('执行 np.dtype(np.int32) 的结果：')
dt = np.dtype(np.int32)
print(dt)
print()

print("2. int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替")
print("执行 p.dtype('i4') 的结果为：")
dt = np.dtype('i4')
print(dt)
print()

print("3. 字节顺序标注")
print("执行 np.dtype('<i4') 结果为：")
dt = np.dtype('<i4')
print(dt)
print()

print("4. 创建结构化数据类型")
print("执行 np.dtype('<i4') 结果为：")
dt = np.dtype([('age',np.int8)])
print(dt)
print()

print("5. 将数据类型应用于 ndarray 对象")
print("执行 np.array([(10,),(20,),(30,)], dtype = dt) print(a['age'])")
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])
print()

print("6. 类型字段名可以用于存取实际的 age 列")
print("执行 np.array([(10,),(20,),(30,)], dtype = dt) 结果为：")
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)
print()

print("7. dtype可以是结构化数据类型")
print("执行 np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])  结果为：")
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)
print()


student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
