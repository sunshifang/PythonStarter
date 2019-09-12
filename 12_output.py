import sys

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
    print(repr(
