tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup3 = 'a', 'b', 'c', 'd'

print("可以这样定义元组：tup3 = 'a', 'b', 'c', 'd'")
print("print(tup3)的结果是：",tup3)

print("************* 01.访问元组 **************")
print("tup1[0]: ",tup1[0])
print("tup2[1:5]: ",tup2[1:5])


print("************* 02.修改元组 **************")
#tup1[0]="baidu"
del tup1[0]
print(tup1)
