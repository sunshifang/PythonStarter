import builtins
import os

dir(builtins)
print('导入的外部模块 bulitins 的内容是: {}'.format(builtins))

#for i in builtins:
#    print(i)

print('*********修改全局变量,要用local声明后才能有效访问到***********')
num = 1
def fun1():

    global num
    print('函数内打印global num => {}'.format(num))
    
    num = 123
    print('函数内打印local num => {}'.format(num))

    

fun1()
print('全局打印 num => {}'.format(num))
print('**********************************')
print()

print('*********修改嵌套作用域变量(内层修改外层),要用nonlocal声明后才能有效访问到***********')
def outer():
    num = 10
    def inner():
        nonlocal num
        print('内层函数打印nonlocal num => {}'.format(num))
        num = 100
        print('内层函数打印local num => {}'.format(num))
    inner()
    print('外层函数打印 num => {}'.format(num))
    
outer()
