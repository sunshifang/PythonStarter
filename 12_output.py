import sys
import math

s = 'Hello Python！'
print("s = 'Hello Python！'")
print("str(s): ",str(s))
print("repr(s): ",repr(s))
print("str(1/7): ",str(1/7))
print("repr(1/7): ",repr(1/7))
print()

x = 10 * 3.25
y = 200 * 200
s = 'x的值为： ' + repr(x) + ', y的值为： ' + repr(y) + '...'

print("x = 10 * 3.25")
print("y = 200 * 200")
print("s = 'x的值为： ' + repr(x) + ', y的值为： ' + repr(y) + '...'")
print(s)
print()

print(" #  repr() 函数可以转义字符串中的特殊字符")
hello = 'hello python\n'
hellos = repr(hello)
print("hello = 'hello python\n'")
print("hellos = repr(hello)")
print("print(hellos)",hellos)
print()

print("# repr() 的参数可以是 Python 的任何对象")
print(repr((x, y, ('Google', 'Runoob'))))
print()

print("两种方式输出一个平方与立方的表")
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
print()

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
print()
print('str.format() 的基本使用如下')
print('{}网址："{}!"'.format('菜鸟教程','www.runoob.com'))

print()
print("位置及关键字参数可以任意的结合:")
print("print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))")
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print()

print("可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：")
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
print()

print('在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。')
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10}==> {1:10d}'.format(name,number))
print()

print('如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。')
#table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print()

print('旧式字符串格式化')
print('常量 PI 的值近似为：%5.3f.'% math.pi)

