#########################################
## 标题：PythonStart 入门               #
## 时间：2019/9/6 开始                  #
#########################################

第一章 环境搭建(使用Python3)
第二章 Python3基础语法
1.编码：默认UTF-8
2.保留字：
	>>> import keyword
	>>> keyword.kwlist
3.注释：单行注释 #   多行注释 ''' """
4.行与缩进
  缩进表示代码块，同一个代码块必须缩进相同的空格数
5.多行语句
  多行语句末尾用反斜杠(\)，括号中不需使用反斜杠(\)
6.数字(Number)类型
  int bool float complex（1 + 2j）
7.字符串(String)
  单引号和双引号完全相同
  三引号可以指定多行字符串
  反斜杠是转义符
  + 表示连接， * 重复次数
  索引可以为负数，表示从后面开始
  字符串不能改变
  没有单独的字符型，一个字符就是长度为一的字符串
  字符串截取称为切片：变量[开始下标：结束下标：步长]
8.空行
  函数之间用空行分隔，类和函数入口之间有空行。
  空行不是语法的一部分，是程序代码的一部分。
9.同一行显示多条语句
  语句之间用";"分隔
10.多个语句构成代码组
   缩进相同的一组语句，称为代码组
11.Print输出
   print输出默认是换行的，在变量末尾加上end="":
12.import与from...import
   import somemodule  导入整个模块
   from somemodule import somefunction  从某个模块导入某个函数
   from somemodule import func1，func2  从某天模块导入多个函数
   form somemodule import * 从某个模块导入其全部函数
13.命令行参数

第三章 基本数据类型
01.概述
   Python中的变量不需要声明，使用前必须赋值，赋值后变量才会创建
   Python中变量没有类型，变量指向的内存对象有类型。
02.多个变量赋值
   JS中的解构赋值
03.标准数据类型
   Number(数字)   不可变
   String(字符串)   不可变
   List(列表)   可变
   Tuple(元组)   不可变
   Set(集合)  可变
   Dictionary(字典)  可变
04.Number(数字)
   type()查询变量所指的对象类型，不认为子类是一种父类类型
   isinstance()查询变量所指的对象类型，认为子类是一种父类类型
   为变量指定一个值时，Number对象被创建，del语句可以删除单个或多个对象
05.String(字符串)
06.List(列表)
07.Tuple(元组)
08.Set(集合)
   用大括号{}创建空集合，set()函数创建集合。
   集合的基本概念是进行成员关系测试和删除重复元素。
09.Dictionary(字典)
   字典是一种映射类型，用{}标识，是无序的键(key):值(value)的集合。
   列表是有序的对象集合，字典是无序的对象集合。字典通过键存取，而非偏移。
   键(key)必须使用不可变类型，同一个字典中键是惟一的。
   内置函数：clear() keys() values()等。
10.数据类型转换
   int(x[,base])
   float(x)
   complex(real[,imag])
   str(x)
   repr(x)  将x转换为表达式字符串
   eval(str)   计算字符串中的有效Python表达式，并返回一个对象
   tuple(s)   将序列s转换为元组
   list(s)
   set(s)
   dict(d)   创建一个字典，d必须是一个(key,value)元组序列
   frozenset(s)   转换为不可变集合
   chr(x)   将一个整数转换为一个字符
   ord(x) 转换为整数
   hex(x) 转换为十六进制字符串
   oct(x) 转换为八进制字符串

第四章 Python3解释器
01.交互式编程 python
02.脚本式编程 python xxx.py

第五章 Python3注释
01.算术运算符
   + 加
   - 减
   * 乘
   / 除
   % 取模
   ** 幂
   // 取整除(向下取整)
02.比较运算符
   == 等于
   != 不等于
   > 大于
   < 小于
   >= 大于等于
   <= 小于等于
03.赋值运算符
   =
   += 加法赋值
   -= 减法赋值
   *=
   /=
   %=
   **=
   //=
04.位运算符
   & 与
   | 或
   ^ 异或
   ~ 取反
   << 左移(高位丢弃，低位补零)
   >> 右移
05.逻辑运算符
   and 与
   or 或
   not 非
06.成员运算符
   in 在指定的序列中找到值返回True
   not in 在指定的序列中没有找到值返回True
07.身份运算符
   is 判断两个标识符是不是引用自一个对象
   is not 判断两个标识符是不是引用自不同对象
08.运算符优先级
   **
   ~ + -  按位取反 一元加号 一元减号(方法名为+@ —@)
   * / % //
   + -
   >> <<
   &
   ^ |
   <= < > >=
   <> == !=  等于运算符
   = %= /= //= -= += *= **=
   is is not
   in not in
   not and or
   
第六章 Python 数字(Number)
01.数据类型不允许改变：如果改变值，将重新分配内存空间。
02.数学函数
   abs(x)
   ceil(x)  向上取整，math.ceil(4.1)返回5
   cmp(x,y)  弃用，使用(x>y)-(x<y)替换
   exp(x)  返回e的x次幂
   fabs(x)  返回数字的绝对值，math.fabs(-10)返回10.0
   floor(x)  下舍取整
   log(x)
   log10(x)
   max(x1,x2,...)
   min(x1,x2,...)
   modf(x)  返回x的整数部分与小数部分，两部分的数值符合与x相同，整数部分以浮点型表示。
   pow(x,y)
   round(x[,n]) 返回浮点数的四舍五入值，n代表小数点的位数
   sqrt(x)  返回x的平方根
03.随机数函数
   choice(seq)  从序列的元素中随机挑选一个元素，如random.choice(range(10))，从0到9中随机挑选一个整数
   ruandrange([start,]stop[,step])  
   random()
   seed([x])
   shuffle(lst)
   uniform(x,y)
04.三角函数
   acos(x)
   asin(x)
   atan(x)
   atan2(y,x)  返回给定的X及Y坐标值的反正切值
   cos(x)
   hypot(x,y)  返回欧几里德范数 sqrt(x*x + y*y)
   sin(x)
   tan(x)
   degrees(x)  将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
   radians(x)  将角度转换为弧度
05.数学常量
   pi
   e
   
第七章 字符串
01.访问字符串中的值
   用方括号
02.字符串更新
   截取、拼接
03.转义字符--\
   \$ 续行符
   \\ 反斜杠
   \' 单引号
   \" 双引号
   \a 响铃
   \b 退格(Backspace)
   \000 空
   \n 换行
   \v 纵向制表符
   \t 横向制表符
   \r 回车
   \f 换页
   \oyy 八进制数(字母o)
   \xyy 十六进制数
   \other 其他字符以普通格式输出
04.字符串运算
   +	字符串连接
   *	重复输出字符串
   []	通过索引获取字符串中字符
   [: ]	截取字符串中的一部分，遵循左闭右开原则，str[0,2]不包含第三个字符
   in	成员运算符
   not in	
   r/R	原始字符串
   %	格式字符串
05.字符串格式化
   将一个值插入到一个有字符串格式符%s的字符串中
   字符串格式化符号：
   %c	字符及ASCII码
   %s	字符串
   %d	整数
   %u	无符号整数
   %o	无符号八进制数
   %x	无符号十六进制数(小写)
   %X	无符号十六进制数(大写)
   %f	浮点数，可指定小数点精度
   %e	科学计数法格式化浮点数
   %E	tongshang
   %g	%f和%e的简写
   %G	%E和%F的简写
   %p	用十六进制格式化变量的地址
   格式化操作辅助指令
   *    定义宽度或小数点精度
   -    用做左对齐
   +    在正数前面显示加号
   <sp> 在正数前面显示空格
   #    在八进制数前面显示零，在16进制前面显示'0x'或者'0X'
   0    在数字前面填充'0'而不是默认的空格
   %    '%%'输出一个单一的'%'
   (va) 映射变量(字典参数)
   m.n. m是显示的最小总宽度，n是小数点后的位数(如果可用的话)
06.三引号
   允许一个字符串跨多行，块中内容WYSIWYG
07.Unicode字符串
   Python3中所有的字符串都是Unicode字符串
08.Python的字符串内建函数
   capitalize()
   center(width,fillchar)
   cout(str,beg=0,end=len(string))
   bytes.decode(encoding="utf-8",errors="strict")
   encode(encoding='UTF-8'，errors='strict')
   endswith(suffix,beg=0,end=len(string))
   expandtabs(tabsize=8)
   find(str,beg=0,end=len(string))
   index(str,beg=0,end=len(string))
   isalnum()
   isalpha()
   sidigit()
   islower()
   isnumeric()
   isspace()
   istitle()
   isupper()
   join(seq)
   len(string)
   ljust(width[,fillchar])
   lower()
   lstrip()
   maketrans()
   max(str)
   min(str)
   replace(old,new[,max])
   rfind(str,beg=0,end=len(string))
   rindex(str,beg=0,end=len(string))
   rjust(width[,fillchar])
   rstrip()
   split(str="",num=string.count(str))
   splitlines([keepends])
   startswith(substr,beg=0,end=len(string))
   strip([chars])
   swapcase()
   title()
   translate(table,deletechars="")
   upper()
   sfill(width)
   isdecimal()
   
第八章 列表
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字--他的位置或索引，索引从0开始。
Python有6个序列的内置类型，最常见的列表和元组。
序列都可以进行的操作包括索引、切片、加、乘、检查成员。
Python内置确定序列长度以及确定最大和最小元素的方法。
列表是最常用的Python数据类型，以方括号内逗号分隔值的形式出现。
列表不需要具有相同的类型
01.访问列表中的值
   使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符。
02.更新列表
   可以对列表的数据项进行修改或更新，也可以使用append()方法来添加列表项
03.删除列表元素
   del list[2];
04.列表脚本操作符
   组合与重复列表和字符串操作类似，用+和*号
05.Python列表函数&方法
   Python包含以下函数：
   len(list)
   max(list)
   min(list)
   list(seq)
   Python包含以下方法：
   list.append(obj)
   list.count(obj)
   list.extend(seq)
   list.index(obj)
   list.insert(index.obj)
   list.pop([index=-1])
   list.remove(obj)
   list.reverse()
   list.sor(key=None,reverse=False)
   list.clear()
   list.copy()
   
第九章 Python 元组
	元组与列表类似，不同之处在于：
	1.元组的元素不能修改(修改、删除元组的元素会报错)
	  TypeError: 'tuple' object does not support item assignment
	2.元组使用小括号，列表使用方括号
	3.可以删除整个元组
	4.元组内置函数
	  len(tuple)
	  max(tuple)
	  min(tuple)
	  tuple(seq) 将列表转换为元组

第十章 字典
00.字典是另一种可变容器模型，且可以存储任意类型对象。
   字典的每个键值对(key:value)用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中。
   键必须是唯一的，值则不必。
01.字典键的特性
   键不可以重复，键不可以改变。
02.字典内置函数
   len(dict)
   str(dict)
   type(variable)  #<class 'dict'>
03.字典内置方法
   radiansdict.clear()
   radiansdict.copy()
   radiansdict.fromkeys()
   radiansdict.get(key,default=None)
   key in dict
   radiansdict.items()
   radiansdict.keys()
   radiansdict.setdefault(key,default=None)
   radiansdict.update(dict2)
   radiansdict.values()
   pop(key[.default])
   popitem()
   
第十一章 集合
01.集合(set)是一个无序不重复元素序列。
   可以使用大括号{}或者set()函数创建集合，
02.集合内置方法
   add()
   clear()
   copy()
   difference()
   difference_update()
   discard()
   intersection()
   intersection_update()
   isdisjoint()
   issubset()
   issuperset()
   pop()
   remove()
   symmetric_difference()
   union()
   update() 给集合添加元素
   
第十二章 编程第一步
01.结构赋值，同时给多个变量赋值
02.关键字end使输出结果在同一行

第十二章 条件控制
01.条件语句的一般形式
	if condition_1:
		statement_block_1
	elif condition_2:
	
第十三章 循环语句
01.while循环
	while condition:
		statement1
	else:
		statement2
02.	简单语句组
	while (condition): print('简单的一行执行语句')
03.for循环--变量序列项目
	for item in sequence
		statements
	else:
		statements
04.range()函数
   产生数列range([start,]stop[,step])
05.break和continue及循环中的else字句
   break语句可以跳出for和while循环体，且else语句块将不执行。
   continue语句跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
   else语句在穷尽列表或条件变为false循环终止时被执行，被break终止不执行。
06.pass语句
   空语句，用做占位符，保持程序结构的完整性
	class MyEmptyClass:
		pass
		
第十四章 迭代器与生成器
01.迭代器
   迭代器是访问集合元素的一种方式，可以记住遍历的位置的对象，只能前进不会后退，字符串、列表和元组都可以用于创建迭代器。
   list=[1,2,3,4]
   it=iter(list)
   print(next(it))
   for x in it:
	print(x,end=" ")
02.生成器
   使用了yield的函数被称为生成器（generator）
   跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，就是一个迭代器
   在调研生成器的过程中，每次遇到yield时，函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。
   调用一个生成器函数，返回的是一个迭代器对象
   
第十五章 函数
00.函数是组织好的，可重复使用的，用来实现单一或相关联功能的代码段
   函数能提高应用的模块性，代码的重复利用率。分为内建函数和自定义函数。
01.定义函数   
   以def关键字开头，后接函数名称和圆括号，最后时冒号
   传入参数和自变量放在圆括号中间
   函数第一行可以选择性的放置函数说明
   函数内容以冒号起始，并且缩进。
   return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的return相当于None
02.语法
	def 函数名(参数列表):
		函数体
03.函数调用
04.参数传递
   在Python中类型属于对象，变量没有类型，它仅仅是一个对象的引用(指针)
05.可更改(mutable)与不可更改(immutable)对象
   在Python中，string,tuple和number是不可变对象，list,dict是可变对象
   不可变类型：变量赋值a=5后，再赋值a=10, 这里实际是新生成一个int值对象，再让a指向他，而5被丢弃，不是改变了a的值，等于新生成了a。
   可变类型：变量赋值a=[1,2,3,4]后，再赋值a[2]=5,则是将a的第三个元素值更改，a本身没动，只是其中一部分值被修改了。
   Python函数的参数传递：
	  不可变类型：类似c++的值传递，如func(a),传递的只是a的值，没有影响a对象本身。
	  可变类型：类似c++的引用传递，列表，字典，如fun(a)修改后外部的a也被修改。
06.参数类型
   必需参数：必须以正确的顺序传入参数，调用时的数量必须和声明时一样。
   关键字参数：函数调用时使用关键字参数来确定传入的参数值。
   默认参数：调用时如果未传入参数，则使用默认参数。
   不定长参数：加了*的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。加了两个星号 ** 的参数会以字典的形式导入。
07.匿名函数
   不再使用def来定义函数，使用lambda来创建匿名函数
   ·lambda只是一个表达式，函数体比def简单很多。
   ·lambda的主体是一个表达式，而不是一个代码块，仅能封装有限的逻辑。
   ·lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
   ·虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
   语法：lambda [arg1 [,arg2,...argn]]:expression
08.return语句
   return语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None
	
第十六章 数据结构
01. 列表（可以修改）
	列表的方法		描述
	list.append(x)	把一个元素添加的列表末尾，相当于a[len(a):]=[x]
	list.extend(L)	添加列表的所有元素到列表末尾，a[len(a):]=L
	list.insert(i,x)在指定位置插入元素
	list.remove(x)	删除列表中值为x的第一个元素，没有元素返回错误
	list.pop([i])	从列表指定位置移除元素，不指定移除最后一个
	list.clear()	移除列表中的所有项，等于 del a[:]
	list.index(x)	返回列表中第一个值为x的元素的索引
	list.count(x)	返回x在列表中出现的次数
	list.sort()		对列表中的元素排序
	list.reverse()	倒排元素
	list.copy()		返回列表的浅复制，等于a[:]
02.	列表当堆栈使用
	push==>append(x)
	pop ==>pop()
03.	列表当队列使用
	效率不高，列表的尾部操作比较快，头部操作慢，所有的位置都要改变
04.	列表推导式
	列表推导式提供了从序列创建列表的简单途径。
	每个列表推导式都在for之后跟一个表达式，然后有零到多个for或if子句。返回结果是一个根据表达从其后的for和if上下文环境中生产出来的列表。
	如果希望表达式推导出一个元组，就必须使用括号。
05. del语句
	依据索引删除一个元素。这与使用pop()返回一个值不同。可以用del语句从列表中删除一个切片，或清空整个列表。
	也可以用del删除实体变量
06. 元组和序列
	元组由若干逗号分隔的值组成，创建元组时括号可选。
07.	集合
	集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素
	集合也支持推导式
08. 字典（无序的键值对集合）
	序列是以连续的整数为索引，字典以关键字为索引，关键字是任意不可变类型，通常用字符串或数值。
	字典推导可以用来创建任意键和值的表达式
09. 字典的遍历技巧
	在字典中遍历时，关键字和对应值可以使用items()方法同时解析出来
	在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
	同时遍历两个或更多的序列，可以使用 zip() 组合：
	要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
   
第十七章 模块
00.模块是一个包含所有已定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。
01.import语句
   import module1[, module2[,... moduleN]]
   一个模块只会被导入一次，防止被导入的模块多次执行
   搜索路径存储在sys.path中，可以保存到环境变量中。
   如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：fib = fibo.fib
02.from ... import语句
   从模块中导入一个指定的部分到当前命名空间中   ...函数名/变量名
03.from ... import * 语句
   导入一个模块的所有项目，尽量少用。
04.深入模块
   模块除了方法定义，还可以包括可执行代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
   每个模块都有各自独立的符号表，在模块内部为所有的函数当做全局符号来使用，可以用modname.itemname来访问。
05.__name__属性
   一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时模块中的某一程序块不执行，可以用__name__属性来使该程序块仅在该模块自身运行时被执行。
   if __name__ == '__main__': 即每个模块又有一个__name__属性，当其值为'__main__'时，标明该模块自身在运行，否则是被引入。
06.dir()函数
   内置函数dir()可以找到模块内定义的所有名称，以一个字符串列表的形式返回：
07.标准模块
   有些模块直接构建在解析器里，这些虽然不是语言内置功能，但他们能高效实用，甚至系统级调用也ok。
   这些组件会根据不同的操作系统进行不同形式的配置，比如winreg只提供给windows系统。
   sys模块内置在每一个Python解析器中，变量sys.ps1和sys.ps2定义了主提示符和副提示符对应的字符串
08.包
   包是一种管理Python模块命名空间的形式，采用"点模块名称"，如A.B表示包A中的子模块B
   在导入一个包的时候，Python会根据sys.path中的目录来寻找这个包中包含的子目录。
   目录只有包含一个叫做__init__.py的文件才会被认作是一个包，
   最简单的情况是放一个空的__init__.py就可以了。
09.从一个包中导入*
   导入语句遵循如下规则：如果包定义文件__init__.py存在一个叫做__all__的列表变量，那么在使用from package import *的时候就把这个列表中的所有名字作为包内容导入。
   __all__ = ["echo", "surround", "reverse"]
   这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块
   如果__all__没定义，那么使用from sound.effects import *这种语法的时候，就不会导入包sound.effects里的任何子模块，只是把包sound.effects和他里面定义的所有内容导入进来
   记住，使用from Package import specific_submodule这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。
   无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
   包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。可以修改这个变量，用来影响包含在包里面的模块和子包。

第十八章 输入和输出
01.输出格式化美化
   Python有两种输出值的方式，表达式语句和print()函数。
   第三种方式使用文件对象的write()方法，标准输出文件可以使用sys.stdout引用。
   str.format()函数可以用来格式化输出值。
   repr(解释器易读)或str(用户易读)函数可以将输出的值转成字符串。
   str.format()的基本使用
   print('{}网址："{}!"'.format('菜鸟教程','www.runoob.com'))
   括号及其里面的字符(称作格式化字段)将会被format()中的参数替换。
   如果在format()中使用了关键字参数，那么它们的值会指向使用该名字的参数。
   位置和关键字参数可以任意结合。
   !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
   在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
   如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
   最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
   也可以通过在 table 变量前使用 ** 来实现相同的功能：
02.旧式字符串格式化
   %操作符也可以实现字符串格式化。它将左边的参数作为类似sprintf()式的格式字符串，将右边的值代入，然后返回格式化后的字符串
03.读取键盘输入
   input()内置函数从标准输入读入一行文本，默认的标准输入是键盘
04.读和写文件
   open()会返回一个file对象，基本语法格式如下：
   open(filename,mode)  
   mode:只读、写入、追加等  r  rb	r+	rb+	w	wb	w+	wb+	a  ab  a+ ab+
   
   模式			r		r+		w		w+		a   	a+
   读			+		+				+				+
   写					+		+		+		+		+
   创建							+		+		+		+
   覆盖							+		+
   指针在开始	+		+		+		+
   指针在结尾									+		+
05.文件对象的方法
   f.read(size) size不存在或者为负数，读取全部文件。
   f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
   f.readlines() 将返回该文件中包含的所有行。
   f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
   f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
   f.seek(offset, from_what) 改变文件当前的位置。from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
   f.close() 来关闭文件并释放系统的资源
   open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
   参数说明:   
   file: 必需，文件路径（相对或者绝对路径）。
   mode: 可选，文件打开模式
   buffering: 设置缓冲
   encoding: 一般使用utf8
   errors: 报错级别
   newline: 区分换行符
   closefd: 传入的file参数类型
   opener:
06.pickle 模块
   pickle 模块实现了基本的数据序列化和反序列化。
   通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。   
   通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
06.文件对象的方法
   file.close()
   file.flush()
   file.fileno()
   file.isatty()
   file.read([size])
   file.readline([size])
   file.readlines('sizeint')
   file.seek(offset[,whence])
   file.tell()
   file.truncate([size])
   file.write(str)
   file.writelines(sequence)
   
第十九章 OS文件/目录方法
os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
	os.access(path,mode)
	os.chdir(path)
	os.chflags(path,flags)
	os.chmode(path,mode)
	os.chown(path,uid,gid)
	os.chroot(path)
	os.close(fd)
	os.closerange(fd_low,fd_high)
	os.dup(fd)
	os.dum2(fd,fd2)
	os.fchdir(fd)
	os.fchmode(fd,mode)
	os.fchown(fd,uid,gid)
	os.fdatasysnc(fd)
	os.fdopen(fd[,mode[,bufsize]])
	os.fpathconf(fd,name)
	os.fstat(fd)
	os.fstatvfs(fd)
	os.fsync(fd)
	os.ftruncate(fd,length)
	os.getcwd()
	os.getcwdu()
	os.isatty(fd)
	os.lchflags(path,flags)
	os.lchmode(path,mode)
	os.lchown(path,uid,gid)
	os.link(src,dst)
	os.listdir(path)
	os.lseek(fd.pos.how)
	os.lstat(path)
	os.major(device)
	os.makedev(major,minor)
	os.makedirs(path[,mode])
	os.minor(device)
	os.mkdir(path[,mode])
	os.mkfifo(path[,mode])
	os.mknod(filename[,mode=0600,device])
	os.open(file,flags[,mode])
	os.openty()
	os.pathconf(path,name)
	os.pipe()
	os.popen(command[,mode[,bufsize]])
	os.read(fd,n)
	os.readlink(path)
	os.remove(path)
	os.remvoedirs(path)
	os.rename(src,dst)
	os.renames(old,new)
	os.rmdir(path)
	os.stat(path)
	os.stat_float_times([newvalue])
	os.statvfs(path)
	os.sysmlink(src,dst)
	os.tcgetpgrp(fd)
	os.tcsetpgrp(fd,pg)
	os.tempnam([dir[,prefic]])
	os.tmpfile()
	os.tmpnam()
	os.ttyname(fd)
	os.unlink(path)
	os.utime(path,times)
	os.walk(top[,topdown=true[,onerror=None[,followlinks=False]]])
	os.write(fd,str)
	os.path 模块    //获取文件属性信息
第二十章 错误和异常
01.语法错误
   语法分析器指出了出错的一行，并且在最先找到的错误位置标记一个小箭头、
02.异常
   运行期检测到的错误被称为异常
03.异常处理
	try:
		x = int(input("Please enter a number: "))
	    break
	except ValueError:
	    print("Oops!  That was no valid number.  Try again   ")
	·首先执行try子句
	·如果没有异常发生，忽略except子句，try子句执行后结束。
	·如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和except之后的名称相符，那么对应的except子句将被执行。最后执行try语句之后的代码。
	·如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
   一个try语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
   处理程序将只针对对应的try子句中的异常进行处理，而不是其他的try的处理程序中的异常。
   一个except子句可以同时处理多个异常，这些异常将被放在一个括号里称为一个元组
	except (RuntimeError, TypeError, NameError):
		pass
   最后一个except子句可以忽略异常的名称，它将被当做通配符使用。你可以使用这种方法打印异常错误信息，然后再次把异常抛出。
   try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行
   使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。
   异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常
04.抛出异常
   raise NameError('ExceptClassChild')
05.用户自定义异常
   你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:
	class MyError(Exception):
		def __init__(self,value):
			self.value = value
		def __str__(self):
			return repr(self,value)
			
	try:
		raise MyError(2*2)
	except MyError as e:
		print('My exception occurred, value:', e.value)
06.定义清理行为
   try语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为
   不管 try 子句里面有没有发生异常，finally 子句都会执行。
07.预定义清理行为
   一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
   关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
   with open("myfile.txt") as f:
       for line in f:
           print(line, end="")

第二十章 面向对象
00.Python在设计之初就是一门面向对象的语言。
01.面向对象技术简介
   ·类(class)：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
   ·方法：类中定义的函数
   ·类变量：在整个实例化的对象中是共用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
   ·数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
   ·方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖(override),也称为方法的重写。
   ·局部变量：定义在方法中的变量，只作用于当前实例的类。
   ·实例变量：在类的声明中，属性是用变量表示的，这种变量称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
   ·继承：一个派生类(derived class)继承基类(base class)的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
   ·实例化：创建一个类的实例，类的具体对象。
   ·对象：通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法。
02.类定义
   class ClassName:
       <statement-1>
       .
       .
       .
       <statement-N>
   类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性
03.类对象
   类对象支持两种操作：属性引用和实例化
   属性引用使用和Python中所有的属性引用一样的标准语法：obj.name.
   类对象创建后，类命名空间中所有的命名都是有效属性名。
   类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
    def __init__(self):
		self.data = []
   类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法.
04.self代表类的实例，而非类
   类的方法与普通函数只有一个特别的区别--他们必须有一个额外的第一个参数名称，self。
05.类的方法
   在类的内部，使用def关键字定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数，self代表的是类的实例。
06.类的继承
   如果一种语言不支持继承，类就没有什么意义。
   class DerivedClassName(BaseClassName1):
   需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索。即方法在子类中未找到时，从左到右查找基类中是否包含方法。
   BaseClassName(示例中的基类名)必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用：
   class DerivedClassName(modulename.BaseClassName):
07.多继承
   class DerivedClassName(Base1, Base2, Base3):
   需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
08.方法重写
09.super()函数
   用于调用父类(超类)的一个方法。
   super是用来解决多重继承问题的，直接用类名调用父类方法，在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序(MRO)、重复调用(钻石继承)等种种问题。
   MRO就是类的方法解析顺序表，其实也就是继承父类方法时的顺序表。
   super(type,[,object-or-type])
   参数：
		type--类
		object-or-type--类，一般是self
	python3可以直接使用super().xxx代替super(class,self).xxx
10.类的专有方法
   __init__:构造函数，在生成对象时调用
   __del__:析构函数，释放对象时使用
   __repr__:打印、转换
   __setitem__:按照索引赋值
   __getitem__:按照索引获取值
   __len__:获得长度
   __cmp__:比较运算
   __call__:函数调用
   __add__:加运算
   __sub__:减运算
   __mul__:乘运算
   __truediv__:除运算
   __mod__:求余运算
   __pow__:乘方
11.运算符重载
   Python支持运算符重载，可以对类的专有方法进行重载。
   
第二十一章 命名空间和作用域
00.命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过Python字典来实现的。
   提供了在项目中避免冲突的一种方法，一般有三种命名空间：
   · 内置名称（built-in names），Python语言内置名称，比如函数名abs、char和异常名称BaseException、Exception等
   · 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其他导入模块、模块级变量和常量。
   · 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量及类中定义的变量。
   命名空间查找顺：局部 → 全局 → 内置
   命名空间的声明周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。无法从外部命名空间访问内部命名空间的对象。
01.作用域
   作用域就是一个Python程序可以直接访问命名空间的正文区域。
   在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
   Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
   变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
   · L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
   · E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
   · G（Global）：当前脚本的最外层，比如当前模块的全局变量。
   · B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索
   g_count = 0  # 全局作用域
   def outer():
       o_count = 1  # 闭包函数外的函数中
       def inner():
           i_count = 2  # 局部作用域
   Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，
02.全局变量和局部变量
03.global和nonlocal关键字
   当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字
   内层不通过关键字直接访问外层变量会报错(局部变量未定义)
   
第二十二章 标准库概览
01.操作系统接口
   os模块提供了与操作系统相关联的函数
   shutil模块提供了针对日程的文件盒目录管理任务的易于使用的高级接口。
02.文件通配符
   glob模块提供了一个函数用于从目录通配符搜索中生成文件列表glob.glob
03.命令行参数
   sys模块提供命令行参数sys.argb
04.错误输出重定向和程序终止
   错误重定向：sys.stdin\stdout\stderr  
   重定向终止：sys.exit()
05.字符串正则匹配
   re模块，高级字符串处理
06.数学
   math模块为浮点运行提供了对底层c函数库的访问
   random提供了生产随机数的工具
07.访问互联网
   smtplib、urllib用于访问互联网以及处理网络通信协议
08.日期和时间
   datetime模块为日期和时间处理提供了简单和复杂的方法，支持时区处理
09.数据压缩
   支持通用的数据打包和压缩格式：zlib,gzip,bz2,zipfile,tarfile.
10.性能度量
   度量解决同一问题的不同方法之间的性能差异timeit
11.测试模块
   doctest扫描模块并根据程序中内嵌的文档字符串执行测试
   
