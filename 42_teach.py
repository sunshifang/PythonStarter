print("一、数据类型")

print("01.整数")
print("整数有两种表示方法：")
print("·常规的数学方法")
print("·16进制方法，前面加0x")
print("")

print("02.浮点数(小数)")
print("浮点数也有两种表示方法：")
print("·数学写法")
print("·科学计数法")
print("整数永远是精确的，而浮点数可能有四舍五入的误差")
print("")

print("03.字符串")
print("\'\'或\"\"是字符串的表示方式，不是字符串的一部分，要想显示\'或\",要使用转义符\\.")
print("如果字符串里面有很多字符都需要转义，就需要用很多\\，为了简化，Python允许\n用r\'\'表示\'\'内部的字符串默认不转义")
print(r"\\\t\\的结果是",'\\\t\\')
print(r"r'\\\t\\'的结果是",r'\\\t\\')
print("如果字符串内有很多换行，用\\n写在一行里不好阅读，为了简化，Python还允许\n用",r"'''...'''的格式表示多行。")
print("例如：")
print(r"print('''line1")
print(r"line2")
print(r"line3''')")
print("的结果如下：")
print('''line1
line2
line3''')
print("")

print("04.布尔值")
print('''布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，
要么是True,要么是False。在Python中可以直接用True或False,要注意大小写。
布尔值可以用and、or或not运算。布尔值经常用在条件判断中。''')
print("")

print("05.空值")
print('''
空值是Python里的一个特殊的值，用None表示。None不能理解为0,因为0是有意义的，
而None是一个特殊的空值。
此外，Python还提供了列表、字典的多种数据类型，还允许创建自定义的数据类型。
''')

print('''
06. 变量
    变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅
可以是是数字，还可以是是任意数据类型。
    变量在程序中就是用一个变量名表示了，命名规则与其他语言相同。
    在Python中，等会=是赋值语句，不同于Basic，不能用于判断是否相等。
    可以把任意数据类型赋值给变量，同一个变量是可以反复赋值，而且可以是不同类型
的变量
a  = 123 #a是整数
print(a)
a = 'ABC' #a变为字符串
print(a)
程序执行输出的结果是：
''')

a  = 123 #a是整数
print(a)
a = 'ABC' #a变为字符串
print(a)
print("")

print('''
这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义
变量是必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
理解变量在计算机内存中的表示也非常重要。
a = "ABC"
Python解释器做了两件事情：
1.在内存中创建已了一个'ABC'的字符串；
2.在内存中创建月一个名为a的变量，并吧它指向'ABC'
也可以再创建一个变量b，把b指向a的变量
a = 'ABC'
b = a
a = 'XYZ'
print(b)  #结果应该是XYZ
''')
a = 'ABC'
b = a
a = 'XYZ'
print(b)  #结果应该是XYZ？
print("")

print('''
06.常量
所谓常量就是不能改变的变量，但Python根本没有任何机制保证常量不被改变，只是用
大写字符表示常量，靠程序员来保证的。

07.小结
Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个对象，而变量就
是在程序中指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
对变量赋值x = y 是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y
的赋值不影响变量x的指向。
注意：Python的整数和浮点数都没有大小限制但是超过一定的范围就表示为inf(无限的)
''')
print("")

print("二、字符串和编码")
print('''
01. 字符编码
    因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字。最早的
计算机在设计时采用8个比特(bit)作为一个字节(byte)，所以，一个字节能表示的最大
的整数就是255(二进制11111111=十进制255)，如果要表示更大的整数，就必须采用更多
的字节。比如两个字节可以表示的最大整数是65535, 而4个字节可以表示的最大整数是
4294967295.
    由于计算机是美国人发明的，因此，最早只有127个字符被编码在计算机里，也就是
只有大小写英文字母、数字和一些符号，这个编码表被称为ASCii编码，比如字母A的编码
是65，小写字母z的编码是122
    但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII
编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。
    全世界有上百种语言，日本把日文编到Shif_JIS里，韩国把韩文编到Euc-kr里，各
国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示
出来会有乱码。
    因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再
有乱码问题了。
    Unicode标准也在不断发展，但最常用的是两个字节表示一个字符(如果要用到非常
偏僻的字符，就需要4个字节)。现代操作系统和大多数编程语言都直接支持Unicode.
    现在捋一捋ASCII编码和Unicode编码的区别：ASCII编码1个字节，Unicode通常2字节
    字母A用ASCII编码是十进制65，二进制的01000001；
    字符0用ASCII编码是十进制48，二进制的00110000，注意字符'0'和整数0是不同的；
    汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制编码
的01001110 00101101
    你可以猜测，如果把ASCII编码的A用Unicode编码，乱码问题从此消失了。但是，如果
你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，
在存储和传输上就十分不划算。
    所以，本着节约的精神，又出现了把Unicode的编码转化为“可变长编码”的UTF8编码
UTF8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码
成一个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要
传输的文本包含大量英文字符，用UFT8编码就能节省空间
字符   ASCII      Unicode              UTF-8
A      01000001   00000000 01000001    01000001
中     X          01001110 00101101    11100100 10111000 10101101
从上面的表格还可以发现，UTF8编码有一个额外的好处，就是ASCII编码实际上就可以被看
成是UTF8的一部分，所以，大量支持ASCII编码的历史遗留软件可以在UTF8编码下继续工作。
    在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就
转换为UTF8编码。
    用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑
完成后，保存的时候再把Unicode转换为UTF8保存到文件。
    浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF8再传输到浏览器，所以
我们看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页用的
是UTF8编码。

02. Python字符串
    在最新的Python3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持
多语言
    对于单个字符的编码，Python提供了ordi获取字符的整数表示，chr()函数把编码
转换为对应的字符
''')
print("ord('A')=",ord('A'))
print("ord('中')=",ord('中'))
print("chr(66)=",chr(66))
print("chr(25991)=",chr(25991))
print('''
如果知道字符的整数编码，还可以用十六进制''')
print(r"'\u4e2d\u6587'=",'\u4e2d\u6587')
print('''
由于Python的字符串类型是str,在内存中以Unicode表示，一个字符对应若干个字节。如果
要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes.
Python对bytes类型的数据用带b前缀的单引号或双引号表示 x = b'ABC'。
要注意区分'ABC'和b'ABC',前者是str,后者虽然内容显示和前者一样，但bytes的每个字符都
只占用一个字节。
以Unicode表示的str通过encode()方法可以编码为指定的bytes,例如：''')
print("'ABC'.encode('ascii')=",'ABC'.encode('ascii'))
print("'中文'.encode('utf-8')=",'中文'.encode('utf-8'))
print('''
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes，要把bytes变为
str，就需要用decode()方法：''')
print("b'ABC'.decode('ascii')=",b'ABC'.decode('ascii'))
print(r"b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')=",b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print('''
如果bytes中包含无法解码的字节，decode()方法会报错。
中文无法编码为ascii码，因为中文的编码范围超过了ASCII编码的范围，Python会报错。
如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误字节。''')
print("b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')=",b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
print("要计算str包含多少个字符，可以用len()函数：")
print("len('ABC')=",len('ABC'))
print("len('中文')=",len('中文'))
print("len(b'ABC')=",len(b'ABC'))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87')=", len(b'\xe4\xb8\xad\xe6\x96\x87'))
print("len('中文'.encode('utf-8'))=",len('中文'.encode('utf-8')))
print('''
可见，1个中文经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用一个字节。
在操作字符串时，我们经常遇到str和bytes的相互转换。为了避免乱码问题，我们应当
始终坚持使用UTF-8编码对str和bytes进行转换。
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存
源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它
按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
第一行注释告诉Linux/OS X系统这是一个Python可执行程序，Windows系统忽略该注释。
第二行注释告诉Python解释器，按照utf-8编码读取源代码，否则，你在源代码中写的
中文输出可能会有乱码。
声明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑
器使用UTF-8 without BOM编码

03. 格式化
采用的格式化方式和C语言是一致的，用%实现，常见的占位符有：
占位符   替换内容
%d       整数
$f       浮点数
%x       十六进制数
%s       字符串   
只有一个占位符，括号可以省略
%s永远起作用，它会把任何数据类型都转换为字符串。
转义符是%
'Age: %s, Gender: %s' % (25,True)

04. format()
字符串的format()方法，用传入的参数依次替换字符串内的占位符{0}、{1}……
'Hello, {0},成绩提升了 {1:.1f}%'.format('小明',17.125)
''')

print("三、使用list和tuple")
print('''
01. list
list是一种有序的集合，可以随时添加和删除其中的元素。
classMates = ['Michael','Bob','Tracy']
print(classMates)
len(classMates)
classMates[0]
classMates[1]
classMates[-]

''')
classMates = ['Michael','Bob','Tracy']
print(classMates)
print("len(classMates)=",len(classMates))
print("classMates[0]=",classMates[0])
print("classMates[1]=",classMates[1])
print("classMates[-]=",classMates[-1])
print('''
list是一个可变的有序表，所以，可以往list中追加元素到末尾:list.append()
也可以把元素插入到之地的位置，比如索引号为1的位置：list.inert(1,'Jack')
要删除list末尾的元素，用pop()方法
要删除指定位置的元素，用pop(i)方法，其中i是索引位置。
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置。
list里面的元素的数据类型也可以不同。
list元素也可以是另一个list,类似于二维数组。
如果list中一个元素也没有，就是一个空的list,他的长度为0。

02. tuple
元组一种不能修改的有序列表，一旦初始化，就不能修改，它也没有append()
和inert()这样的方法，能通过下标访问元素，但不能修改元素。
因为tuple不可变，所以代码就更安全。
只有一个元素的tuple定义时必须加一个逗号，来消除tuple()和数学公式中的
小括号，Python在显示只有一个元素的tuple时，也会加一个逗号，以免你误解
成数学计算意义上的括号。
如果元组的元素是list，那么list的元素是可以修改的。
''')
l = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(l)
print(l[0][0])
print(l[1][1])
print(l[2][2])
print("")

print("四、条件判断")
print("计算机之所以能做很多自动化的任务，因为它可以自己做条件判断")
print('''if语句的完整形式：

if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的不执行

if判断条件还可以简写：
if x:
    print('True')
只要x是非零数值、非空字符串、非空list等，就判断为True, 否则为False

五、循环
01. Python的循环有两种：
一种是for...in循环，依次把list或tuple中的每个元素迭代出来，对序列数
的迭代可使用range函数来生成list。
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出。
break可以提前退出循环
continue跳过当前的这次循环，直接开始下一次循环。
尽量少用break和continue,用循环条件或者循环逻辑来实现。
ctrl + c退出程序。

02. dict
使用键值对存储，具有极快的查找速度。
例如，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个
names = ['Michael','Bob','Tracy']
scores = [95, 75, 85]
给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从
scores取出对应的成绩，list越长，耗时越长。
如果用dict实现，只需要一个"名字"--"成绩"的对照表，直接根据名字查找
成绩，无论这个表有多大，查找速度都不会变慢。
''')
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print("d['Bob']=",d['Bob'])
print('''
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设
字典包含一万个汉字，我们要查某一个字，一个办法是从前往后翻，直到找
到为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里(比如部首表)查这个字对应的页码，然后
直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会
随着字典大小的增加而变慢。
dict就是第二种实现方式，给定一个名字，比如'Bob'，dict在内部就可以
直接计算出Bob对应的存放成绩的“页码”，也就是75这个数字存放的内存
地址，直接取出来，所以速度非常快。
你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出
value的存放位置，这样，取的时候才能根据key直接拿到value.
把数据放入dict的方法，除了初始化时指定外，还可以通过key放入。
由于一个key只能对应一个value，所以，多次对一个key放入value，后面的
值会把前面的值覆盖掉。如果key不存在，dict就会报错。
有两种方法判断key是否存在：
一种通过in判断 'Thomas' in d
另一种是通过dict提供的get()方法，如果key不存在，可以返回None,或者
自己制定的value（注意：返回None的时候，Python交互环境不显示结果)
要删除一个key, 用pop(key)方法，对应的value也会从dict中删除。
请务必注意，dict内部存放的顺序和key放入的顺序没有关系，和list比较，
dict有以下几个特点：
·1、查找和插入的速度极快，不会随着key的增加而变慢；
·2、需要占用大量的内存，内存浪费多。
而list相反：
·1、查找和插入的时间随着元素的增加而增加；
·2、占用空间小，浪费内存少。
所以，dict是用空间换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python的代码中几乎无处不在，
正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出
的结果不同，那dict的内部就完全混乱了。通过这个key计算的算法称为“哈
希算法(hash)”
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数
等都是不可变的，因此，可以放心的作为key。而list是可变的，就不可以。

03. set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，
所以，在set中，没有重复的key.
要创建一个set,需要提供一个list作为输入集合：''')
s = set([1,2,3])
print(s)
print('''
注意，传入的参数[1,2,3]是一个list，而显示的{1,2,3}只是告诉你这个set
内部又1,2,3这3个元素，显示的顺序也不表示set是有序的。重复元素被过滤。
''')
s=set([1,1,2,2,3,3])
print("s = set([1,1,2,2,3,3])")
print("s = ",s)
print('''
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
通过remove(key)可以删除元素
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学
意义上的交集、并集等操作''')
s1 = set([1,2,3])
s2 = set([2,3,4])
print("s1 = set([1,2,3])")
print("s2 = set([2,3,4])")
print("s1 & s2 = ",s1 & s2)
print("s1 | s2 = ",s1 | s2)
print('''
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法
保证set内部"不会有重复元素"。
set.add(list)会报错unhashable type: 'list'
classMates = ['Michael','Bob','Tracy']
s1 = set(classMates)
print(s1)
s1.add(classMates)  #unhashable type: 'list'
#print(s1)

04. 再议不可变对象
对应不可变对象，比如list，对list进行操作，list内部的内容是会变化的，如：
a = ['b','c','a']
a.sort()
print（a)
a = ['a','b','c']
而对应不可变对象，比如str，对str进行操作
a = 'abc'
print(a.replace('a','A'))
Abc
print(a)
abc
要牢记的是，a是变量，而'abc'才是字符串对象！
我们经常说的a的内容是abc，其实是指：a本身是一个变量，它指向的对象的内容
才是abc。
当我们调用a.replace('a','A')时，实际上方法replace是作用在字符串对象abc
上的，而这个方法没有改变字符串’abc‘的内容，而是创建并返回了一个新字符串
'Abc'，如果我们用变量b指向该新字符串，就容易理解了。
所以，对于不变对象来说，调用对象自身的任意方法，不会改变对象自身的内容，
这些方法会创建新的对象并返回，这样，就保证了不可变对象本身的不可变。

classMates = ['Michael','Bob','Tracy']
s1 = set(classMates)
print(s1)
#s1.add(classMates)  #unhashable type: 'list'
#print(s1)
s1.add((1,2,3))
print(s1)
s1.ad((1,[2,3]))
''')

print("六、函数")
print('''
当代码出现有规律的重复的时候，就要考虑使用函数。
01. 抽象
借助抽象，我们才能不关心底层的具体计算过程，而直接在更改层次上思考问题
写程序也是一样，函数就是最基本的一种代码抽象方式。
''')

print("七、调用函数")
print('''
Python内置了很多函数，可直接调用
01. 数据类型转换
函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，
相当于给这个函数起了一个别名
''')

print("八、定义函数")
print('''
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的
参数和冒号，然后在缩进块中写函数体，函数的返回值用return语句返回。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
return None 可以简写为 return
如果你已经把my_abs()函数定义保存在abstest.py文件了，那么，可以在该文件的
当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()
函数，注意，abstest是文件名(不含.py扩展名)

01. 空函数
如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
pass是占位符，没有或省略pass会报错。

02. 参数检查
定义函数时要注意检查参数的类型、个数甚至取值范围。

03. 返回多个值
可以返回一个tuple，在语法上返回一个tuple可以省略括号，而多个变量可以同时接收
一个tuple，按位置赋给对应的值。

04. 小结
·定义函数时，需要确定函数名和参数个数；
·如果有必要，可以先对参数的数据类型做检查；
·函数体内部可以用return随时返回函数结果；
·函数执行完毕没有return语句时，自动return None
·函数可以同时返回多个值，但其实就是一个tuple.
''')

print("九、函数的参数")
print('''
定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于
函数调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，
函数内部的复杂逻辑别封装起来，调用者无需了解。
Python函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用
默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，
还可以简化调用者的代码。

01. 位置参数
调用函数时，传入参数位置顺序要正确。

02. 默认参数
默认参数可以简化函数调用，设置默认参数时要注意几点
一是必选参数在前，默认参数在后
二是变化小的参数设置为默认参数
三是默认参数必须指向不变的对象
不变对象的好处：
可以减少由于修改数据导致的错误
多任务环境下同时读取对象不需要加锁，

03. 可变参数(参数的个数是可变的)
允许传入0个或任意个参数，在函数调用时自动组装为tuple,传入list或tuple,并且在前面加*

04. 关键字参数
允许传入0个或任意个参数名的参数，这些关键字参数在函数内部自动组装为dict，前面加**

05. 命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数。没有可变参数时加*号，否则不加

06. 参数组合
各种参数可以组合使用，定义顺序必须是必须、默认、可变、命名关键字、关键字参数。

07. 小结
·Python的函数灵活，即可简单调用，也可传入复杂的参数
·默认参数一定要有不可变对象，如果是可变对象，程序运行时会有逻辑错误。
·要注意可变参数和关键字参数的语法：
  *args是可变参数，args结收的是一个tuple;
  **kw 是关键字参数，kw接收的是一个dict
·可变参数既可以直接传入，又可以先组装list或tuple，再通过*args插入
·关键字参数既可以直接传入，也可以先组装dict,通过**kw传入
·使用*args和**kw是Python的习惯写法，推荐使用
·命名的关键字参数是为了限制调用者可以传入的参数名同时可以提供默认值。
·定义命名的关键字参数在没有可变参数的情况下，不要忘了写分隔符。
''')

print("十、递归函数")
print('''
如果一个函数在内部调用自身，这个函数就是递归函数。
过深的调用会导致栈溢出
''')

print("十一、高级特性")
print('''
01. 切片代替循环取n个数据
02. 迭代代替循环输出
03. 列表生成式"
[x * x for x in range(1,11) if x % 2 == 0]
在方括号中，要生成的元素放在前面，后面跟for循环，循环后可以加判断
还可以使用两层循环，可以生成全拍列
[m + n for m in 'ABC' for n in 'XYZ']
运用列表生成式可以写出非常简洁的代码。
例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
''')

import os
print([d for d in os.listdir('.')])

print("for循环可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代kye和value")
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
    print(k,"=",v)

#d = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k, v in d.items()])
print("")

print("把一个list中的所有字符串变成小写")
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print([s.upper() for s in L])
print("")

print("isinstance函数可以判断一个变量是不是字符串")
x='abc'
y=123
print(isinstance(x,str))
print(isinstance(y,int))
      
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s,str)])
#print([s.upper() for s in L1])

print('''
运用列表生成式，可以快速生成list，可以通过已list推出另一，代码简洁

04. 生成器generator
通过列表生成式，我们可以直接创建一个列表，但是受到内存限制，列表容量
肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存
储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的
空间都白白浪费了。所以，如果列表元素可以按照某种算法推算出来，那我们
是否可以在循环过程中不断推出后续元素呢？这样就不必创建完整的list,从而
节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器
要创建一个generator,有很多种方法。第一种方法很简单，只要把一个列表生
成式的[]改成(),就创建了一个generator:
''')
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)
    
i=0
g = (x * x for x in range(10))
while i<10:
    print(next(g))
    i=i+1
    
print('''
generator非常强大，如果推算的算法比较复杂，用类似列表生成式的for循环
无法实现的时候，还可以用函数来实现。
''')

def fib(max):
    n,a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n +1
    return 'done'

print(fib(6))

print('''
创建generator的第二种方法是创建含有yield关键字的函数
def fib(max):
    n,a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n +1
    return 'done'

这里最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到
return语句或者最后一行就返回。而generator函数，在每次调用next()的时候执
行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
''')

def fib(max):
    n,a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n +1
    return 'done'

print(fib(6))
g = fib(6)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('''
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator,
也可以通过函数实现复杂逻辑的generator。要理解generator的工作原理，它是在for
循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成
generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束gengertor
的指令，for循环随之结束。

05. 迭代器
可以直接作用于for循环的数据类型有以下几种：
集合数据类型：list, tuple, dict, set, str等；
generator类型：生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象Iterable.
可以使用isinstance()判断一个对象是否是Iterable对象
而生成器不单可以作用于for循环，还可以被next()函数不断调用并返回下一个值。直到
最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator.
生成器都是Iterator对象，但list, dict, str虽然是Iterable, 却不是Iterator
把list, dict, str等Iterable变成Iterator可以使用iter()函数
''')

from collections.abc import Iterable
from collections.abc import Iterator
print("isinstance([],Iterable) = ",isinstance([],Iterable))
print("isinstance({},Iterable) = ",isinstance({},Iterable))
print("isinstance('abc',Iterable) = ",isinstance('abc',Iterable))
print("isinstance((x for x in range(10)),Iterable) = ",isinstance((x for x in range(10)),Iterable))
print("isinstance(100,Iterable) = ",isinstance(100,Iterable))
print("isinstance([],Iterator) = ",isinstance([],Iterator))
print("isinstance(iter([]), Iterator)",isinstance(iter([]), Iterator))
print("isinstance('abc',Iterator) = ",isinstance('abc',Iterator))
print("isinstance(iter('abc'), Iterator)",isinstance(iter('abc'), Iterator))

print('''
为什么list, dict, str等数据类型不是Iterator?
因为Python的Iterator对象表示一个数据流，Iterator对象可以被next()函数调用并不断
返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个
有序序列，但我们却不能提前知道序列的长度，只能通过next()函数实现按需计算下一个
数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能
存储全体自然数的。

小结
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算序列；
集合数据类型如list, dict, str等是Iterable但不是Iterator, 可以用iter()函数转换
Python的for循环本质上就是不断调用next()函数实现的。
''')

print("十三、函数式编程")
print('''
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数
调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。
函数是面向过程的程序设计的基本单元。
而函数式编程--Functional Programming，虽然也可以归结到面向过程的程序设计，但其
思想更接近数学计算。
我们首先要搞明白计算机(Computer)和计算(Compute)的概念。
在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所
以，汇编语言是最贴近计算机的语言。
而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。
对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C
语言；越高级的语言，月贴近计算，抽象程度高，执行效率低，比如Lisp语言。
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量
因此，任意一个函数，只要输入时确定的，输出就是确定的，这种纯粹函数我们称之为没有
副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，统样的输入，
可能得到不同的输出。因此，这种函数是有副作用的。
函数式编程的一个特点是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python部分支持函数式编程。由于Python允许使用变量，不是纯粹的函数式编程语言。

01. 高阶函数
    1）变量可以指向函数
    函数本身也可以赋值给变量，即：变量可以指向函数
    f = abs
    f(-10) >>>10
    说明变量f已经指向了abs函数本身，直接调用abs()和调用f()完全相同
    2）函数名也是变量
    对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数
    >>> abs = 10
    >>> abs(-10)
    TypeError: 'int' object is not callable
    把abs指向10后，就无法通过abs(-10)调用该函数了！因为这个变量已经不指向求绝对值
    函数而是指向一个整数10！
    3）传入函数
    既然变量可以指向函数，函数的参数就能接收变量，那么一个函数就可以接收另一个函数
    作为参数，这种函数就称之为高阶函数。
    def add(x, y, f):
        return f(x) + f(y)

    add(-5, 6, abs)==>11
    编写高阶函数，就是让函数的参数能够接收别的函数。
    4）小结
    把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程

02. Python内建了map()和reduce()函数(并行处理大规模的数据)
    1）map()函数接受两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到
    序列的每个元素，并把结果作为新的Iterator返回。
    def add(x, y, f):
        return f(x) + f(y)
    print(add(-5, 6, abs))
    
    2）reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接受两个参数
    reduce把结果继续和序列的下一个元素做累积计算，其效果就是
    reduce(f, [x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
    比方说对一个序列求和，就可以用reduce实现：
''')

from functools import reduce

def add(x, y):
    return x + y

print("reduce(add,[1,3,5,7,9])=",reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x*10+y
print("reduce(fn,[1,3,5,7,9])",reduce(fn,[1,3,5,7,9]))

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

print("reduce(fn,map(char2num,'13579'))=",reduce(fn,map(char2num,'13579')))
print("")

print("整理成一个str2int的函数就是")
digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return digits[s]
    return reduce(fn,map(char2num,s))
print(str2int('12345'))

print("理用lambda函数进一步简化成")

digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
    return digits[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y,map(char2num,s))

print(str2int('354'))


print('''
03. filter
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数
依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

例如，在一个list中，删掉偶数，只保留奇数
''')
def is_odd(n):
    return n%2==1

a=list(filter(is_odd,[1,2,4,5,6,9,10,15]))
print(a)
print("")

print("删掉序列中的空字符串")
def not_empty(s):
    return s and s.strip()
a=list(filter(not_empty,['A','','B',None,'C','  ']))
print(a)
print("")

print("用filter求素数")

def _odd_iter():
    #生成无限序列的生成器
    n=1
    while True:
        n=n+2
        yield n
           
def _not_divisible(n):
    #筛选函数
    return lambda x: x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
'''
for n in primes():
    if n<1000:
        print(n)
    else:
        break
'''
print('''
小结
filter()的作用是从一个序列中筛选出符合条件的元素，由于filter()使用了惰性计算，所以只有在取
filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

04. sorted
01）排序算法
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较亮元素的大小。
如果是数字，我们可以直接比较，如果是字符串或两dict呢？直接比较数学上的大小时没有意义的，因此
比较的过程必须通过函数抽象出来。
Python内置的sorted()函数可以对list进行排序
sorted([36,5,-12,9,-21])
此外，sorted()函数也是一个高阶函数，它可以接收一个key函数来实现自定义的排序.
默认情况下，对字符串排序是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母
a的前面。给sorted传入key函数，可实现忽略大小写的排序：
''')
print("[36,5,-12,9,-21]")
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21],key=abs))
print("")

a = ['bob', 'about', 'Zoo', 'Credit']
print(a)
print("默认排序的结果：")
print(sorted(a))
print("忽略大小写的排序，传入key函数key=str.lower")
print(sorted(a,key=str.lower))
print("反向排序，传入第三个参数reverse=True")
print(sorted(a,key=str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#L2 = sorted(L)
#print(L2)
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
print("按name排序的结果如下：")
L2=sorted(L,key=by_name)
print(L2)
print("按成绩排序的结果如下：")
L2=sorted(L,key=by_score)
print(L2)
print("")

print('''
02.返回函数

01）函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
我们来实现一个可变求和的情况。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

但是，如果不需要立刻求和，而是在后面的代码中，根据需要在计算怎么办？
可以不返回求和结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

当我们调用lazy_sum()时，返回的并不是求和的结果，而是求和函数：
当我们调用f()时，才真正计算求和的结果。
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum
的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数值，这种称为"闭包
(Closure)"的程序结构拥有极大的威力。
还要注意，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即时传入相同的参数。
''')

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())

print("f1 = lazy_sum(1,3,5,7,9)")
print("f2 = lazy_sum(1,3,5,7,9)")
f2 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print("f1 == f2的结果是：",f1 == f2)
print("f1()和f2()的调用结果互不影响。")

print('''
02）闭包
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用才执行。例子如下：
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

在上面的例子中，每次循环，都创建了一个新的函数，然后，八创建的3个函数都返回了。
调用f1(), f2(), f3()结果都是9。原因在于返回的函数引用了变量i，但它并非立刻执行。
等到3个函数都返回时，他们引用的变量i已经变成了3，因此结果为9.

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量的当前
的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))  # f(i)立刻执行，因此i的当前值被传入f()
    return fs

小结
一个函数可以返回一个计算结果，也可以返回一个函数。
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

03. 匿名函数
当我们传入函数时，有些时候，不需要显式第定义函数，直接传入匿名函数更方便。
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义
一个f(x)的函数外，还可以直接传入匿名函数：
list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))
通过对比可以看出，匿名函数lambda x: x*x实际上就是
def f(x):
    return x*x

关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数
对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x*x
f(5)结果是 25

同样，也可以把匿名函数作为返回值返回，比如：
def build(x,y):
    return lambda: x*x + y*y

练习：
用匿名函数改造下面代码
def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd, range(1,20)))
改造后的代码如下：
L=list(filter(lambda n: n % 2 == 1, range(1,20)))
print(L)

Python对匿名函数的支持有限，只有一些简单情况下可以使用。
''')
L=list(filter(lambda n: n % 2 == 1, range(1,20)))
print(L)

a=list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]))
print(a)
a=list(map(lambda x: x*x,range(1,10)))
print(a)

print('''
04. 装饰器
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用函数。
函数对象有一个__name__属性，可以拿到函数的名字：
def now():
    print('2019-11-08')

f = now
f()
print(f.__name__)
print(now.__name__)

现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望
修改now()函数的定义，这种在运行期间动态增加功能的方式，称为"装饰器"(Decorator)。
本质是，decorator就是一个返回函数的高阶函数，所以，我们要定义一个能打印日志的
decorator,可以定义如下：
def log(func):
    def wrapper(#args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个参数。
我们要借助Python的@语法，把decorator置于函数的定义外：
有点儿难了，下次再说吧，应该很有用的！！！
def now():
    print('2019-11-08')

f = now
f()
print(f.__name__)
print(now.__name__)

05. 偏函数
Python的functools模块提供了很多有用的功能，其中一个就是偏函数(Partial function)。
要注意，这里的偏函数和数学意义上的偏函数不一样。通过设定函数参数的默认值，可以降低
函数调用的难度。而偏函数可以做到这一点。举例如下：
int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
int('12345') 的结果是 12345
但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制转换
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，
可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x,base)
    
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接
使用下面的代码创建一个新函数int2:
a=int('12345')
print("int('12345')=",a)
a=int('12345',base=8)
print("int('12345',base=8)=",a)
a=int('12345',base=16)
print("int('12345',base=16)=",a)
    
def int2(x, base=2):
    return int(x,base)
print(int2('1000000'))
print(int2('1010101'))
print("")

import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))

所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住(也就是
设置默认值)，返回一个新函数，调用这个新函数会更简单。

小结
当函数的参数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个
函数可以固定住原函数的部分参数，从而在调用时更简单。

十四、模块
在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来
越不好维护。
为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含
的代码就相对较少，很多编程语言都采用这种组织单的方式。在Python中，一个.py文件就称为
一个模块(module)。
使用模块的最大好处就是大大提高了代码的可维护性。其次，编写代码不必从0开始。当一个
模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括
Python内置的模块和来自第三方的模块。
使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的
模块中，因此，我们自己编写模块时，不必考虑名字会与其他模块冲突。但是也要注意，尽量
不要与内置函数名字冲突。
为了避免模块名冲突，Python又引入了按目录组织模块的方法，称为包(Package).
举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是xyz模块。
为了防止abc和xyz这两个模块名字与其他模块冲突，我们可以通过包来组织模块，方法是选择
一个顶层包名，比如mycomany，按如下目录存放：
mycompany
    __init__.py
    abc.py
    xyz.py
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py
模块的名字就变成了mycompany.abc，类似的，xyz.py就变成了mycompany.xyz
每一个包目录下都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把
这个目录当成普通目录，而不是一个包。
__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它
的模块名就是mycompany.
可以有多级目录，组成多级层次的包结构。比如如下的目录结构
mycompany
    web
        __init.py
        utils.py
        www.py
    __init.py
    abc.py
    utils.py

自己创建模块时要注意命名，不能和Python自带的模块名称冲突。否则无法导入系统的模块。

01. 使用模块
Python本身内置了很多非常有用的模块，只有安装完毕，就可以使用。
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

` a test module`

__authonr__='ssf'

import sys

def test():
    args = sys.argv
    if len(args==1:
        print('Hello, world!')
    elfi len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__='__main__':
    test()

第1行注释行，说明hello.py可以直接在Unix/Linux/Mac上运行
第2行注释行，文件本身使用标准UTF-8编码；
第4行字符串，表示模块的文档注释，任何模块代码的第一个支持都被视为模块的文档注释
第6行变量，__author__把作者写进去，开源时别人了解作者
以上时Python模块的标准文件模板，可以不写。

导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys的功能。
sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一
个参数永远是该文件的名称.
import sys

def test():
    args = sys.argv
    print("sys.argv[0]=%s" % sys.argv[0])
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!',args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

最后两行代码：
当我们在命令行运行模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令
行运行时执行一些额外代码，最常见的就是运行测试。

01）作用域
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有些仅在模块内部使用。在Python中，是通过"_"前缀来实现的。
正常的函数和变量名是公开的public,可以直接被引用，比如：abc，x123，PI等；
类似__xxx__这样的变量是特殊变量，可被直接引用，但是用途特殊，比如上面的__author__,
__name__,__doc__,我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的(private)，不应该被直接引用。
Python并没有一种方法可以完全限制访问private函数或变量，从编程习惯上不应该引用。

02. 安装第三方模块
通过包管理工具pip安装第三方模块

01）安装常用模块
推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，内置许多第三方库

02）模块搜索路径
默认情况下，Python解释器会搜索当前目录，所有已安装的内置模块和第三方模块，搜索路径
存放在sys模块的path变量中。
如果我们要添加自己的搜索目录，有两种方法：
一是直接修改sys.path，添加要搜索的目录
import sys
sys.path.append('/users/michaeal/my_py_scripts')
二是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式
与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python的搜索路径不受影响

''')
import sys

def test():
    args = sys.argv
    print("sys.argv[0]=%s" % sys.argv[0])
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!',args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting("sunshifang"))
print(_private_2("调用私有函数"))

print('''
十五、面向对象
面向对象编程--Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象
作为程序的基本单元，一个对象包含了数据和操作数据的函数。
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行，为了简化
程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块含量来降低系统
的复杂度。
而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象
发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象直接传递。
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型
计算面向对象中的类(class)的概念。
我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。
假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程用一个dict表示：
std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}
而处理学生的成绩可以通过函数实现，比如打印学生的成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种
数据类型应该被视为一个对象，这个对象拥有name和score这两个属性(Property)。如果要打
印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score
消息，让对象自己把自己的数据打印出来。
class Student(object):

    def __init__(self,name,scord):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法(Method).面向对象
的程序写出来如下：
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print)socre()

面向对象的设计思想是从自然界中来的，因为在自然界中，类(class)和实例(instance)的概念
是很自然的。Class是一种抽象概念，比如我们定义的Class --- Student，是指学生这个概念，
而实例(instance)则是一个个具体的Student，比如Bart Simpson和Lisa Simpson是两个具体的
Student。所以，面向对象的设计思想是抽象出Class, 根据Class创建Instance.
面向对象的抽象程度比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

小结：数据封装、继承和多态是面向对象的三大特点。

一、类和实例
面向对象最重要的概念就是类(Class)和实例(Instance)，必须牢记类是对象(抽象)的模板，
比如Student类，而实例是根据类创建处理的一个个具体的“对象”，每个对象都拥有相同的
方法，但各自的数据可能不同。
仍以Student类为例，在Python中，定义类是通过class关键字：
class Student(object):
    pass

class后面紧跟着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示
该类是从哪个类继承下来的，通常如果没有合适的继承类，就使用object类，这是所有类最终
都会继承的类。

定义好了Student类，就可以根据Student类创建出Student实例，创建实例通过类名+()实现：
bart = Student()
<class '__main__.Student'>
<__main__.Student object at 0x0000000002BE7EC8>
可以看到，变量bart指向的是一个Student的实例，后面是内存地址，每个object的地址都不一
样，而Student本身则是一个类。
可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个那么属性：
class Student(object):
    pass

print(Student)
bart = Student()
print(bart)
bart.name = "Bart Simpson"
print(bart.name)

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性
强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候就把name,score属性绑定
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法
匹配的参数，但self不需传参，Python解释器自己会把实例变量传进去：
bart = Student('Bart Simpson', 59)

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是self，并且，调用
时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以使用
默认参数、可变参数、关键字参数和命名关键字参数。

01. 数据封装
面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的
name和score这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩
def print_score(std):
    print('%s: %s' % (std.name,std.score))

但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去
访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何
打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，却不
用知道内部实现细节。

封装的另一个好处是可以给Student类增加新的方法，比如get_grade:

小结：
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互
不影响。

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两实例变量，虽然他们
都是同一个类的不同实例，但拥有的变量名称都可能不同
''')

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
print("外部可以修改类的属性")
bart = Student('Bart Simpson',59)
print(bart.score)
bart.score = 99
print(bart.score)

print('''
二、访问限制
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例
的变量名如果以__开头，就变成了一个私有变量(private)，只有内部可以访问，外部不能访
问，会报错。

需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划
线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以不能用这样的
变量名。

有些变量，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当
你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要
随意访问

双下划线开头的实例变量__name可以通过_student__name来访问。也就是说，Pyhon本身没有
任何机制阻止你干坏事儿，一切全靠自觉。

最后注意下面这种错误写法：
bart = Student("Bart Simpson",59)
bart.get_name()→Bart Simpson
bart.__name = 'New Name'
bart.__name → New Name
关键点__name 和class内部的__name不是同一个变量！内部的__name变量已经被Python解释器
自动改成了_student__name，而外部代码被新增增了一个__name变量


''')
'''
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
print("外部不可以访问类的属性")
bart = Student('Bart Simpson',59)
print(bart.score)
print("外部不可以修改类的属性")
bart.score = 99
print(bart.score)
'''


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)

bart = Student("Bart Simpson",59)
print("bart.get_name()=",bart.get_name())
bart.__name = 'New Name'
print("bart.__name=",bart.__name)
print("bart.get_name()=",bart.get_name())
print("bart.get_name()获取的__name并未被修改！！！")

print('''
三、继承和多态
继承的最大好处就是子类获得了父类的全部功能。
多态的好处是，我们需要传入各种子类型时，比如Dog,Cat,Tortoise...我们只需要接收父类
Animal，子类都可以看做是父类，Dog，Cat,Tortoise都是Animal。然后，按照父类Animal进
行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子
类，就会自动调用实际类型的run()方法。

对于一个变量，我们只需要知道它是Animal类型，无需确切知道它的子类型，就可以放心地
调用run()方法，而具体调用的run()方法是作用在Animal,Dog,Cat还是Tortoise对象上，由
运行时该对象的确切类型决定，这就是多态的真正威力：调用方只管调用，不管细节，而当
我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用
的，这就是著名的“开闭”原则：
    ·对扩展开放：允许新增Animal子类；
    ·对修改关闭：不需要修改依赖Animal类型的run_twice（）等函数
''')
class Animal(object):
    
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):

    def run(self):
        print("Tortoise is slowly running...")

def run_twice(animal):
    animal.run()
    animal.run()

class Timer(object):

    def run(self):
        print("Timer is starting...")

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print("多态调用：")
run_twice(dog)
run_twice(cat)
tortoise = Tortoise()
run_twice(tortoise)
timer = Timer()
run_twice(timer)

print('''
01. 静态语言VS动态语言
对于静态语言(例如java)来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或
者它的子类型，否则将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型，只要传入对象有run()方法
就可以。
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子
走起路来像鸭子”，那它就可以被看成是鸭子。
小结：
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的
方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像动态语言那样是必须的。

四、获取对象信息
01. 使用type()--判断基本类型
02. 使用isinsctance()--判断class的类型
    能用type()判断的类型也可以用isinstance()判断
    并且还可以判断一个变量是否是某些类型中的一种，如判断是list或者是tuple
    总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
03. 使用dir()获得对象的所有属性和方法
    返回的属性和方法列表中的类似__XXX__的属性和方法在Python中都有特殊用途__len__
    实际上，在len()函数内部，它自动去调用该对象的__len__()方法。
    我们自己写类也可以有__len()__方法。
小结：
通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要
注意的是：只有在不知道对象信息的时候，我们才会去获取对象信息。
如果可以直接写 sum = obj.x + obj.y
就不要写 sum = getattr(obj,'x') + getattr(obj,'y')

假设我们希望从文件流fp中读取图像，我们首先要判断fp对象是否存在read方法，如果存在
则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
def readImage(fp):
    if hasattr(fp,'read'):
        return readDaa(fp)
    return None
''')

'''
print("type(123)=",type(123))
print("type('str')=",type('str'))
print("type(None)=",type(None))
print("type(dog)=",type(dog))
animal = Animal
import types
print("type(run_twice(animal))=",type(run_twice(animal))==types.FunctionType)
print("isinstance(dog,Dog)=",isinstance(dog,Dog))
print("isinstance(dog,Animal)=",isinstance(dog,Animal))
print("isinstance([1,2,3],(list,tuple))=",isinstance([1,2,3],(list,tuple)))
print("dir(dog)=",dir(dog))
'''

print('''
五、实例属性和类属性
由于Python是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是通过实例变量，或者是通过self变量
小结：
实例属性属于各个实例所有，互不干扰；
类属性属于类所有，所有实例共享一个属性
不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

十六、面向对象高级编程
封装、继承和多态是面向对象程序设计中的最基础的3个概念。在Python中，面向对象还有
很多高级特性，允许我们写出非常强大的功能。多重继承、定制类、元类等。

01. 使用__slots__
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定
任何属性和方法，这就是动态语言的零活性。
给一个实例绑定的方法，对另一个实例不起作用，给class绑定方法才可以。
动态绑定还允许我们在程序运行的过程中动态给class加上功能。

在定义class的时候，定义__slots__变量，将属性列表赋给该变量，来限制该class实例能
添加的属性。当添加列表中不存在的属性时会报错。
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。
除非在子类中也定义__slots__,这样，子类实例允许定义的属性就是自身的__slots__加上
父类的__slots__。

02. 使用@property
在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数
导致成绩可以随便改。使用set_ get_方法能够检查，但是有些麻烦

装饰器(decorator)可以给函数动态加上功能，对于类的方法，装饰器一样起作用。Python
内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

@property的实现比较复杂，把一个getter方法变成属性，只需要加上@property就可以了
此时，@property本身又创建了另一个装饰器@score.setter,负责把一个setter方法变成
属性赋值，于是，我们就拥有一个可控的属性操作。

注意这个神奇的@property,我们对实例属性操作的时候，就知道该属性很可能不是直接暴
露的，而是通过getter和setter方法实现的。还可以定义只读属性，只定义getter方法，不
定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

上面的birth是可读属性，而age是一个只读属性，因为age可以根据birth和当前时间计算
小结：
@property广泛应用在类的定义中，可以让调用者写成简短的代码，同时保证对参数进行必‘
要的检查，这样，程序运行时就减少了出错的可能性。
''')

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
        

s = Student()
s.score = 60
print(s.score)

print('''
02. 多重继承
通过多重继承，一个子类可以同时获得多个父类的所有功能。

MinIn
在设计类的继承关系时，通常，主线都是单一继承下来的，如果需要混入额外的功能，
通过多重继承就可以实现。
为了更好地看成继承关系，我们把runnable和Flyable改为RunnableMixIn和FlyableMixIn
的功能，而不是设计多层次的复杂的继承关系
Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这
两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由
ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速
构造出所需的子类。

小结：
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
只允许单一继承的语言(如java)不能使用MixIn的设计。



03. 定制类
看到类似__slots__这种形如__XXX__的变量或者函数名就要注意，这些在Python中有特殊
用途。
__slots__ 保存的列表中设置了允许绑定属性范围
__len__() 返回类名的长度
__str__() 相当于oString()方法，给用户看的
__repr__() 返回程序开发者看到的字符串，跟开发人员看的。
__iter__() 该方法返回一个迭代对象
__getitem__() 根据下标取出元素，可以支持切片，可以支持负数索引，可以支持dict对象
__setitem__()
__delitem__()
__getattr__() 获取属性值
__call__() 定义了该方法的类可以直接对实例进行调用。

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
print(s())

04. 使用枚举类
因为普通方式定义的常量其实质还是一个int类型，并且是可修改的。
通过枚举类型来实现真正的常量
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
@unique装饰器可以帮助我们检查保证没有重复值。

05. 使用元类
01）type()
动态语言和静态语言的最大不同，就是函数和类的定义不是编译时定义的，而是运行动态
创建的。

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态
创建出一个Hello的class对象

type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，
而h是一个实例，它的类型就是class(Hello)。

我们说class的定义是运行时动态创建的，而创建class的方法就是使用type函数

type函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()
函数创建出Hello类，而无需通过class Hello(object）的定义：

要创建一个class对象，type()函数依次传入3个参数：
    1.class的名称
    2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单
      元素写法
    3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时
仅仅是扫描一下class定义的语法，然后调用type函数创建出class.

type()函数可以动态创建类

metaclass
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass.
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
类是metaclass创建出来的实例，很少用到，以后再说吧！

十七、错误调试和测试
跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。(Python的pdb可以让我们
以单步方式执行代码）
有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测。

01. 错误处理
用错误码来表示是否出错十分不便，因为函数的返回结果和错误码混在一起，难判断
Python使用try...except...finally...的错误处理机制

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

当我们认为某些代码可能会出错时，可以用try来运行这段代码。
不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获就可以了。

调用栈
如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，
然后程序退出。

记录错误
如果不捕获错误，自然可以让Python解释器去打印出错误堆栈，但程序也被结束了。我们
捕获错误，打印错误堆栈，分析错误原因，让程序自动运行下去。

抛出错误
因为错误时class，捕获一个错误就是捕获到该class的一个实例，因此，错误并不是凭空
产生的，而是有意创建并抛出的。Python内置函数会抛出很多类型的错误，我们自己编写
的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误class，选择好继承关系，然后，用
raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

尽量使用Python内置的错误类型，只有在必要的时候才定义我们自己的错误类型。

还有一种错误处理方式，当前函数不知道错误如何处理，可以继续抛出错误，让调用者去
处理。

02. 调试
用print()打印可能有问题的变量，简单直接粗暴有效；将来还需要删除这些print语句

01）断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

assert的意思是，表达式 n != 0应该是True，否则，根据程序运行逻辑，后面的代码肯定
会出错。
如果断言失败，assert语句本身就会抛出AssertinError

$ python -O err.py
Traceback (most recent call last):
-O参数用来关闭assert,assert语句相当于pass

02）logging
把print()替换为loggin是第三种方式，和assert比，logging不会抛出错误，可输出到文件
import logging

logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

logging允许指定记录信息的级别，有debug, info, warning, error等几个级别，当我们
指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后,debug和
info 就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后
统一控制输出哪个级别的信息。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如
console和文件。

03）pdb
第4种方式是启动Python的调试器pdb,让程序以单步方式运行，可以随时查看运行状态
在命令行下执行 python -m pdb xxx.py
    l 查看代码
    n 执行下一条代码
    p var 查看变量的值
这种方式理论上是可行的，实际操作很麻烦。

04）pdb.set_trace()
这个方法也是用pdb,但是不需要单步执行，只需导入pdb，然后，在可能出错的地方放一个
pdb.set_trace()，就可以设置一个断点。
这个方法效率也高不到哪里去

05）IDE
如果要比较爽的设置断点，单步执行，就需要一个支持调试功能的IDE，如PyCharm...

logging是调试的终极武器。

03. 单元测试
TDD：Test-Driven Development)测试驱动开发

单元测试是用来对一个模块、一个函数或者一个类进行正确性检查的测试工作。
比如对函数abs()，我们可以编写出以下几个测试用例：
    1.输入正数，比如1、1.2、0.99，期待返回值与输入值相同；
    2.输入负数，比如-1, -1.2, -0.99，期待返回值与输入值相反；
    3.输入0，期待返回0；
    4.输入非数值类型，比如None,[],{}，期待抛出TypeError。
把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

如果单元测试通过，说明我们测试的这个函数能够正常工作；如果单元测试不通过，要么
函数有bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。

单元测试的意义：如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通
过，说明我们的修改未对abs()函数的原有行为造成影响，如果测试不通过，说明我们的休
改与原有行为不一致，要么修改代码，要么修改测试。

这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试
用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。

编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
以test开头的方法就是测试方法，不以test开头的方法，不被认为是测试方法，测试的时候
不会被执行。

对每一类测试都需要编写一个test_xxxx()方法，由于unittest.TestCase提供了很多内置
的条件判断，我们只需要调用这些方法就可断言输出是否是我们所期望的。最常用的断言就
是assertEqual:
    self.assertEqual(abs(-1),1) #断言函数返回的结果与1相等

另一种断言就是期待抛出指定类型的Eorror，比如通过d['empty']访问不存在的key时，断
言会抛出keyError:
    with self.assertRaises(KeyError):
        value = d['empty']

而通过d.empty访问不存在的key时，我们期待抛出AttributeError:
    with self.assertRaises(AttributeError):
        value = d.empty

01）运行单元测试
最简单的方法是在测试文件的最后加上下面两行代码,就可以把测试文件当成正常脚本运行。
if __name__== '__main__':
    unittest.main()

另一种方法就是在命令行通过参数 -m unittest直接运行单元测试；
$ pyton -m unittest mydict_test
这是推荐做法，因为这样可以一次批量运行很多单元测试，并且有很多工具可以自动运行

02）setUp与tearDown
可以在单元测试中编写两个特殊的setUp和tearDown方法。这两个方法会分别在调用每一个
测试方法的前后分别被执行。比如你在测试时需要启动一个数据库，这时，就可以在setUP
方法中连接数据库，在tearDown()方法中关闭数据库，这样不必在每个测试方法中重复相
同的代码。
''')

import logging

logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print("10 / n")

print('''
小结
·单元测试是可以有效的测试某个程序模块的行为，是未来重构代码的信息保证。
·单元测试的测试用例要覆盖常用的输入组合、边界条件和异常
·单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug.
·单元测试通过了并不意味着程序就么有bug了，但是不通过程序肯定有bug。

04. 文档测试
文档测试就是自动执行写在文档中的代码，但是注释要按如下格式进行书写：
def abs(n):
    '''                                         '''
    Function to get absolute value of number.
    
    Example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''                                          '''
    return n if n >= 0 else (-n)

    if __name__=='__main__':
    import doctest
    doctest.testmod()

这样写文档首先可以明确的告诉调用者该函数的期望输入和输出，并且Python内置的文
档测试(doctest)模块可以直接提取注释中的代码执行并测试。
doctest严格按照Python交互式mingl行的输入和输出来判断测试结果是否正确。只有测
试异常的时候，可以用...表示中间一大段烦人的输出。

测试程序中最后添加三行的作用是，只有直接运行改代码码时，测试才会执行。

小结
doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工
具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了它。


十八、IO编程
IO在计算机中指Input/Output，就是输入和输出。由于程序和运行时数据是在内存中驻
留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，
就需要IO接口。

比如你打开浏览器，访问新浪网页，浏览器这个程序就需要通过网络IO获取新浪的网页。
浏览器首先会发送数据给新浪服务器，告诉他我想要的首页的HTML，这个动作是往外发
数据，叫Output；随后新浪服务器把网页发过来，这个动作是从外面接收数据，叫Input
所以，通常程序完成IO操作会有Input和Output两个数据流。当然也有只有一个的情况，
比如，从磁盘读取文件到内存，就只有Input操作，反过来，把数据写到磁盘文件里，就
只是一个Output操作。

IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水
管里的水，但只能单向流动。Input Stream就是数据从外面(磁盘、网络)流进内存，
Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器
之间至少需要建立两根水管，才可以既能发数据，又能收数据。

由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配
的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需0.01秒
可是磁盘接收这100M的数据可能需要10秒，有两种协调办法：
第一种是CPU等着，也就是程序暂停执行后续代码，等100M数据在10秒后写入磁盘，再接
着往下执行，这种模式成为同步IO；
另一种方法是CPU不等待，继续执行后续代码，这种模式称为异步IO。

同步和异步的区别就在于等待IO执行的结果。异步IO编写程序的性能会远远高于同步IO，
但是异步IO的编程模型复杂，比如知道执行结果的方式有回调模式、轮询模式，复杂。

操作IO的能力是由操作系统提供的，每一种编程语言都会把操作系统提供的C低级接口
封装起来方便使用，Python也不例外。本章就是要讨论Python的IO编程接口。

01. 文件读写
在磁盘上读写文件的功能是由操作系统提供的，现代操作系统不允许普通程序直接操作
磁盘，所以，读写文件就是请求操作系统打开一个文件对象(通常称为文件描述符)，然
后，通过操作系统提供的接口从这个文件对象中读取数据(读文件)，或者把数据吸入这
个文件对象(谢文件)。

01）读文件
f = open('/Users/michael/test.txt', 'r')
 r表示读，w表示写
 如果文件不存在，open()函数会抛出一个IOError的错误，并且给出错误码和详细的信
 息告诉你文件不存在。

f.read()
Python把内容读到内存，用一个str对象表示

f.close()
文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时
间能打开的文件数量也是有限的。

由于读写文件都能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了
保证无论是否出错都能正确地关闭文件，可以使用try...finally来实现：
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
        
但是，每次都这么写实作太繁琐，所以，Python引入了with语句来自动帮助我们调用
close()方法，特点是代码更简洁，且不必调用f.close()。
with open('/path/to/file', 'r') as f:
    print(f.read())

调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了。所以保险起见
可以反复调用read(size)方法，另外，调用readline()可以每次读取一行内容，调用
readlines()一次读取所有内容并返回list。因此，要根据需要进行调用。

如果文件很小，read()一次性读取最方便；如果不确定文件大小，反复调用read(size)
比较保险；如果是配置文件，调用readlines()最方便。
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

file-like Object
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
除了file外，还可以是内存的字节流、网络流、自定义流等等。file-like Object不要求
从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object, 常用字临时缓冲。

二进制文件
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('/Users/michael/test.jpg', 'rb')
f.read()

字符编码
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如读取GBK文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f.read()

遇到有些编码不规范的文件，可能会遇到UnicodeDecodeError，因为文本文件中可能夹杂
了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇
到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

写文件
写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示
写文本文件或写二进制文件：
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
可以反复调用write()来写入文件，但是，务必要调用f.close来关闭文件。当我们写文件
时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候，再慢
慢写入。只有调用f.close()方法时，操作系统才保证把没有吸入的数据全部写入磁盘。
忘记调用f.close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了，所以，还是
用with语句保险：
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动换成指定
编码。
以'w'方式写入文件时，如果文件已经存在，会直接覆盖(相当于删掉后新写入一个文件).
如果我们希望追加到文件末尾，可以传入'a'追加(append)模式写入

02. StringIO和BytesIO
01）StringIO
StringIO顾名思义就是在内存中读写str.
要不str写入StringIO，我们需要先创建一个StringIO, 然后，像文件一样写入即可：
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())
hello world!

getvalue()方法用于获得写入后的str.
要读取StringIO,可以用一个str初始化StringIO,然后像读文件一样读取：
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!

2）BytesIO
StringIO操作的只能是str,如果要操作二进制数据，就需要使用BytesIO
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
注意，写入的不是str, 而是经过UTF-8编码的Bytes
和StringIO类似，可以用一个bytes初始化BytesIO,然后像读文件一样读取：
>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'

小结：
StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致接口。
''')

f = open('tmp/excerice_1.png','rb')
a = f.read(40000)
f.close()

f1 = open('tmp/123.png','wb')
f1.write(a)
f1.close()

print('''
03. 操作文件和目录
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。
比如dir、cp等命令
Python内置的os模块，也可以直接调用操作系统提供的接口函数
import os
print(os.name)

01）环境变量
os.environ,列出所有的环境变量

02）操作文件和目录
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中。
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')


04. 序列化
在程序运行过程中，所有的变量都是在内存中，比如，定义一个dict:
d = dict(name='Bob',age=20,score=88)
可以随时修改变量，比如把name改成'bill'，但是一旦程序结束，变量所占用的内存就
被操作系统全部回收。如果没有把修改后的'bill'存储到磁盘上，下次重新运行程序，
变量又被初始化为'Bob'。
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫picking，在
其他语言中也被称之为serialization，marshalling, flattening等。
序列化之后，可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpacking.
>>> import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d)
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX
\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

pickle.dumps()方法把任意对象序列化成一个bytes,然后就可以把这个bytes写入文件。
或者调用pickle.dump()直接把对象序列化写入一个file-like Object

当我们把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()
方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like object中直接
反序列化出对象。

01）JSON
如果我们要在不同编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读
取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快
而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应
JSON类型   Python类型
{}         dict
[]         list
"String"   str
234.56     int / float
true/false True/False
null       None

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串
之间转换。
''')

import os
import pickle

print(os.name)
print(os.environ.get('path'))
f = open('tmp/dump.txt','wb')
d=dict(name='Bob',age=20,score=88)
pickle.dump(d,f)
f.close()

f = open('tmp/dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
print("")
print("JSON序列化")
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

print('''
JSON进阶
Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class
表示对象，比如定义Student类，然后序列化：



''')
'''
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print("序列化。。。。")
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print("反序列化。。。")
print(json.loads(json_str, object_hook=dict2student))
'''
print('''
十九、进程和线程
Mac OS X, UNIX, Linux, Windows等都是支持“多任务”的操作系统。
多任务就是操作系统可以同时运行多个任务，打个比方，一边上网，一边听音乐，一边用
word赶作业，这就是多任务。
现在，多核CPU已经很普及了，但是，即使过去的单核CPU也可以执行多任务。采用的方法
是让各个任务轮流交替执行。由于CPU运行速度很快，感觉所有任务都在同时执行。
真正的并行执行多任务只能在多核CPU上实现，但是，任务数量远远多于CPU的核心数量，
所以，操作系统也会自动把很多任务轮流调度到美国核心上执行。
对于操作系统来说，一个任务就是一个进程(Process)，比如打开一个浏览器就是启动一
个浏览器进程，打开一个记事本就启动了一个记事本进程。
有些进程还不止同时干一件事，比如word，它可以同时进行打字、拼写检查、打印等事情
在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这
些“子任务”称为线程(Thread)。
由于美国进程至少要干一件事，所以，一个进程至少有一个线程。当然，像word这种复杂
的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，
也是有操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同
时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。

Python要同时执行多个任务有三种解决方案：
·多进程模式：启动多个进程
·多线程模式：在一个进程内启动多个线程
·多进程+多线程模式：启动多个进程，在每个进程中启动多个线程

小结
线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全又操作
系统决定，程序自己不能决定什么时候执行，执行多长时间。
多进程和多线程的程序涉及到同步、数据共享的问题，编写起来很复杂。

01. 多进程
要让Python程序实现多进程(multiprocessing)，我们要先了解操作系统的相关知识。
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一
次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程(称为父
进程)复制了一份(称为子进程)，然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID，这样做的理由是，一个父进程可以fork出
很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getappid()就可
以拿到父进程的ID。

01）multiprocessing
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于windows没有fork
调用，multiprocessing模块提供了一个Process类来代表一个进程对象。

进程的代码调试没有出现预期的效果，以后如果用到的话再来研究吧

02. 多线程
多任务可以由多进程完成，也可以由一个进程内的多线程完成

由于线程是操作系统直接支持的执行单元，因此高级语言通常都内置多线程的支持，
Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，低级和高级，高级对低级进行
了封装，绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行。

01）Lock
多线程和多进程的最大不同在于，多进程中，同一个变量各自有一份拷贝在于每个
进程中，互不影响；而多线程中，所有变量都由所有线程共享，所以，任何一个变量都
可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改了
一个变量，把内容给该乱了。
为了改进这个现象，线程修改变量时先将变量锁住，修改完成后再释放锁，让其他线程
进行修改。

02）多核CPU
启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占有率仅有102%,也就是
仅用了一核。但是，C、C++或Java直接可以跑满全部核心，4核就跑到400%, 8核就跑到
800%。为什么Python不行呢？
因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global
interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条
字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把
所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即时100个
线程跑在100核CPU上，也只能使用一个核。
GIL是Python解释器设计的历史遗留问题，通常我们的解释器是官方实现的CPython，要
真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线
程利用多核，那只能通过C扩展来实现，不过，这样就失去了Python简单易用的特点。

不过也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程
实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

小结：
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在
Python中就是一个美丽的梦。

03. ThreadLocal
在多线程环境下，每个线程都有自己的数据，一下线程使用自己的局部变量比使用全
局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修
改必须加锁。
但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦。
ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不
干扰。解决了参数在一个线程中各个函数之间互相传递的问题。

04. 进程 VS 线程
多进程模式的最大优点是稳定性高，因为一个进程崩溃了，不会影响主进程和其他子
进程，著名的Apache最早就采用多进程模式。缺点是创建进程的代价大。
多线程模式比多进程快一点儿，在Windows下，多线程的效率比多进程高，稳定性差。

01）线程切换
无论是多进程还是多线程，只要数量一多，效率肯定就上不去。因为切换线程或进程
也是需要耗费系统资源的，执行也是需要时间的。

02）计算密集型 VS IO密集型
是否采用多任务的第二个考虑是任务的类型。
计算密集型任务的特点是要进行大量的计算，消耗CPU资源，任务数量应当等于CPU的
核心数量。代码运行效率至关重要，Python不适合。
IO密集型任务涉及到网络、磁盘操作，这里任务的特点是CPU消耗少，IO等待的时间多
Web应用就是这类IO密集型的任务。Python等解释性语言适合。

03）异步IO
考虑到CPU和IO之间巨大的速度差异，一个任务执行的过程中大部分时间都在等待IO
操作，单进程模型会导致逼得任务无法并行执行，因此，我们才需要多进程模型或者
多任务模型来支持多任务并发执行。
现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果重复
利用操作系统通过的异步IO支持，就可以用单进程模型来支持多线程模型来支持多任
务并发执行。

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分
利用操作系统提供的异步IO支持就可以用单进程单线程来执行多任务，这种全新的模
型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，他在单核CPU上采用单进程
模型，可以高效的支持多任务。

对应Python语言，单进程的一般编程模型称为协程，有了谢成的异步编程单线程模型
就可以基于事件驱动编写高效的多任务程序。

04. 分布式进程
Python的分布式进程接口简单，封装良好，适合需要把繁重的任务分布到多台机器的
环境下。
''')

'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target='run_proc', args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

print("Pool的示例......")
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


print("多线程code示例......")
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''
print('''
二十、正则表达式
字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不
在。比如判断一个字符串是否是合法的Email地址，虽然可以编程提取@前后的字符串
再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。

正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的
语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，
否则，该字符串就是不合法的。

因为正则表达式也是用字符串表示的，先了解如何用字符串来描述字符串：
01）直接给出字符，就是精确匹配。
02）\d 可以匹配一个数字
03）\w 可以匹配一个字母或数字
04）. 匹配任意1个字符
05）* 匹配任意个字符
06）+ 匹配至少一个字符
07）? 匹配0个或1个字符
08）{n} 表示n个字符
09）{n,m} 表示n-m个字符
10）\s 空格 匹配tab等空白字符
11）[] 表示范围
12) | 表示或
13）^ 表示行的开头
14）$ 表示行的末尾

01. re模块
Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用"\"
转义，所以要特别注意 s='ABC\\-001' → 'ABC\-001'
因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了。

match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。

02. 切分字符串
用正则表达式切分字符串比用固定的字符更灵活

03. 分组
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能，用()表示的
就是要提取的分组(Group)。比如：^(\d{3})-(\d{3,8})$分别定义了两个组，可以
直接从匹配的字符串中提取出区号和本地号码：

04. 贪婪匹配
正则表达式默认是贪婪匹配，就是匹配尽可能多的字符
加个？就可以让贪婪匹配变成非贪婪匹配。

05. 编译
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
    1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    2.用编译后的正则表达式去匹配字符串
如果一个正则表达式要重复使用几千次，出于效率考虑，我们可以预编译正则表达式
接下来重复使用时就不需要编译这个步骤了，直接匹配：

编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用
对应的方法时，不用给出正则表达式字符串

06. 小结
正则表达式非常强大，要在短短的一节里讲透很难，就是个多练，本次比较有心得，
能够看得懂了。不断地重复就会有进步。

''')
import re
print("match()方法：")
print(re.match(r'^\d{3}-\d{3,8}$','010-12345'))
print(re.match(r'^\d{3}-\d{3,8}$','010 12345'))
print("")

print("切分字符串")
print("'a b  c'.split(' ')的结果是：")
print('a b  c'.split(' '))
print("无法识别连续的空格")
print("")
print("re.split(r'\s+','a b   c')切分的结果是：")
print(re.split(r'\s+','a b   c'))
print("再加入其它的分隔符也容易实现")
print("re.split(r'[\s\,\;]+','a,b  c  d')切分的结果是：")
print(re.split(r'[\s\,\;]+','a,b;;  c  d'))
print("")

print("分组")
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print("re.match(r'^(\d{3})-(\d{3,8})$','010-12345')")
print(m)
print("m.group(0)=",m.group(0))
print("m.group(1)=",m.group(1))
print("m.group(2)=",m.group(2))
print("")

print("贪婪匹配")
print("re.match(r'^(\d+)(0*)$', '102300').groups()")
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print("\d+是贪婪匹配，加个？就可以让d+采用非贪婪匹配")      
print("re.match(r'^(\d+?)(0*)$', '102300').groups()")
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
print("")

print("编译")
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print("re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')")
print("re_telephone.match('010-12345').groups()")
print(re_telephone.match('010-12345').groups())
print("re_telephone.match('010-8086').groups()")
print(re_telephone.match('010-8086').groups())






