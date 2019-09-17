import sys

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
print()

print("类的方法")
class people:
    
    name = ''
    age = 0
    __wight = 0
    
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s 说：我%d 岁。'%(self.name,self.age))

p = people('runoob',10,30)
p.speak()
print()

print("类的继承--单继承")
class student(people):
    
    grade = ''
    
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g

    def speak(self):
        print('%s 说：我 %d 岁了，我在读 %d 年级'%(self.name,self.age,self.grade))

s = student('ken',10,60,3)
s.speak()
print()

print("类的继承--多继承")
class speaker():
    topic = ''
    name = ''

    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫 %s, 我是一个演说家，我演讲的主题是 %s'%(self.name,self.topic))

class sample(speaker,student):
    
    a = ''

    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample('Tim',25,80,4,'Python')
test.speak()
print()

print("方法重写")
print("super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法")
class Parent:
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):
    def myMethod(self):
        print('调用子类方法')

c = Child()
c.myMethod()
super(Child,c).myMethod()
'''
如此调用报错
super().myMethod()
'''
print()

print("运算符重载")
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print('v1 + v2 = {}'.format((v1 + v2)))



        
