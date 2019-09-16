import sys
import math
import pickle
import pprint


'''
str = input('请输入：')
print('你输入的内容是：{0}'.format(str))
print('你输入的内容是：%s'%str)
'''
print()

print('以下实例将字符串写入到文件 foo.txt 中：')
f = open("tmp/foo1.txt",'w')
f.write('Python 是一个非常好的语言。\n是的，的确非常好!!\n')
f.close()
f = open('tmp/foo.txt','r')
str = f.read()
print("读到foo.txt文件内容:\n%s"%str)
print()
print('f.readline() 会从文件中读取单独的一行')
f.seek(0,0)
str = f.readline()
print(str)
print()

print('f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。')
print(f.tell())
print()

print('f.readlines() 将返回该文件中包含的所有行')
f.seek(0)
str = f.readlines()
print(str)
print()

print('使用pickle模块将数据对象保存到文件')
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('tmp/data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)
output.close()
print()

print('#使用pickle模块从文件中重构python对象')
pkl_file = open('tmp/data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()




