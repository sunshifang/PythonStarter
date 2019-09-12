
a = [66.25, 333, 333, 1, 1234.5]
print("#定义变量")
print("a = [66.25, 333, 333, 1, 1234.5]")
print()
print("a.count(333) ==> ", a.count(333))
print("a.count(66.25) ==> ", a.count(66.25))
print("a.count(x) ==> ", a.count('x'))
print()
a.insert(2,-1)
a.append(333)

print("a.insert(2,-1)")
print("a.append(333)")
print("执行inset和append操作后a的值为：")
print(a)

a.index(333)
print("a.index(333)")
print("执行a.index(333)操作后a的值为：")
print(a)

a.remove(333)
print("a.remove(333)")
print("执行a.remove(333)操作后a的值为：")
print(a)

a.reverse()
print("a.reverse()")
print("执行a.reverse()操作后a的值为：")
print(a)

a.sort()
print("a.sort()")
print("执行a.sort()操作后a的值为：")
print(a)
print()
print("*****列表推导式******")
vec = [2, 4, 6]
print("vec = [2, 4, 6]")
print("执行[3*x for x in vec]后：",[3*x for x in vec])
print("执行[[x,x**2] for x in vec]后：",[[x,x**2] for x in vec])
print()
print("******对序列里的每一个元素逐个调用某方法******")
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']")
print("执行[weapon.strip() for weapon in freshfruit]后")
print([weapon.strip() for weapon in freshfruit])
print("可以用 if 子句作为过滤器")
print("执行[3*x for x in vec if x > 3]后：",[3*x for x in vec if x > 3])
print("执行[3*x for x in vec if x < 2]后：",[3*x for x in vec if x < 2])

print("*****其他技巧*****")
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([(x*y) for x in vec1 for y in vec2])
print()

print("字典的遍历技巧")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print()
print("在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print()

print("同时遍历两个或更多的序列，可以使用 zip() 组合：")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
print()

print("要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：")
for i in reversed(range(1, 10, 2)):
    print(i)
print()

print("按顺序遍历，使用sorted()")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


