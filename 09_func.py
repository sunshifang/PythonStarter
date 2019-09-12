def area(width, height):
    # 计算面积函数
    return width * height

def print_welcome(name):
    print("Welcome",name)


#调用函数
print_welcome("Runoob")
print("width = 4, height = 5, area = ",area(4,5))

print("******** 传递不可变对象实例 *******")
def changeInt(a):
    a = 10
    print("函数内取值：",a)

b = 2
changeInt(b)
print ("函数外取值: ", b)
print()

print("******** 传递可变对象实例 *******")
def changeMe(myList):
    "修改传入的列表"
    myList.append([1,2,3,4])
    print("函数内取值：",myList)
    return

myList = [10,20,30]
changeMe(myList)
print ("函数外取值: ", myList)
print()

print("******** 不定长参数_元组 *******")

def printInfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vartuple)

printInfo(70, 60, 50)
print()

print("******** 不定长参数_字典 *******")

def printInfo1(arg1, **vardict):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vardict)

printInfo1(70, a=60, b=50)
printInfo1(1,a=2,b=3,c=4)
print()

print("******** 匿名函数 *******")
