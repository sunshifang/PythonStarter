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
   
第二十三章 正则表达式
00.正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
01.re.match函数
   尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
   re.match(pattern,string,flags=0)
	pattern 匹配的正则表达式
	string  要匹配的字符串
	flags   标志位，控制匹配方式，区分大小写、多行匹配等等。
   可以使用group(num)或groups()匹配对象函数来获取匹配的表达式。
    group(num=0)匹配的整个表达式的字符串，group()可以一次输入多个组号，返回一个包含那些组所对应值的元组。
	groups返回一个包含所有小组字符串的元组，从1到所含的小组号。
02.search方法
   re.search扫描整个字符串并返回第一个成功的匹配
   re.search(pattern, string, flags=0)
03.re.match与re.search的区别
   re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
04.re.sub(pattern,repl,string,count=0,flags=0)
	参数：
		pattern：正则中的模式字符串
		repl: 替换的字符串，也可为一个函数
		string：要被查找替换的原始字符串
		count：模式匹配后替换的最大次数，默认0表示替换所有的匹配。
		flags：编译时用的匹配模式，数字形式。
05.findall
   在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，未找到返回空表。
   re.findall(string[, pos[, endpos]])
06.finditer		
   在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
    re.finditer(pattern, string, flags=0)
07.split
   split 方法按照能够匹配的子串将字符串分割后返回列表
   re.split(pattern, string[, maxsplit=0, flags=0])
08.正则表达式的特殊元素
   模式		描述
   ^		字符串开头
   $		字符串末尾
   .		匹配任意字符
   [...]	表示一组字符，单独列出
   [^...]	不在组合中的字符
   re*		匹配0个或多个表达式
   re+		匹配一个或多个表达式
   re?		匹配0个或1个表达式
   re{n}	匹配n个表达式
   re{n,}	精确匹配n个前面表达式
   re{n,m}	匹配n到m个表达式
   a|b 		匹配a或b
   (re)		匹配括号内的表达式，表示一个组
   (?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
   (?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
   (?: re)	类似 (...), 但是不表示一个组
   (?imx:re)在括号中使用i, m, 或 x 可选标志
   (?-imx:re)在括号中不使用i, m, 或 x 可选标志
   (?#...)	注释.
   (?=re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
   (?!re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
   (?>re)	匹配的独立模式，省去回溯
   \w		匹配数字、字母、下划线
   \W		匹配非数字、字母、下划线
   \s		任意空白字符，等价于[\t\n\f]
   \S		任意非空字符
   \d		任意数字，等价于[0-9]
   \D		任意非数字
   \A		字符串开始
   \Z		字符串结束，如果存在换行，只匹配到换行前的结束字符串
   \z		字符串结束
   \G		最后匹配完成的位置
   \b 		匹配一个单词边界，也就是指单词和空格直接的位置。例如'er\b'可以匹配'never'中的er，不能匹配'verb'中的er
   \B		匹配一个非单词边界，同'\b'相反。
   \n,\t..	匹配一个换行符，制表符...
   \1...\9	匹配第n个分组的内容
   \10		匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
   
第二十四章   Python CGI 编程

00.CGI(Common Gateway Interface),通用网关接口，它是一段程序，运行在服务器上，如：HTTP服务器，提供同客户端HTML页面的接口。
01.网页浏览
   · 使用浏览器访问URL并连接到HTTP web服务器
   · Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
   · 浏览器从服务器上接收信息，并显示接收的文件或者错误信息。
   CGI程序可以使Python脚本、PERL脚本、SHELL脚本，C或者C++程序等
运行CGI需要WEB服务器进行设置，无法看到结果

第二十五章 Python MySQL  mysql-connector 驱动
00.按照教程没啥问题，在初始没有指定数据库的时候，注意当前数据库设置。
   用PyMySQL(v0.9)模块的时候，没有办法指定数据库端口，要解决一下。可能是版本低的问题吗？
01.主要使用cursor来执行sql语句，比nodejs方便
   可以批量实现插入语句，事务处理好像很方便。
   
第二十六章 网络编程
00.网络编程主要涉及到的是socket编程，上班后研究一下，还有研究一下git的合并。
   Python提供了两个级别访问的网络服务：
   · 低级别的网络服务级别支持基本的Socket，它提供了标准的BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
   · 高级别网络服务模块SocketServer，它提供了服务器中心类，可以简化网络服务器的开发。
01.什么是Socket？
   Socket又称套接字，应用程序通常通过“套接字”向网络发出请求或者应答网络请求，使主机或者一台计算机上的进程间可以通讯。
02.Socket()函数
   socket.socket([family[,type,[proto]]])
   其中，family：套接字家族可以使(用)AF_UNIX 或者 AF_INET
	    type：套接字类型可以根据是面向连接的还是非连接的，分为SOCK_STREAM或SOCK-DGRAM
		protocol: 一般不填默认为0.
03.Socket对象(内建)方法
   函数				描述
   服务器端套接字
   s.bind()			绑定地址(host,port)到套接字，在AF_INET下，以元组(host,port)的形式表示地址。
   s.listen()		开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
   s.accept()		被动接受TCP客户端连接，(阻塞式)等待连接的到来。
   客户端套接字
   s.connect()		主动初始化TCP服务器连接，一般address的格式为元组(hostname,port)，如果连接出错，返回socket。error错误。
   s.connect_ex()	connect()函数的扩展版本，出错时返回错误码，而不是抛出异常
   公共用途的套接字函数
   s.recv()
   s.send()
   s.sendall()
   s.recvfrom()
   s.sendto()
   s.close()
   s.getpeername()
   s.getsockname()
   s.setsockopt(level,opt,value)
   s.getsockopt(level,opt,[,buflen])
   s.settimeout(timeout)
   s.gettimeout()
   s.fileno()
   s.setblocking(flag)
   s.makefile()
04.简单实例  
   网络连接的实例要在终端中运行
05.Python Internet 模块
   协议		功能						端口号	Python模块
   HTTP		网页访问					80		httplib, urllib, xmlrpclib
   NNTP		阅读和张贴新闻文章，帖子	119		nntplib
   FTP		文件传输					20		ftplib，urllib
   SMTP		发送邮件					25		smtplib
   POP3		接收邮件					110		poplib
   IMAP4	获取邮件					143		imaplib
   Telnet	命令行					23		telnetlib
   Gopher	信息查找					70		gopherlib，urllib
   
第二十七章 Python3 SMTP发送邮件
00.SMTP(Simple Mail Transfer Protocal)即简单邮件传输协议，它是一组用于由源地址到目的地址传输邮件的规则，由它来控制邮件的中转方式。
   1）创建SMTP对象语法
   import smtplib
   smtpObj = smtplib.SMTP([host[,port[,local_hostname]]])
   参数说明：
   · host：SMTP服务器主机，IP或者域名，可选
   · port：提供了host参数，需要指定SMTP服务使用的端口号，一般情况下SMTP端口号为25.
   · local_hostname：如果SMTP在你的本机上，你只需要指定服务器地址为localhost即可。
   2）SMTP对象发送邮件语法：
   SMTP.sendmail(from_addr, to_addrs,msg[,mail_options,rcpt_options])
   参数说明：
   · from_addr: 邮件发送者地址
   · to_addrs：邮件接收地址，字符串列表
   · msg：邮件内容

第二十八章 多线程
00.多线程类似于同时执行多个不同程序，多线程有如下优点：
   · 使用线程可以把占据长时间的程序中的任务放到后台去处理。
   · 用户界面可以更加吸引人，比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理进度。
   · 程序的运行速度可能加快。
   · 在一些等待的任务实现上入用户输入、文件读写和网络收发数据等，线程比较有用。在这种情况下可以释放资源，如内存等。
   每个独立的线程有一个程序运行的入口、顺序执行序列和程序出口。但是线程不能独立运行，必须依存在应用程序中，有应用程序提供多个线程执行控制。
   每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反应了线程上次运行该线程的CPU寄存器的状态。
   指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。
   · 线程可以被抢占(中断)。
   · 在其他线程正在运行时，线程可以暂时搁置(也称睡眠)--这就是线程退让。
   线程可以分为：
   · 内核线程：由操作系统内核创建和撤销。
   · 用户线程：不需要内核支持而在用户程序中实现的线程。
   Python线程中常用_thread 和 threading(推荐)，_thread是python2的thread的重命名，
01.开始学习Python线程
   Python3中使用线程有两种方式：函数调用(start_new_thread())或者用类包装线程对象。
   _thread.start_new_thread(function,args[,kwargs])
   参数说明：function-线程函数。
            args-传递给线程函数的参数，tuple类型
			kwargs-可选参数
02.线程模块
   _thread提供了低级别的、原始的线程以及一个简单的锁，他相比于threading模块的功能还是比较有限的。
   threading模块除了包含_thread模块中的所有方法外，还提供其他方法
   · threading.currentThread(): 返回当前的线程变量
   · threading.emumerate()：返回一包含正在运行的线程的list。正在运行指线程启动后、结束前，不包含启动前和终止后的线程。
   · threading.activeCount()：返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
   除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法：
   · run()：用以表示线程活动的方法。
   · start()：启动线程活动。
   · join([time])：等待线程中止。这阻塞调用线程直至线程的join()方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
   · isAlive()：返回线程是否是活动的。
   · getName()：返回线程名。
   · setName()：设置线程名。
03.使用threading模块创建线程
   直接从threading.Thread继承创建一个新的子类，并实例化后调用start()方法启动新的线程，即它调用了现场的run()方法。
04.线程同步
   如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
   使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，可以直接将数据放到acquire和relase方法之间。
   多线程的优势在于可以同时运行多个任务(至少感觉起来是这样)。但是当线程需要共享数据时，可能存在数据不同步的问题。
   如：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
   那么线程"set"开始改的时候，线程"print"便来打印列表了，输出就有一部分0一部分是1，这就是数据不同步。为了避免这种情况，引入了锁的概念。
   锁有两种状态--锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。经过这样的处理，则不会再出现混淆的情况。
05.线程优先级队列(Queue)
   Queue模块中提供了同步的、线程安全的队列类，包括FIFO(先进先出)队列Queue，LIFO(后进先出)队列LifoQueue，和优先级队列PriorityQueue。
   这些队列都实现了锁原语，能够在线程中直接使用，可以使用队列来实现线程间的同步。
   Queue模块中的常用方法：
   · Queue.qsize() 返回队列的大小
   · Queue.empty() 如果队列为空，返回True，反之False
   · Queue.full() 如果队列满了，返回True
   · Queue.get([block[,timeout]) 获取队列timeout等待时间
   · Queue.get_nowait()相当于Queue.get(False)
   · Queue.put(itme) 写入队列
   · Queue.put_nowait(item)相当Queue.put(item,False)
   · Queue.task_done() 在完成一项工作之后，Queue.task_done()函数想任务已经完成的队列发送一个信号
   · Queue.join() 实际上意味着等到队列为空再执行别的操作。
   
第二十九章 Python XML解析
01.什么是XML？
   传输和存储数据
   定义语义的规则，将文档分成许多部件并对这些部件加以标识。
   也是元标记语言，即定义了用于定义其他与特定领域有关的、语义的、结构化的标记语言的句法语言。
02.Python对XML的解析
   常见的XML编程接口有DOM和SAX，这两种接口处理XML文件的方式不同，使用场合也不同。
   Python有三种解析方法：SAX，DOM，ElementTree
   1）SAX(simple API for XML)
      Python标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户自定义的回调函数来处理XML文件。
   2）DOM(Document Object Model)
      将XML数据在内存中解析成一颗数，通过对数的操作来操作XML.
03.使用SAX解析XML
   SAX是一种基于事件驱动的API。
   利用SAX解析XML文档涉及到两个部分：解析器和事件处理器
   解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
   事件处理器负责对事件作出响应，对传递的XML数据进行处理。
   ·1 对大型文件进行处理
   ·2 只需要文件的部分内容，或者只需从文件中得到特定信息
   ·3 想建立自己的对象模型的时候。
   处理时要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。
04.ContentHandler类方法介绍
   characters(content)方法
     从行开始，遇到标签之前，存在字符，content的值为这些字符。
     从一个标签，遇到下一个标签之前，存在字符，content的值为这些字符。
     从一个标签，遇到结束符之前，存在字符，content的值为这些字符。
     标签可以是开始标签，也可以是结束标签。
   startDocument()
     文档启动的时候调用
   endDocument()
     解析器到达文档结尾时调用
   startElment(name,attrs)	 
     遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
   endElement(name)
     遇到XML结束标签时调用
   make_parser
     创建并返回新的解析器对象
   parser
     创建SAX解析器并解析XML文档
     xml.sax.parse(xmlfile, contenthandler[, enrrohandler])
   parseString
     创建一个XML解析器并解析XML字符串
     xml.sax.parseString(xmlstring, contenthandler[, errorhandler])

第三十章 JSON数据解析
00.JSON(JavaScript Object Notation)是一种轻量级的数据交换格式，基于ECMAScript的一个子集。
   json模块对JSON数据进行编码、解码，它包含了两个函数：
   ·json.dumps()：对数据进行编码
   ·json.loads()：对数据进行解码
   在json编码过程中，python的原始类型与json类型会相互转换，具体转换对照如下：
   Python 编码为 JSON 类型转换对应表：
   Python								JSON
   dict									object
   list,tuple							array
   str									string
   int,float,int- & float-derived Emums	number
   True									true
   False								false
   None									null
   JSON 解码为 Python 类型转换对应表：
   JSON			Python
   object		dict
   array		list
   string		str
   number(int)	int
   number(real)	float
   true			True
   false		False
   null			None
   如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：
   
   实例(Python 3.0+)
   # 写入 JSON 数据
   with open('data.json', 'w') as f:
       json.dump(data, f)
    
   # 读取数据
   with open('data.json', 'r') as f:
       data = json.load(f)
	   
第三十一章 日期和时间
00.Python提供了一个time和calendar模块用于格式化日期和时间。
   时间间隔是以秒为单位的浮点小数。
   每个时间戳都以1970年1月1日午夜(历元)经过的时间来表示。
   Python的time模块下有很多函数可以转换常见日期格式，如time.time()用于获取当前时间戳。
01.时间元组
   很多Python函数用一个元组装起来的9组数字处理时间：
   序号		字段			属性			值
   0		4位数年		tm_year		2008	
   1		月			tm_mon		1 到 12
   2		日			tm-mday		1 到31
   3		小时			tm_hour		0 到 23
   4		分钟			tm_min		0 到 59
   5		秒			tm_sec		0 到 61(60或61是闰秒)
   6		一周的第几日	tm_wday		0 到 6(0是周一)
   7		一年的第几日	tm_yday		1 到 366
   8		夏令时		tm_isdst	1(夏令时)、0(非夏令时)、-1(未知)，默认-1
02.获取当前时间
   从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数
03.获取格式化的时间
   最简单的获取可读的时间模式的函数是asctime()
04.格式化日期
   使用time模块的strftime方法来格式化日期：
   time.strftime(format[, t])
   format格式化符号：
   · %y 两位数的年份(00-99)
   · %Y 四位数的年份(0000-9999)
   · %m 月份(01-12)
   · %d 月内中的一天(0-31)
   · %H 24小时制的小时数(0-23)
   · %I 12小时制的小时数(01-12)
   · %M 分钟数(00-59)
   · %S 秒(00-59)
   · %a 本地简化星期名称
   · %A 本地完整星期名称
   · %b 本地简化月份名称
   · %B 本地完整月份名称
   · %c 本地相应的日期和时间表示
   · %j 年内的一天(000-366)
   · %p 本地A.M.或P.M.的等价符
   · %U 一年中的星期数(00-53),星期天为星期的开始
   · %w 星期(0-6),星期天为星期的开始
   · %W 一年中的星期数(00-53),星期一为星期的开始
   · %x 本地相应的日期表示
   · %X 本地相应的时间表示
   · %Z 当前时区的名称
   · %% 表示%号本身
05.获取某月日历
   Calendar模块有很广泛的方法来处理年历和月历，例如打印某月的月历：
06.Time模块
   函数							描述
   1）time.altzone					返回格林威治西部的夏令时地区的偏移秒数，如果该地区在格林威治东部返回负值，对夏令时启用地区才能使用。
   2）time.asctime([tupletime])	接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"(2008年12月11日 周二18时07分14秒)的24个字节的字符串 
   3）time.clock()
   用以浮点数计算的秒数返回当前cpu的时间。用来衡量不同程序的耗时，比time.time()更有用
   4）time.ctime([secs])
   作用相当于asctime(localtime(secs)),未给参数相当于asctime()
   5）time.gmtime([secs])
   接收时间戳(1970纪元后经过的浮点秒数)并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
   6）time.localtime([secs])
   接收时间戳返回当地时间下的时间元组t
   7）time.mktime(tupletime)
   接受时间元组返回时间戳
   8）time.sleep(secs)
   推迟调用线程的运行，secs指秒数
   9）time.strftime(fmt[,tupletime])
   接收时间元组，返回可以读字符串表示的当地时间，格式有fmt决定。
   10）time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
   根据fmt的格式把一个时间字符串解析为时间元组
   11）time.time()
   返回当前时间的时间戳
   12）time.tsize()
   根据环境变量TZ重新初始化时间相关设置
   13）time.perf_counter()
   返回计时器的精确时间(系统的运行时间)，包含整个系统睡眠时间。由于返回值的基准点是未定义的所以，只有连续调用的结果之间的差才是有效的。
   14）time.process_time()
   返回当前进程执行CPU时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间才是有效的
   Time模块包含两非常重要的属性：
   1）time.timezone
   当地时区，距格林威治的偏移秒数(>0,美洲;<=0大部分欧洲、亚洲、非洲)
   2）time.tname
   包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称
07.日历(Calendar)模块
   1）calendar.calendar(year,w=2,l=1,c=6)
   返回一个多行字符串格式的year年历，3个月一行，间隔距离为c。每日宽度间隔为w字符。每行长度为21*w+18+2*c。l是每星期行数。
   2）calendar。firstweekday()
   返回当前每周起始日期的设置。默认情况下首次载入calendar模块时返回0，即星期一。
   3）calendar.isleap(year)
   闰年返回True
   4）calendar.leapdays(y1,y2)
   返回在y1，y2两个年之间的闰年总数。
   5）calendar.month(year,month,w=2,l=2)
   返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行长度为7*w+6。

   6）calendar。monthcalendar(year,month)
   返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月的日期都设为0；范围内的日子都由该月第几日表示，从1开始。
   7）calendar.monthrange(year,month)
   返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0(星期一)到6(星期日)。
   8）calendar.prcal(year,w=2,l=1,c=6)
   相当于print calendar.calendar(year,w,l,c)
   9）calendar.prmonth(year,w=2,l=1)
   相当于 print calendar.calendar（year，w，l，c）。
   10）calendar.setfirstweekday(weekday)
   设置每周的起始日期码。0（星期一）到6（星期日）。
   11）calendar.timegm(tupletime)
   和time.gmtime相反：接受一个时间元组，返回该时刻的时间戳
   12）calendar.weekday(year,month,day)
   返回给定日期的日期码。0(星期一)到6(星期日)。月份为1(一月)到12(12月)。

第三十二章 内置函数
   1）abs()
   2) all()
   3) any()
   4) ascii()
   5) bin()
   6) bool()
   7) bytearray()
   8) bytes()
   9) callable()
   10) char()
   11) classmethod()
   12) compile()
   13) complex()
   14) delattr()
   15) dict()
   16) dir()
   17) divmode()
   18) enumerate()
   19) eval()
   20) exec()
   21) filter()
   22) float()
   23) format()
   24) frozenset()
   25) getattr()
   26) globals()
   27) hasattr()
   28) hash()
   29) help()
   30) hex()
   31) id()
   32) input()
   33) int()
   34) isinstance()
   35) issubclass()
   36) iter()
   37) len()
   38) list()
   39) locals()
   40) map()
   41) max()
   42) memoryview()
   43) min()
   44) next()
   45) object()
   46) oct()
   47) open()
   48) ord()
   49) pow()
   50) print()
   51) property()
   52) range()
   53) repr()
   54) reversed()
   55) round()
   56) set()
   57) setattr()
   58) slice()
   59) sorted()
   60) staticmethod()
   61) str()
   62) sum()
   63) super()
   64) tuple()
   65) type()
   66) vars()
   67) zip()
   68) __import__()
第三十三章 GUI编程(Tkinter)
01.Tkinter编程
   Tkinter是内置到python的安装包中，只需导入可以快速创建GUI应用程序。
   IDLE也是用Tkinter编写而成，对于简单的图形界面能够应付自如。
   Python3.x版本使用的库名为tkinter，即首字母T为小写。
   创建GUI程序的流程：
   ·1、导入tkinter模块。
   ·2、创建控件。
   ·3、指定这个控件的master，即这个控件属于哪个控件。
   ·4、告诉GM(geometry manager)有一个控件产生了。
02.tkinter组件
   目前有15种tkinter组件(Python2.x)：
   序号	控件			描述
   01	Button		按钮控件；在程序中显示按钮
   02	Canvas		画布控件；显示图形元素，如线条或文本
   03	Checkbutton	多选框控件；用于在程序中提供多项选择框
   04	Entry		输入控件；用于显示简单的文本内容
   05	Frame		框架控件；在屏幕上显示一个矩形区域，多用来作为容器
   06	Label		标签控件；可以显示文本和位图
   07	Listbox		列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
   08	Menubutton	菜单按钮；显示菜单栏、下拉菜单和弹出菜单
   09	Message		消息控件；用来显示多行文本，与label比较类似
   10	Radiobutton	单选按钮；
   11	Scale		范围控件；显示一个数值刻度，为输出限定范围的数字区间
   12	Scroobar	滚动条控件；当内容超过可视化区域时使用，如列表框
   13	Text		文本控件；用于显示多行文本
   14	Toplevel	容器控件；用来提供一个单独的对话框，和Frame比较类似
   15	Spinbox		输入控件；与Entry类似，但是可以指定输入范围值
   16	PanedWindow	窗口布局管理插件，可以包含一个或者多个子控件
   17	LabelFrame	简单的容器控件；常用于复杂的窗口布局
   18	tkMessageBox用于显示应用程序的消息框
03.标准属性(所有控件的共同属性)
   属性		描述
   Dimension控件大小
   Color	颜色
   Font		字体
   Anchor	锚点
   Relief	控件样式
   Bitmap	位图
   Cursor	光标
04.几何管理(布局管理)
   tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，包括包、网格、位置三个公开的管理类
   
第三十四章 NumPy应用   
00.NumPy通常与SciPy(Scientific Python)和Matplotlib(会图库)一起使用，这种组合广泛用于替代MatLab，是一个强度的科学计算环境，有助于学习数学科学或者机器学习。
   SciPy是一个开源的Python算法库和数学工具包。
   SciPy包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、厂微分方程和其他科学与工程中常用的计算。
   Mapplotlib是Python编程语言及其数值数学扩展包NumPy的可视化操作界面。它为利用通用的图形用户界面工具包，如tkinter、wxPython、Qt或GTK+向应用程序嵌入式绘图提供了应用程序接口
   NumPy是一个运行速度非常快的数学库，主要用于数组计算，包含：
    · 一个强大的N维数组对象ndarray
	· 广播功能函数
	· 整合C/C++/Fortran代码的工具
	· 线性代数、傅里叶变换、随机数生成等功能
01.NumPy安装
   1、使用已有的发行版本
   2、使用pip安装
      python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
	  --user选项可以设置只安装在当前的用户下，而不是写入系统目录
   3、安装验证
      from numpy import *
	  eye(4)
   4、Numpy Ndarray对象
      Numpy最重要的一个特点是其N维数组对象ndarray，它是一系列同类型数据的集合，以0下标为开始进行集合中元素的索引。
	  ndarray对象用于存放同类型元素的多维数组
	  ndarray中的每个元素在内存中都有相同存储大小的区域。
	  ndarray内部又以下内容组成：
	     ·一个指向数据(内存或内存映射文件中的一块数据)的指针。
		 ·数据类型或dtype，描述在数组中的固定大小值的格子。
		 ·一个表示数组形状(shape)的元组，表示各维度大小的元组。
		 ·一个跨度元组(stride),其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。
   5、创建ndarray的语法：
      numpy.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)
	  · object	数组或嵌套的数列
	  · dtype	数组元素的数据类型，可选
	  · copy	对象是否需要复制，可选
	  · order	创建数组的样式，C为行方向，F为列方向，A为任意方向(默认)
	  · subok	默认返回一个与基类型一致的数组
	  · ndmin	指定生成数组的最小维度
	  ndarray对象由计算机内存连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置内存块以行顺序(C样式)或列顺序(FORTRAN或MatLab风格，即前述的F样式)来保存元素。
   6、NumPy数据类型
      numpy支持的数据类型比Python内置类型要多很多，基本上可以和C语言的数据类型对应上，其中部分类型对应为Python内置的类型，常用基本类型如下表：
	  名称		描述
	  bool_		布尔数据类型（True或者False）
	  int_		默认的整数类型(类似于C语言的long、int32或int64)
	  intc		与C的int类型一样，一般是int32或int64
	  intp		用于索引的整数类型(类似于C的ssize_t，一般情况下仍然是int32或int64)
	  int8		字节(-128 头127)
	  int16		整数(-32768 to 32767)
	  int32		整数(-2147483648 to 2147483647)
	  int64		整数(-9223372036854775808 to 9223372036854775807)
	  uint8		无符号整数(0 to 255)
	  uint16	无符号整数(0 to 65535)
	  uint32	无符号整数(0 to 4294967295)
	  uint64	无符号整数（0 to 18446744073709551615）
	  float_	float64类型的简写
	  float16	半精度浮点数，包括：1个符号位，5个指数位，10个尾数位。
	  float32	半精度浮点数，包括：1个符号位，8个指数位，23个尾数位。
	  float64	半精度浮点数，包括：1个符号位，11个指数位，52个尾数位。
	  complex_	complex128类型的简写，即128位复数
	  complex64 复数，表示双32位浮点数(实数部分和虚数部分)
	  complex128复数，表示双64位浮点数(实数部分和虚数部分)
   7、数据类型对象(dtype)
      · 数据的类型(整数、浮点数或者Python对象)
	  · 数据的大小(例如，整数使用多少个字节存储)
	  · 数据的字节顺序(小端法或大端法)
	  · 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
	  · 如果数据类型是子数组，它的形状和数据类型
	  字节顺序是通过对数据类型预先设定 "<" 或 ">" 来决定的。"<" 意味着小端法(最小值存储在最先的地址，即低位组放在最前面)。">" 意味着大端法(最大的数值存储在最小的地址，即高位组放在最前面)。
	  dtype对象使用以下语法构造：
	   numpy.dtype(object,align,copy)
	   ·object - 要转换为的数据类型对象
	   ·align - 如果为true，填充字段使其类似C的结构体。
	   ·copy - 复制dtype对象，如果为false，zeshi对内置数据类型对象的引用
	  每个内建类型都有一个唯一定义它的字符代码，如下：
	  字符	对应类型
	  b 	布尔型
	  i 	(有符号)整型
	  u 	(无符号)整型
	  f 	浮点型
	  c 	复数浮点型
	  m	 	timedelta(时间间隔)
	  M 	diatetime(日期时间)
	  O 	(Python)对象
	  S,a 	(byte-)字符串
	  U		Unicode
	  V		原始数据(void)
   8、NumPy数组属性
      维数称为秩(rank)，一维数组的秩为1，二维数组的秩为2，以此类推。
	  在NumPy中，每一个线性的数组称为是一个轴(axis)，也就是维度(dimensions)。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所有一维数组就是NumPy中的轴(axis)，第一个轴相当于底层数组，第二个轴是底层数组里数组。而轴的数量--秩就是数组的维数。
	  很多时候可以声明axis。axis=0，表示沿着第0轴进行操作，即对每一列进行操作；axis=1，表示沿着第一轴进行操作，即对每一行操作。
	  NumPy的数组中比较重要的ndarray对象属性有：
	  属性			说明
	  ndarray.ndim	秩，即轴的数量或维度的数量
	  ndarray.shape	数组的维度，对于矩阵，n行m列
	  ndarray.size	数组元素的总个数，相当于.shape中的n*m的值
	  ndarray.dtype	对象的元素类型
	  ndarray.itemsize 对象中每个元素的大小，以字节为单位
	  ndarray.flags	对象的内存信息
	  ndarray.real	元素的实部
	  ndarray.imag	元素的虚部
	  ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性
	  NumPy 也提供了 reshape 函数来调整数组大小
	  ndarray.flags返回ndarray对象的内存信息，包含以下属性：
	  属性				描述
	  C_CONTIGUOUS(C)	数据是在一个单一的C风格的连续段中
	  F_CONTIGUOUS(F)	数据是在一个单一的Fortran风格的连续段中
	  OWNDATA(0)		数组拥有它所使用的内存或从另一个对象中借用它
	  WRITEABLE(W)		数据区域可以被写入，将该值设置为False，则数据为只读
	  ALIGNED(A)		数据和所有元素都适当地对齐到硬件上
	  UPDATEIFCOPY(U)	这个数组是其他数组的一个副本，当这个数组被释放时，原数组的内容将被更新
   8、NumPy创建数组
      ndarray数组除了可以使用底层ndarray构造器来创建外，也可以通过以下几种方式来创建
	  numpy.empty
	  创建指定形状(shape)、数据类型(dtype)且未初始化的数组：
	  numpy.empty（shape,dtype=float,order='C')
	  numpy.zeros
	  创建指定大小的数组，数组元素以 0 来填充
	  numpy.zeros(shape, dtype = float, order = 'C')	  
	  numpy.ones
	  创建指定形状的数组，数组元素以 1 来填充：
	  numpy.ones(shape, dtype = None, order = 'C')
   9、从已有数组创建数组
      numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个
	  numpy.asarray(a, dtype=None, order=None)
	  a -- 任意形式的输入参数，可以是列表、列表的元组、元组、元组的元组、元组的列表、多维数组
	  dtype -- 数据类型，可选
	  order -- 可选，有C和F两个选项，分别代表行优先和列优先，表示在计算机内存中的存储元素的顺序。
	  numpy.frombuffer
	  用于实现动态数组
	  接受buffer输入参数，以流的形式转化成ndarray对象。
	  numpy.frombuffer(buffer,dtype=float,count=-1,offset=0)
	  注意：buffer是字符串的时候，Python3默认str是Unicode类型，所以要转成bytestring，在原str前加上b。
	  参数说明：
	  buffer	可以是任意对象，会以流的形式读入。
	  dtype		返回数组的数据类型，可选。
	  count		读取的数据数量，默认为-1，读取所有数据。
	  offset	读取的起始位置，默认为0.
   9、从迭代对象创建数组
      numpy.frommiter(iterable, dtype, count = -1)
   10.从数值范围创建数组
      numpy.arange(start, stop, step, dtype)
	  参数说明：
	  start		起始值，默认为0
	  stop		终止值(不包含)
	  step		步长，默认为1
	  dtype		返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
   11.用函数创建数组
      numpy.linspace(start,stop,num=50,endpoint=true,retstep=False,dtype=None)
	  参数说明：
	  start		序列的起始位置
	  stop		序列的终止位置，如果endpoint为true，该值包含于数列中。
	  num		要生成的等步长的样本数量，默认为50.
	  endpoint	该值为true时，数列中包含stop值，反之不包含，默认是true
	  retstep	如果为true时，生成的数组中会显示间距，反之不显示。
	  dtype		ndarray的数据类型
   12.用函数创建等比数列
      np.logspace(start,stop,num=50,endpoint=true,base=10.0,dtype=None)
	  base参数意思是取对数的时候log的下标：
	  参数		描述
	  start		序列的起始值为：base**start
	  stop		序列的终止值为：base**stop. 如果endpoint为true，该值包含于数列中
	  num		要生成的等步长的样本数量，默认为50
	  endpoint	该值为True时，数列中包含stop值，反之不包含，默认是True。
	  base		对数log的底数
	  dtype		ndarray的数据类型
   13.NumPy切片和索引
      ndarray对象的内容可以通过索引或切片来访问和修改，与Python中list的切片操作一样。
	  ndarray数组可以基于0-n的下标进行索引，切片对象可以通过内置的slice函数，并设置start，stop及step参数进行，从原数组中切割出一个新数组。
	  也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作：索引从0开始，不包括结束位置。
	  如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。如果为 [2:]，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
	  适用于多维数组
	  切片还可以包含省略号…，来使选择元组的长度与数组的维度相同。如果在行位置使用省略号，它将返回包含行中元素的ndarray。
   14.NumPy的高级索引
      NumPy比一般的Python序列提供更多的索引方式。除了之前看到的用整数和切片索引之外，数组可以由整数数组索引、布尔索引及花式索引。
	  1）整数数组索引
	  ……
   15.NumPy广播(Broadcast)
      广播是numpy对不同形状的数组进行数值计算的方式，对数组的算术运算通常在相应的元素上进行。
	  如果两数组a和b形状相同，即满足a.shape==b.shape，那么a*b的结果就是a与b数组对应位相乘。这要求维数相同，且各维度的长度相同。
	  广播的规则：
	  · 让所有输入数组都向其中形状最长的数组看齐，形状中不足部分都通过在前面加1补齐。
	  · 输出数组的形状是输入数组形状的各个维度上的最大值。
	  · 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为1时，这个数组能够用来计算，否则出错。
	  · 当输入数组的某个维度的长度为1时，沿着此维度运算时都用此维度上的第一组值。
	  简单理解：对两个数组，分别比较他们的每一个维度(若其中一个数组没有当前维度则忽略)，满足：
	  · 数组拥有相同的形状。
	  · 当前维度的值相等。
	  · 当前维度的值有一个1.
	  若条件不满足，抛出"ValueError:frames are not aligned"异常。
   16.NumPy迭代数组
      NumPy迭代器对象NumPy.nditer提供了一种零活访问一个或者多个数组元素的方式。
	  迭代器最基本的任务是可以完成对数组元素的访问。
   17.Numpy数组操作
      NumPy中包含了一些函数用于处理数组，大概可以分为以下几类：
	  · 修改数组形状
	  · 翻转数组
	  · 修改数组维度
	  · 连接数组
	  · 分隔数组
	  · 数组元素的添加和删除
	  1）修改数组形状：
	  函数		描述
	  reshape	不改变数据的条件下修改形状
	  flat		数组元素迭代
	  flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
	  ravel		返回展开数组
	  NumPy.reshape(arr,newshape,order='c')
	  · arr:要修改形状的数组
	  · newshape:整数或整数数组，新的形状应当兼容原有形状
	  · order：'C'--按行，'F'--按列，'A'--原顺序，'k'--元素在内存中出现的顺序。
	  2）翻转数组
	  函数		描述
	  transpose	对换数组的维度
	  ndarray.T	和self.transpose()相同
	  rollaxis	向后滚动指定的轴
	  swapaxes	对换数组的两个轴
      3）修改数组维度
	  维度			描述
	  broadcast		产生模仿广播的对象
	  broadcast_to	将数组广播到新形状
	  expand_dims	扩展数组的形状
	  squeeze		从数组的形状中删除一维条目
	  4）连接数组
	  函数			描述
	  concatenate	连接沿现有的数组序列
	  stack			沿着新的轴加入一系列数组
	  hstack		水平堆叠序列中的数组(列方向)
	  vstack		竖直堆叠序列中的数组(行方向)
	  5）分割数组
	  函数			描述
	  split			将一个数组分割为多个子数组
	  hsplit			将一个数组水平分割为多个子数组（按列）
	  vsplit			将一个数组垂直分割为多个子数组（按行）
	  6）数组元素的添加与删除
	  函数		元素及描述
	  resize	返回指定形状的新数组
	  append	将值添加到数组末尾
	  insert	沿指定轴将值插入到指定下标之前
	  delete	删掉某个轴的子数组，并返回删除后的新数组
	  unique	查找数组内的唯一元素
	  7）NumPy位运算
	  NumPy中"bitwise_"开头的函数是位运算函数
	  函数			描述
	  bitwise_and	对数组元素执行位与操作
	  bitwise_or	对数组元素执行位或操作
	  invert		按位取反
	  left_shift	向左移动二进制表示的位
	  right_shift	向右移动二进制表示的位
	  注：也可以使用"&"、"~"、"|"和"^"等操作符进行计算
	  8）NumPy字符串函数
	  以下函数用于对dtype为numpy.string_或numpy.unicode_的数组执行向量化字符串操作。它们基于Python内置库中的标准字符串函数。
	  这些函数在字符数组类（numpy.char）中定义
	  函数		描述
	  add()		对两个数组的逐个字符串进行连接
	  multiply	返回按元素多重连接后的字符串
	  center	居中安字符串
	  capitalize将字符串第一个字母转换为大写
	  title		将字符串的每个单词的第一个字母转换为大写
	  lower		数组元素转换为小写
	  upper		数组元素转换为大写
	  split		指定分隔符对字符串进行分割，并返回数组列表
	  splitlines返回元素中的行列表，以换行符分割
	  strip		移除元素开头或者结尾处的特定字符
	  join		通过指定分割符来连接数组中的元素
	  replace	使用新字符串替换字符串中的所有子字符串
	  decode		数组元素依次调用str.decode
	  encode	数组元素依次调用str.encode
	  18.NumPy数学函数
	  NumPy包含大量的各种数学运算的函数，包括三角函数、算术运算函数、复数处理函数等
	  1）NumPy算术函数
	  包含简单的加减乘除：add(),substract(),multiply()和divide()
	  需要注意的是数组必须具有相同的形状或符合数组广播规则
	  2）NumPy统计函数
	  NumPy提供了很多统计函数，用于从数组中查找最小元素amin，最大元素amax，百分位标准差ptp和方差percentile
	  numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）
	  numpy.percentile(a,q,axis)表示小于这个值的观察值的百分比，百分位数是统计中使用的度量。
	  a: 输入数组
	  q: 要计算的百分位数，在0~100之间
	  axis：沿着它计算百分位数的轴，
	  百分位数：第p个百分位数是这样一个值，它使得至少有p%的数据项小于或等于这个值，且至少有(100-p)%的数据项大于或等于这个值。
	  举个例子：高等院校的入学考试成绩经常以百分位数的形式报告。比如，假设某个考生在入学考试中的语文部分的原始分数为54分。相对于参加统一考试的其他学生来说，他的成绩如何并不容易知道。但是如果原始分数54fen恰好对应的是第70百分位数，我们就能知道大约70%的考生的考分比他低，而约30%的学生考分比他高。这里的p=70.
	  numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。	  
	  该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。	  
	  加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。	  
	  考虑数组[1,2,3,4]和相应的权重[4,3,2,1]，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
	  标准差是一组数据平均值分散程度的一种度量。
	  方差
	  统计中的方差(样本方差)是每个样本值与全体样本值的平均数之差的平方值的平均数，即mean((x-x.mean())**2)
	  换句话说，标准差是方差的平方根
	  3）NumPy排序、条件筛选函数
	  NumPy提供了多种排序方法，这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。
	  种类					速度		最坏情况		工作空间		稳定性
	  quicksort快速排序		1		0(n^2)		0			否
	  mergesort归并排序		2		0(n#log(n))	~n/2		是
	  heapsort堆排序			3		0(n*log(n))	0			否
	  · numpy.sort(a,axis,king,order) 返回输入数组的排序副本
	    a: 要排序的数组
		axis：沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序，axis=0按列排序，axis=1按行排序
		king：默认为quicksort(快速排序)
		order：如果数组包含字段，则是要排序的字段
	  · numpy.argsort()返回数组值从小到大的索引值
	  · numpy.lexsort()
	    用于对多个序列排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
		举例应用场景：小升初考试，重点班录取学生按照总成绩录取，在总成绩相同时，数学成绩高的优先录取，在总成绩和数据成绩都相同时，按照英语成绩录取……这里，总成绩排在电子表格的最后一列，数学成绩在倒数第二列，英语成绩在倒数第三列。
	  4）NumPy字节交换
	  在几乎所有的机器上，多字节对象都被存储为连续的字节序列。字节顺序，是跨越多字节的程序对象的存储规则。
	  · 大端模式：指数据的高字节保存在内存的低地址中，而数据的低字节保存在内存的高地址中，这样的存储模式有点类似于把数据当做字符串顺序处理：地址由小向大增加，而数据从高位往低位放；这和我们的阅读习惯一致。
	  · 小端模式：指数据的高字节保存在内存的高地址中，而数据的低字节保存在内存的低地址中，这种存储模式将地址的高低和数据位权有效地结合起来，高地址部分权值高，低地址部分权值低。
	  例如在C语言中，一个类型为int的变量x地址为0x100，那么其对应地址表达式&x的值为0x100.且x的四个字节将被存储在存储器的0x100，0x101，0x102，0x103位置。
	  numpy.ndarray.byteswap()函数将ndarray中的每个元素中的字节进行daxiaoduan转换。
      5）NumPy副本和视图
	  副本是一个数据的完整拷贝，如果我们对副本进行修改，它不会影响原始数据，物理内存不在同一位置。
	  视图是数据的一个别称或引用，通过该别称或引用便可访问、操作原始数据，但原始数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。
	  视图一般发生在：
		· 1. NumPy的切片操作返回源数据视图。
		· 2. 调用ndarray的view()函数产生一个视图。
	  副本一般发生在：
		· python序列的切片操作，调用deepCopy函数
		· 调用ndarray的copy()函数产生一个副本。
	  无复制
	  简单的赋值不会创建数组对象的副本。相反，它使用原始数据的相同id()来访问它。id()返回Python对象的通用标识符，类似于C中的指针。
	  此外，一个数组的任何变化都反应在另一个数组上。例如，一个数组的形状改变也会改变另一个数组的形状。
   19.NumPy矩阵库(Matrix)
      NumPy中包含了一个矩阵库numpy.matlib,该模块中的函数返回的是一个矩阵，而不是ndarray对象
	  一个m×n的矩阵是一个由m行(row)n列(column)元素排列成的矩形阵列。
	  矩阵里的元素可以是数字、符合或数学式。
	  numpy.matlib.empty(shape,dtype,order)返回一个新的矩阵,内容是随机数
	  numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵
	  numpy.matlib.eye(n, M,k, dtype) 函数返回一个矩阵，对角线元素为 1，其他位置为零
	  numpy.matlib.identity() 函数返回给定大小的单位矩阵，单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0
	  numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
	  矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
   20.线性代数
      线性代数库的函数
	  函数			描述
	  dot			两个数组的点积，即元素对应相乘
	  vdot			两个向量的点积
	  inner			两个数组的内积
	  matmul		两个数组的矩阵积
	  determinant	数组的行列式
	  solve			求解线性矩阵方程
	  inv			计算矩阵的乘法逆矩阵
   21.Numpy IO
      Numpy可以读写磁盘上的文本数据或二进制数据。
	  NumPyweindarray对象引入了一个简单的文件格式：npy。
	  npy文件用于存储重建ndarray所需的数据、图形、dtype和其他信息。
	  常用的IO函数有：
	  · load(flie)和save(file, arr, allow_pickle=True, fix_imports=True)函数是读写文件数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中。
	  · savze(file, *args, **kwds)函数用于将多个数组写入文件，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为.npz的文件中。
	  · loadtxt()和savetxt()函数处理正常的文本文件(.txt等)
第三十五章 Matplotlib应用
   1. Windows系统安装Matplotlib
   2. 显示中文的设置
      # 在我的 notebook 里，要设置下面两行才能显示中文
	  plt.rcParams['font.family'] = ['sans-serif']
	  # 如果是在 PyCharm 里，只要下面一行，上面的一行可以删除
	  plt.rcParams['font.sans-serif'] = ['SimHei']
   3. pylab模式
	  pylab是matplotlib面向对象绘图库的一个接口。它的语法和Matlab十分相近。
	  Matplotlib的默认设置都允许用户自定义。你可以调整大多数的默认配置：
	  · 图片大小和分辨率(dpi)
	  · 线宽
	  · 颜色
	  · 风格
	  · 坐标轴
	  · 网格属性
	  · 文字与字体属性等
   4. 图像、子图、坐标轴和记号
      可以显示地控制图像、子图、坐标轴。Matplotlib中的图像指的是用户界面看到的整个窗口内容。在图像里有所谓子图。子图的位置是由坐标网格确定的，而【坐标轴】却不受此限制，可以放在图像的任意位置。
	  隐式使用图像和子图时，matplotlib调用gca()函数以及gcf()函数来获取当前的坐标轴和图像，如果无法获取图像，则会调用figure()函数来创建一个---严格地说，是用subplot(1,1,1)创建一个只有一个子图的图像。
   5. 图像
      所谓图像，就是GUI里以[Figure#]为标题的那些窗口。图像编号从1开始，与MATLAB的风格一致，而与Python从0开始编号的风格不同。以下是图像的属性：
	  参数		默认值			描述
	  num		1				图像的数量
	  figsize	figure.figsize	图像的长和宽(英寸)
	  dpi		figure.dpi		分辨率(点/英寸)
	  facecolor	figure.facecolor绘图区域的背景颜色
	  edgecolor	figure.edgecolor绘图区域的边缘颜色
	  frameon	True			是否绘制图像边缘
	  这些默认值可以在源文件中指明。不过除了图像数量这个参数，其余的参数很少修改。
	  在图形界面中可以按右上角的X来关闭窗口。Maplotlib也提供了名为close的函数来关闭这个窗口。close函数的具体行为取决于你提供的参数：
		1.不传递参数，关闭当前窗口；
		2.传递窗口编号或窗口实例（instance）作为参数：关闭指定窗口；
		3.all：关闭所有窗口。
	  和其他对象一样，可以使用setp或者set_something这样的方法来设置图像的属性。
   6. 子图
      可以使用子图来将图样(plot)均匀的放在坐标网格中。用subplot函数的时候，你需要指明网格的行列数量，以及你希望将图样放在哪一个网格区域中。此外，gridspec的功能更强大，可以实现这个功能。
#用时39天	  
#########################################
## 标题：PythonStart 入门               #
## 时间：2019/10/15 开始                #
########################################





#########################################
## 标题：Linux 入门                     #
## 时间：2019/10/15 开始                #
#########################################
01. Linux系统启动过程
	01）系统启动过程
	· 内核引导
	· 运行init
	· 系统初始化
	· 建立终端
	· 用户登录系统
	02）内核引导
		当打开计算机电源后，首先是BIOS开机自检，安照BIOS中设置的启动设备(通常是硬盘)来启动
		操作系统接管硬件以后，首先读入/boot目录下的内核文件。
	03）运行init
		init进程是系统所有进程的起点，可以把它比拟成系统所有进程的老祖宗，没有这个进程，系统中任何进程都不会启动。
		init程序首先是需要读取配置文件/etc/inittab
	04）运行级别
		许多程序需要开机启动。他们在Windows叫做服务(service)，在Linux就叫做"守护进程"(deamon)。
		init进程的一大任务，就是去运行这些开机启动的程序。
		但是，不同场合需要启动不同的程序，比如用作服务器时，需要启动Apache，用作桌面就不需要。
		Linux允许为不同场合，分配不同的开机启动程序，这就叫做"运行级别"(runlevel)。也就是说，启动是根据"运行级别"，确定要运行哪些程序。
		Linux系统有7个运行级别：
			· 运行级别0：系统停机状态，系统默认运行级别不能设置为0，否则不能正常启动。
			· 运行级别1：单用户工作状态，root权限，用户系统维护，禁止远程登录
			· 运行级别2：多用户状态(没有NFS)
			· 运行级别3：完全的多用户状态(有NFS)，登录后进入控制台命令行模式
			· 运行级别4：系统未使用，保留
			· 运行级别5：X11控制台，登录后进入图形GUI模式
			· 运行级别6：系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动
	05）系统初始化
		在init配置文件中有这么一行：si::sysinit:/etc/rc.d/rc.sysinit 它调用执行了/etc/rc.d/rc.sysinit，而rc.sysinit是一个bash shell脚本，它主要是完成一些系统初始化的工作，rc.sysinit是每一个运行级别都要首先运行的重要脚本。
		它主要完成的工作有：激活交换分区，检查磁盘，加载硬件模块以及其他一些需要优先执行的任务。
		当init改变运行级别时，所有相关的守护进程都将重启。
		可以通过chkconfig或setup中的'System Services'来自行设定。
	06）建立终端
		rc执行完毕后，返回init。这时基本系统环境已经设置好了，各种守护进程也已经启动了
		init接下来会打开6个终端，以便用户登录。zaiinittab中的以下6个终端
		1:2345:respawn:/sbin/mingetty tty1
		2:2345:respawn:/sbin/mingetty tty2
		3:2345:respawn:/sbin/mingetty tty3
		4:2345:respawn:/sbin/mingetty tty4
		5:2345:respawn:/sbin/mingetty tty5
		6:2345:respawn:/sbin/mingetty tty6
		同时它会显示一个文本登录界面，就是我们经常看到的登录界面，提示用户输入用户名，用户输入的用户名将作为参数传给login程序来验证用户的身份。
	07）用户登录
		· （1）命令行登录
		· （2）ssh登录
		· （3）图像界面登录
		对于运行级别为5的图形方式用户来说，他们的登录是通过一个图形化的登录界面。登录成功后可以直接进行入KDE、Gnome等窗口管理器。
		Linux的账号验证程序是login，login会接收mingetty传来的用户名作为用户名参数，然后login会对用户名进行分析：如果用户名不是root，且存在/etc/nologin文件，login将输出nologin文件的内容，然后退出。
		这通常用来在系统维护时防止非root用户登录。只有/etc/securetty中登录了的终端才允许root用户登录，如果不存在这个文件，则root用户可以在任何终端上登录。
		/etc/usertty文件用于对用户做出附加访问限制，如果不存在这个文件，则没有其他限制。
	08）图形模式与文字模式的切换方式
		Linux预设停了六个命令窗口终端机让我们来登录。
		默认我们的登录的就是第一个窗口，也就是tty1，这六个窗口分别为tty1,tty2...tty6，你可以按下Ctrl+Alt+F1~F6来切换它们。
		如果你安装了图形界面，默认情况下是进入图形界面的，此时你就可以按Ctrl+Alt+F1~F6来进入其中一个命令窗口界面。
		当你记进入命令窗口界面后再返回图形界面只有按下Ctrl+Alt+F7就回来了。
		如果你有的wmware虚拟机，命令窗口切换的快捷键为Alt+Space+F1~F6。如果你在图形界面请按Alt + Shift + Ctrl + F1~F6切换至命令窗口。
	09）Linux关机
		在Linux领域内大多用在服务器上，很少遇到关机操作。毕竟服务器上跑一个服务是永无止境的，除非特殊情况下，不得已才会关机。
		正确的关机流程为：sync > shutdown > reboot > halt
		sync  将数据由内存同步到硬盘中
		shutdown  关机指令，
		shutdown -h 10 'This server will shutdown after 10 mins'  # 这个命令告诉大家，计算机将在10分钟后关机，并且会显示在登录用户的当前屏幕中
		shutdown -h now  # 立马关机
		shutdown -h 20:25  # 系统会在今天20:25关机
		shutdown -h +10  # 十分钟后关机
		shutdown -r now  # 系统立刻重启
		reboot  # 就是重启，等同于shutdown -r now
		halt  #关闭系统，等同于shutdown -h now 和 poweroff
		不管是重启系统还是关闭系统，首先要运行sysnc命令，把内存中的数据写到磁盘中。
		关机的命令有：
		shutdown -h now
		halt
		poweroff
		init0
		重启系统的命令有：
		shutdown -r now
		reboot
		init6
02. Linux系统目录结构
	· /bin: bin是binary的缩写，这个目录存放着最经常使用的命令。
	· /boot: 启动Linux时使用的一些核心文件，包括以下连接文件以及镜像文件
	· /dev: dev是Device(设备)的缩写，存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。
	· /etc: 存放所有的系统管理所需的配置文件和子目录
	· /home: 用户的主目录，在Linux中，每个用户都有一个自己的子目录，一般该目录名是以用户的账号命名的。
	· /lib: 存放系统最基本的动态连接共享库，其作用类似于windows里的dll文件。几乎所有的应用程序都需要用到这些共享库
	· /lost+found: 这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。
	· /media: Linux会自动识别一些设备，例如U盘、光驱等，当识别后，Linux会把识别的设备挂载到这个目录下。
	· /mnt: 系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。
	· /opt: 这是给主机额外安装软件所设置的目录，比如你安装一个ORACLE数据库则就可以放到这个目录下，默认是空的。
	· /proc: 这个目录是虚拟目录，它是系统内存的映射，我们可以退通过直接访问这个目录来获取系统信息。这个目录的内容不在硬盘上而是在内存里，我们可以直接修改里面的某些文件，比如可以通过下面的命令来屏蔽主机的ping命令，是别人无法ping你的机器
	· /root: 该目录是系统管理员，也称作超级权限者的用户主目录。
	· /sbin: s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。
	· /selinux: 这个目录是Redhat/CentOS所特有的目录，Selinux是一个安全机制，类似于windows的防火墙，但是这套机制比较复杂，这个目录就是存放selinux相关文件的。
	· /srv: 该目录存放一些服务启动之后需要提取的数据。
	· /sys: 这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个系统文件sysfs。sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。该文件系统是内核设备树的一个直观反映。当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中被创建。
	· /tmp: 存放临时文件
	· /usr: 这是一个非常重要的目录，用户的很多应用程序和文件都存放在这个目录下，类似于windows下的program files目录
	· /usr/bin: 系统用户使用的应用程序
	· /usr/sbin: 超级用户使用的比较高级的管理程序和系统守护程序。
	· /usr/src: 内核源代码的存放目录
	· /var: 这个目录存放着不断扩充着的东西，我们习惯将那些经常被修改的目录存放在这个目录下。包括各种日志文件。
	· /run: 是一个临时文件系统，存储系统启动以来的信息。当系统重启时，这个目录下的文件应该被删掉或清除。如果你的系统上有/var/run目录，应该让他指向run。
	在linux系统中，有几个目录是比较重要的，平时需要注意不要误删除或者随意更改内部文件：
	/etc: 系统中配置文件，如果更改了目录下的某个文件可能会导致系统不能启动。
	/bin,/sbin,/usr/bin,/usr/sbin: 这是系统预设的执行文件存放目录，比如ls就是在/bin/ls目录下的。/bin,/usr/bin是给系统用户使用的指令(除root外的普通用户)，而/sbin,/usr/sbin是给root使用的指令。
	/var: 这是一个非常重要的目录，系统上跑了很多程序，那么每个程序都会有相应的日志产生，而这些日志就记录在这个目录下，具体在/var/log目录下，另外mail的预设也放置在这里。
03. Linux忘记密码解决方法
	01）进入单用户模式，更改root密码即可
		· 重启linux系统
		· 3秒之内要按一下回车
		· 输入e
		· 在第二行最后边输入single，有一个空格。具体方法是按向下箭头移动到第二行，按"e"进入编辑模式
		· 最后按"b"启动，就进入单用户模式了。
		进入单用户模式，就可以更改密码了，命令为passwd。
	02）使用系统安装光盘的救援模式(rescue)
		救援模式即rescue，这个模式主要应用于系统无法进入的情况。如，grub损坏或者一个配置文件修改出错。
		· 光盘启动，按F5进入rescue模式
		· 输入linux rescue回车
		· 选择语言，建议选择英语
		· 选择us键盘
		· 是否启动网络，选no
		· 把系统挂载在/mnt/sysimage中：
			· Continue 就是挂载后继续下一步
			· Read-Only 挂载成只读，这样更安全，有时文件系统损坏时，只读模式会防止文件系统进一步损坏。
			· Skip 就是不挂载，进入一个命令窗口模式。
		· 至此，系统已经挂载到了/mnt/sysimage中，接下来回车，输入chroot /mnt/sysimage 进入管理员环境
		提示：其实也可以到rescue模式下更改root密码的。这个rescue模式和windows PE系统很相近。
04. Linux文件基本属性
	Linux系统是一种典型的多用户系统，不同的用户处于不同的地位，拥有不同的权限。为了保护系统的安全性，Linux系统对不同用户访问同一个文件(包括目录文件)的权限做了不同规定。
	在Linux中我们可以使用ll或者ls -l命令来显示一个文件的属性及文件所属的用户和组，如下实例：
	dr-xr-xr-x  2 root root 4096 Dec 14 2012 bin
	dr-xr-xr-x  4 root root 4096 Apr 19 2019 boot
	在Linux中第一个字符代表这个文件是目录、文件或链接文件等等
	  · [d] 目录
	  · [-] 文件 
	  · [l] 链接文档(link file)
	  · [b] 可供存储的接口设备(可随机存取装置)
	  · [c] 串行口设备(一次性读取装置，键盘、鼠标)
	接下来的字符中，以三个为一组，且均为【rwx】的三个参数的组合。
	其中[r]代表可读(read)、[w]代表可写(write)、[x]代表可执行(execute)。
	这三个权限的位置不会改变，如果没有权限，就用减号[-]。
	每个文件的属性由左边第一部分的10个字符来确定。
	· 第0位，确定文件类型
	· 第1-3位，确定属主(该文件的所有者)拥有该文件的权限
	· 第4-6位，确定属组(所有者同组用户)拥有该文件的权限
	· 第7-9位，确定其他用户拥有该文件的权限
	其中，第1、4、7位表示读权限(r)，第2、5、8位表示写权限(w)，第3、6、9位表示可执行权限(x)
	01）Linux文件属主和属组
		对于文件来说，它都有一个特定的所有者，也就是对该文件具有所有权的用户。
		同时，在Linux系统中，用户是按组分类的，一个用户属于一个或多个组。
		文件所有者以外的用户又可以分为文件所有者的同组用户和其他用户。
		因此，Linux系统按文件所有者、文件所有者同组用户和其他用户来规定了不同文件访问权限。
		对于root用户来说，一般情况下，文件的权限对其不起作用。
	02）更改文件属性
		1、更改文件属组：
		   chgrp [-R] 属组名 文件名 
		2、更改文件属主，也可以同时更改文件属组
		   chown [-R] 属主名 文件名
		   chown [-R] 属主名：属组名 文件名
		3、更改文件9个属性 chmod
		   Linux文件属性有两种设置方法，一种是数字，一种是符合。
		   Linux文件的基本权限就有9个，分别是owner/group/others三种身份各有自己的read/write/execute权限。
		   文件的权限字符为[-rwxrwxrwx],这9个权限是三个一组的，我们可以用数字来代表各个权限：r:4、w:2、x:1
		   每种身份(owner/group/others)各自的三个权限(r/w/x)分数是需要累加的，
		   chmod [-R] xyz[权限累加和(7-0)] 文件或目录
		   例如要将权限变成 -rwxr-xr--，那么权限的累加和为[4+2+1][4+0+1][4+0+0]=754
		   符号法中使用u(user),g(group),o(others)来代表三种身份权限，a则代表all，即全部的身份。读写权限可以写成r,w,x，可以用下表的方式来看
		   chmod	u	+(加入)		r		文件或目录
					g	-(除去)		w
					o	=(设定)		x
					a
			===========================================
			如果我们需要将文件权限设置为-rwxr-xr--,可以使用【chmod u=rwx,g=rx,o=r 文件名】来设定
			而如果要将权限去掉而不改变其他已存在的权限？例如要拿掉全部人的可执行权限，可使用【chmode a-x 文件名】
05. Linux文件与目录管理
	Linux目录结构为树状结构，最顶级的目录为根目录/。
	其他目录通过挂载可以将他们添加到树中，通过解除挂载可以移除它们。
	· 绝对路径：路径的写法由根目录/写起，例如：/usr/share/doc
	· 相对路径：路径的写法不是由根目录写起，例如由/usr/share/doc到/usr/share/man时，可以写成：cd ../man
	01）处理目录常用的命令
		· ls：列出目录
		· cd：切换目录
		· pwd：显示当前目录
		· mkdir：创建一个新目录
		· rmdir：删除一个空目录
		· cp：复制文件或目录
		· rm：移除文件或目录
		· mv：移动文件或目录，或修改文件与目录的名称
	02）ls(列出目录)	选项与参数
		· -a：全部的文件，连同隐藏档(开头为.的文件)一起列出来(常用)
		· -d：仅列出目录，而补列出目录内的文件(常用)
		· -l：长数据串列出，包含文件的属性与权限等数据(常用)
		ls -al ~    #列出家目录下的所有文件(含属性与隐藏文件)
	03）cd(切换目录) [相对路径或绝对路径]
	04）pwd(显示当前目录) [-p]显示出确实路径，而非使用连结(link)路径
	05）Linux文件内容查看
		· cat 由第一行开始显示文件内容
		· tac 从最后一行开始显示文件内容
		· nl 显示时输出行号
		· more 按页显示文件内容
		· less 与more类似，可以向前翻页
		· head 只看头几行
		· tail 只看后几行
06. 用户和用户组管理
	Linux系统使用多用户多任务的分时操作系统，任何一个要使用系统资源的用户，都必须想系统管理员申请一个账号，然后以这个账号的身份进入系统。
	用户的账号一方面可以帮助系统管理员对使用系统的用户进行跟踪，并控制他们对系统资源的访问；另一方面也可以帮助用户组织文件，并未用户提供安全性保护。
	每个用户账号都拥有一个唯一的用户名和各自的口令。
	用户在登录是键入正确的用户名和口令后，就能够进入系统和自己的主目录。
	用户账号的管理有以下几个方面
	· 用户账号的添加、删除与修改
	· 用户口令的管理
	· 用户组的管理
	01）Linux系统用户账号的管理
		1、添加新的用户账号使用useradd命令，语法如下：
			useradd 选项 用户名
			选项：
			· -c comment指定一段注释性描述
			· -d 目录 指定用户主目录，如果此目录不存在，则同时使用-m选项，可以创建主目录。
			· -g 用户组 指定用户所属的用户组
			· -G 用户组 指定用户所属的附加用户组
			· -s Shell文件 指定用户的登录Shell
			· -u 用户号 指定用户的用户号，如果同时有-o选项，则可以重复使用其他用户的标识号
			实例1：useradd -d /home/sam -m sam
			创建用户sam，其中-d和-m选项用来为登录名sam产生一个主目录/home/sam (/home为默认的用户主目录所在的父目录)
			实例2：useradd -s /bin/sh -g group -G adm,root gem
			此命令创建了一个新用户gem，改用户的登录Shell是/bin/sh，他属于group用户组，同时又属于adm和root用户组，其中group用户组是其主组。
			这里可能需要新建组：groupadd group 及 groupadd adm
			增加用户账号就是在/etc/passwd文件中为新用户增加一条记录，同时更新其他系统文件如/etc/shadow, /etc/group等
			Linux提供了集成的系统管理工具userconf，它可以用来对用户账号进行统一管理。
		2、删除账号 userdel 选项 用户名
			删除用户账号就是要将/etc/passwd等系统文件中的用户记录删除，必要时还删除用户的主目录
			常用的选项是-r，作用是同时删除用户的主目录
		3、修改账号 usermod 选项 用户名
			常用的选项包括-c,-d,-m,-g,-G,-s,-u,-o等，这些选项的意义与useradd命令中的选项一样，可以为用户指定行动资源值。
			usermod -s /bin/ksh -d /hom/z -g developer sam
			此命令将用户sam的登录Shell修改为ksh，主目录修改/home/z，用户组改为developer
		4、用户口令管理 passwd 选项 用户名
			选项：
			· -l 锁定口令，即禁用账号。
			· -u 口令解锁
			· -d 使账号无口令
			· -f 强迫用户下次登录时修改口令
			如果默认用户名，则修改当前用户的口令
			普通用户修改自己的口令时，会询问原来的口令，超级用户修改时不需要原来的口令。
			实例1：passwd -d sam  为用户指定空口令
			实例2：passwd -l sam  锁定用户，使其不能登录
	02）Linux系统用户组的管理
		每个用户都有一个用户组，系统可以对一个用户组中的所有用户进行集中管理。不同Linux系统对用户组的规定有所不同，如Linux下的用户属于与它同名的用户组，这个用户组在创建用户时同时创建。
		用户组的管理涉及用户组的添加、删除和修改。组的增加、删除和修改实际上就是对/etc/group文件的更新。
		1、增加用户组 groupadd 选项 用户组名
			选项：
			· -g GID指定新用户组的组标识号(GID)
			· -o 一般与-g选项同时使用，表示新用户组的GID可以与系统已有用户组的GID相同。
			实例1：groupadd group1 向系统中增加新组group1，新组的组标识号是在当前已有的最大组标识号的基础上加1。
			实例2：groupadd -g 101 group2 增加新组group2，同时指定新组的组标识号是101.
		2、删除用户组 groupdel 用户组名
		3、修改用户组 groupmod 选项 用户组名
			选项：
			· -g GID 为用户组指定新的组标识号
			· -o 与-g选项同时使用，用户组的新GID可以与系统已有用户组的GID相同
			· -n新用户组 将用户组的名字改为新名字
			 实例1：groupmod -g 102 -n group3 group2 组group2的标识号改为102，组名改为group3
		4、切换组 newgrp 用户组名
			如果一个用户同时属于多个用户组，那么用户可以在用户组之间切换，以便具有其他用户组的权限
	03）与用户账号有关的系统文件
		完成用户管理的工作有许多种方法，但是每一种方法实际上都是对有关的系统文件进行修改。
		与用户和用户组相关的信息都存放在一些系统文件中，这些文件包括/etc/passwd,/etc/shadow,/etc/group等
		1、/etc/passwd文件是用户管理工作涉及的最重要的一个文件
		   文件中的一行记录对应着一个用户，每行记录又被冒号(:)分隔为7个字段
		   用户名 ：口令 ：用户标识号 ：组标识号 ：注释性描述 ：主目录 ：登录Shell
		2、/etc/shadow中的记录行与/etc/passwd中的一一对应，它有pwconv命令根据/etc/passwd中的数据自动产生
		   它的文件格式与/etc/passwd类似，有若干个字段组成，字段之间用":"隔开。这些字段是：
		   登录名 ：加密口令 ：最后一次修改时间 ：最小时间间隔 ：最大时间间隔 ：警告时间 ：不活动时间 ：失效时间 ：标志
		   1.登录名 与/etc/passwd文件中的登录名一致
		   2.口令 为空则对应用户没有口令
		   3.最后一次修改时间 从某个时刻起，到用户最后一次修改口令时的天数
		   4.最小时间间隔 两次修改口令之间所需的最小天数
		   5.最大时间间隔：口令保持有效的最大天数。
		   6.警告时间 从系统开始警告用户到用户密码正式失效之间的天数
		   7.不活动时间 用户没有登录活动但账号仍能保持有效的最大天数。
		   8.失效时间 是一个绝对天数，如果使用了这个字段，那么就给出相应账号的生存期。期满后，该账号就不再是一个合法的账号，不能登录。
		3、用户组的所有信息都存放在/etc/group文件中
		   将用户分组是Linux系统对用户进行管理及控制访问权限的一种手段。
		   每个用户都属于某个用户组；一个组中可以有多个用户，一个用户也可以属于不同的组。
		   当一个用户同时是多个组的成员是，在/etc/passwd文件中记录的是用户所属的主组，也就是登录是所属的默认组，而其他组称为附加组。
		   用户要访问属于附加组的文件时，必须首先使用newgrp命令使自己成为所要访问的组中的成员。
		   用户组的所有信息都存放在/etc/group文件中，此文件格式也类似于/etc/passwd文件，由冒号(:)隔开若干字段，这些字段有：
		   【组名 ：口令 ：组标识 ：组内用户列表】
		   1. 组名：用户组的名称，由字母数字构成，与/etc/passwd中的登录名一样，组名不应重复。
		   2. 口令：用户组加密后的口令，一般为空或"*"
		   3. 组标识号：与用户标识号类似，也是一个整数，被系统内部用来标识组。
		   4. 组内用户列表：属于这个组的所有用户的列表，不同用户之间用逗号(,)分隔。这个用户组可以是用户主组，也可以是附加组
	04）批量添加用户
		1、先编辑一个用户的文本文件
		   user001::600:100:user:/home/user001:/bin/bash
		   user002::601:100:user:/home/user002:/bin/bash
			……
		   注意用户名、UID、宿主目录都不可以相同，密码栏可以留空
		2、以root身份执行命令/usr/sbin/newusers，从刚创建的用户文件user.txt中导入数据创建用户
		   newusers < user.txt
		   然后执行命令vipw或vi /etc/passwd检查文件中是否已经出现这些用户数据，并且用户的宿主目录是否已经创建。
		3、执行命令/usr/sbin/pwunconv
		   将/etc/shadow产生的shadow密码解码，然后回写到/etc/passwd中，并将/etc/shadow的密码栏删掉。这是为了方便下一步的密码转换工作，即先取消shadow password功能。
		   # pwunconv
		4、编辑每个用户的密码对照文件passwd.txt
			user001:密码
			user002:密码
			……
		5、以root身份执行命令/usr/sbin/chpasswd
		   创建用户密码，chpasswd会将经过/usr/bin/passwd命令编码过的密码写入/etc/passwd的密码栏
		   # chpasswd < passwd.txt
		6、确定密码经编码写入/etc/passwd的密码栏
		   执行命令/usr/sbin/pwconv将密码编码为shadow passwd，并将结果写入/etc/shadow
		   # pwconv
		这样就完成了大量用户的创建了，之后可以到/home下检查这些用户宿主目录的权限设置是否正确，并登陆验证用户密码是否正确。
07. Linux磁盘管理
    磁盘管理好坏直接关系到整个系统的性能问题，磁盘管理常用三个命令为df、du和fdisk
	· df：列出文件系统的整体磁盘使用量
	· du：检查磁盘空间使用量
	· fdisk：用于磁盘分区
	01）df 检查文件系统的磁盘空间占用情况。语法：
		df [ahikHTm] [目录或文件名]
		选项参数：
		· -a：列出所有的文件系统，包括系统特有的/proc等文件系统
		· -k：以KBytes的容量显示各文件系统
		· -m：以MBtytes的容量显示各文件系统
		· —h：以人们较易阅读的GBytes，MBytes，KBytes等格式自行显示
		· —H：以M=1000K取代M=1024K的进位方式
		· -T：显示文件系统类型，连同partition的filesystem名称(例如ext3)也列出
		· -i：不用硬盘容量，而以inode的数量来显示
	02）du 查看文件和目录使用的磁盘空间
		du [-ahskm] 文件或目录名称
		选项参数：
		· -a：列出所有文件与目录容量，因为默认仅统计目录底下的文件
		· -h：以人们较易阅读的容量格式(G/M)显示
		· -s：列出总量而已，不列出每个个别的目录占用容量
		· -S：不包括子目录下的总计，与-s有差别
		· -k：以KBytes列出容量显示
		· -M：以MBytes列出容量显示
	03）fdisk 磁盘分区
		fdisk [-l] 设备名称
		选项参数：
		· -l：输出后面接的设备所有的分区内容。若仅有fdisk -l 时，则系统将会把整个系统内能够搜寻到的装置的分区列出来。
		fdisk /dev/hdc 回车后出现命令提示符
		Command（m for help）：等待输入
		命令介绍：
		a	toggle a bootable flag
		b	edit bsd disklabel
		c	toggle the dos compatibility flag
		d	delete a partition
		l	list knowpartition types
		m	print this menu
		n	add a new partition
		o	create a new empty DOS partition table
		p	print the partition table
		q	quit without saving changes
		s	create a new empty Sun disklabel
		t	change a partition's system id
		u	change display/entry units
		v	verify the partition table
		w	write table to disk and exit   <==将刚刚的动作写入分区表
		x	extra functionality(expert only)
	04）mkfs 磁盘格式化
		磁盘分区完毕后进行文件系统格式化（make filesystem）
		mkfs [-t 文件系统格式] 设备名
		选项参数：
		· -t：可以接文件系统格式，例如ext3，ext2，vfat等
	05）fsck 磁盘检验
		(file system check)检查和维护不一致的文件系统，若系统掉电或磁盘发生问题
		fsck [-t 文件系统] [ACay] 设备名称
		选项参数：
		· -t：给定文件系统的类型，若在/etc/fstab中已有定义或kernel本身已支持的，则不需要加上此参数
		· -s：依序执行fsck的指令来检查
		· -A：对/etc/fstab中所有列出来的分区(partition)做检查
		· -C：显示完整的检查进度
		· -d：打印出e2fsck的debug结果
		· -p：同时有-A条件时，同时有多个fsck的检查一起执行
		· -R：同时有-A条件时，省略/不检查
		· -V：详细显示模式
		· -a：如果检查有错则自动修复
		· -r：如果检查有错则由使用者回答是否修复
		· -y：指定检测每个文件是自动输入yes，在确定哪些是不正常的时候，可以执行#fsck -y 全部检查修复。
		实例1：fsck [tab][tab] 查看系统有多少文件系统支持fsck命令
		实例2：fsck -C -f -t ext3 /dev/hdc6 强制检测/dev/hdc6分区
	06）磁盘挂载与卸载
		Linux的磁盘挂载使用mount命令，卸载使用umount命令
		磁盘挂载的语法：
		mount [-t 文件系统] [-L Label名] [-o 额外选项] [-n] 设备文件名 挂载点
		实例1：用默认方式，将刚刚创建的/dev/hdc6挂载到/mnt/hdc6上面
		mkdir /mnt/hdc6
		mount /dev/hdc6 /mnt/hdc6
		df
		磁盘卸载的语法：
		umount [-fn] 设备名或挂载点
		选项参数：
		· -f：强制卸载，可用在类似网络文件系统(NFS)无法读取到的情况
		· -n：不升级/etc/mtab情况下卸载
		实例1：卸载/dev/hdc6
		umount /dev/hdc6
08. Linux vi/vim
	vim具有程序编辑的能力，可以主动的以字体颜色辨别语法的正确性，方便程序设计。
	01）vim的使用
		基本上vim分为三种模式，分别是命令模式(Command mode)，输入模式(Insert mode)和底线命令模式(Last line mode)。
	02）命令模式
		用户刚刚启动vim，便进入了命令模式
		此状态下敲击键盘动作会被vim识别为命令，而非输入字符。常用命令如下：
		· i 切换到输入模式，以输入字符。
		· x 删除当前光标所在处的字符。
		· : 切换到底线命令模式，以在最底一行输入命令。
		若想要编辑文本：启动vim，进入命令模式，按下i，切换到输入模式。
		命令模式只有一些最基本的命令，因此仍要依靠底线命令模式输入更多命令
	02）输入模式
		在命令模式下按i就进入了输入模式
		在输入模式中可以使用以下按键：
		· 字符按键以及Shift组合，输入字符
		· ENTER，回车键，换行
		· BACKSPACE，退格键，删除光标前一个字符
		· DEL，删除键，删除光标后一个字符
		· 方向键，在文本中移动光标
		· HOME/END，移动光标到首行/尾行
		· PageUp/PageDown，上/下翻页
		· Insert，切换光标为输入/替换模式，光标将变成竖线/下划线
		· ESC，退出输入模式，切换到命令模式
	03）底线模式
		在命令模式下按下:(英文冒号)就进入了底线命令模式。
		底线命令模式可以输入单个或多个字符的命令，可用的命令非常多。
		在底线命令模式中，基本的命令有(已经省略了冒号)：
		· q 退出程序
		· w 保存文件
		按ESC键可以随时退出底线命令模式
		命令模式(输入iao) --→ 输入模式(输入ESC键) --→ 命令模式
		命令模式(输入:) --→ 底线命令模式(回车) --→ 命令模式
	04）vim使用实例
		1、使用vim进入一般模式
		   直接输入【vim 文件名】就进入了vim的一般模式。一定要加文件名，不管该文件是否存在！
		2、按下i进入输入模式(也称为编辑模式)，开始编辑文字
		   在一般模式之中，只要按下i，o，a等字符就可以进入输入模式了！
		   在编辑模式当中，你可以发现在左下角状态栏中会出现 --INSERT-- 的字样，那就是可以输入任意字符的提示。
		   在这个时候，键盘上除了ESC这个按键之外，其他的按键都可以视作一般的输入按钮了，所以，你可以进行任何的编辑。
		3、按下ESC键回到一般模式
		   按下ESC键以后，左下角的 --INSERT-- 不见了！
		4、在一般模式中按下 :wq 存储后离开vim
	05）vim按键说明
		第一部分：一般模式可用的光标移动、复制粘贴、搜索替换等
		1、移动光标的方法：
		   h|←   光标向左移动一个字符
		   j|↓   光标向下移动一个字符
		   k|↑   光标向上移动一个字符
		   l|→   光标向右移动一个字符
		   【如果要进行多次移动的话，加上想要进行的次数(数字)后，按下动作即可！[30j]
		   [Ctrl]+[f]	屏幕向下移动一页，相当于[Page Down]按键(常用)
		   [Ctrl]+[b]	屏幕向上移动一页，相当于[Page Up]按键(常用)
		   [Ctrl]+[d]	屏幕向下移动半页
		   [Ctrl]+[u]	屏幕向上移动半页
		   +			光标移动到非空格符的下一行
		   -			光标移动到非空格符的上一行
		   n<space>		按下数字再按空格键，光标会向右移动这一行的n个字符
		   0|Home		移动到这一行的最前面字符处(常用)
		   $|End		移动到这一行的最后面字符处(常用)
		   H			光标移动到这个屏幕的最上方那一行的第一个字符
		   M			光标移动到这个屏幕的中央那一行的第一个字符
		   L			光标移动到这个屏幕的最下方那一行的第一个字符
		   G			光标移动到这个文档的最后一行(常用)
		   nG			n为数字，移动到这个文档的第n行
		   gg			移动到文档的第一行，相当于1G(常用)
		   n<Enter>		光标向下移动n行(常用)
		2、搜索替换
		   /word		向光标之下寻找一个名称为word的字符串
		   ?word		向光标之上寻找一个名称为word的字符串
		   n(next)		代表重复前一个搜寻动作	
		   N			反向进行前一个搜寻动作
		   :n1,n2s/word1/word2/g	n1与n2为数字。在第n1与n2行之间寻找word1这个字符串，并将该字符串用word2取代
		   :1,$s/word1/word2/g或	从第一行到最后一行寻找word1字符串，并用word2取代
		   :%s/word1/word2/g
		   :1,$s/word1/word2/gc或	从第一行到最后一行寻找word1字符串，并用word2取代,且在取代前显示提示信息
		   :%s/word1/word2/gc
		3、删除、复制和粘贴
		   x,X		在一行字当中，x为向后删除一个字符(相当于[del]按键)，X为向前删除已字符(相当于[backspace])(常用)
		   nx		n为数字，连续向后删除n个字符。
		   dd		删除光标所在的那一整行(常用)
		   ndd		删除光标所在的向下n行
		   d1G		删除光标所在到第一行的所有数据
		   dG		删除光标所在到最后一行的所有数据
		   d$		删除关标所在到该行的最后一个字符
		   d0		删除光标所在到该行的最前面的一个字符
		   yy		复制光标所在的一行
		   nyy		复制光标所在向下n行
		   y1G		复制光标所在行到第一行的所有数据
		   yG		复制光标所在到最后一行的所有数据
		   y0		复制光标所在的那个字符到该行首行的所有数据
		   y$		复制光标所在的那个字符到该行行尾的所有数据
		   p,P		p将已复制的数据贴在光标的下一行，P贴在上一行
		   J		将光标所在行与下一行的数据合成同一行
		   c		重复删除多个数据，例如向下删除10行，[10cj]
		   u		重复前一个动作
		   [Ctrl]+r	重做上一个动作
		   .		重复前一个动作
		第二部分：一般模式切换到编辑模式的可用按钮说明
		1、进入输入或替换编辑模式
		   i,I		进入输入模式(Insert mode)：
					i为[从目前光标所在处输入]，I为[在目前所在行的第一个非空格符处开始输入]
		   a,A		进入输入模式(Insert mode):
					a为[从目前光标所在的下一个字符处开始输入]，A为[从光标所在行的最后一个字符开始输入]
		   o,O		进入输入模式：
					o在当前光标所在的下一行处输入新的一行，O为在当前光标所在处的上一行输入新的一行
		   r,R		进入替换模式(Replace mode):
					r只会替换光标所在的那一个字符一次，R一直替换光标所在的文字，直到按下ESC为止(常用)
		   上面这些按键中，在vim画面的左下角处会出现【--INSERT--】或【--REPLACE--】的字样。由名称可以知道动作！！
		   在文档中输入字符时，一定要在左下角看到INSERT或REPLACE才能输入。
		第三部分：一般模式切换到指令行模式可用按钮说明
		01、指令行的储存、退出等指令
			:w			将编辑的数据写入磁盘文件中(常用)
			:w!			若文件属性为只读是，强制写入该文件
			:q			退出vim(常用)
			:q!			强制退出(不保存)
			:wq			保存后退出
			ZZ			若文档没有改动，则不保存退出，若文档已经被修改过，则保存后退出
			:w[fn]		将编辑的数据保存为另一个文件(另存为)
			:r[fn]		在编辑的数据中，读入另一个文档的数据，就是将fn这个文档的内容加到光标所在行的后面
			:ni,n2 w fn 将n1到n2的内容保存成fn这个文件
			:!command	暂时离开vi到指令行模式下执行command的显示结果 [:! ls]在vim中查看当前目录下的文件
		02、vim环境变更
			:set nu		显示行号，设定之后，会在每一行的前缀显示该行的行号
			:set nonu	与set nu相反，取消显示行号
	特别注意：在vim中，数字通常代表重复做几次的意思！也可能是代表去到第几个什么什么的意思。
08. Linux yum命令
	yum(Yellow dog Updater, Modified)是一个在Fedora和RedHat以及SuSE中的Shell前段软件包管理器
	基于RPM包管理，能够从指定的服务器自动下载RPM包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软件包，无须频繁的一次次下载、安装。
	yum提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令简洁好记。
	01）yum语法
		yum [options] [command] [package ……]
		· options：可选，选项包括-h(帮助)，-y(安装过程提示全部选"yes")，-q(不显示安装过程)等等。
		· command：要进行的操作
		· package：操作的对象
	02）yum常用名
		· 1.列出所有可更新的软件清单：yum check-update
		· 2.更新所有软件命令：yum update
		· 3.仅安装指定的软件命令：yum install <package_name>
		· 4.仅更新指定的软件命令：yum update <package_name>
		· 5.列出所有可安装软件清单命令：yum list
		· 6.删除软件包命令：yum remove <package_name>
		· 7.查找软件包命令：yum search <keyword>
		· 8.清除缓存命令：
			· yum clean packages: 清除缓存目录下的软件包
			· yum clean headers: 清除缓存目录下的headers
			· yum claean oldheaders: 清除缓存目录下旧headers
			· yum clean,yum clean all(=yum clean packages;yum clean oldheaders):清除缓存目录下的软件包及旧的headers
	03）国内yum源
		网易(163)yum源是国内最好的yum源之一，无论速度还是软件版本，都非常的不错。
		安装步骤
		首先备份/etc/yum.repos.d/CentOS-Base.repo
			mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
		下载对应版本repo文件，放入/etc/yum.repos.d/(操作前请做好相应备份)
			wget http://mirrors.163.com/.help/CentOS6-Base-163.repo
			mv CentOS6-Base.repo CentOS-base.repo
		运行以下命令生成缓存
			yum clean all
			yum makecache
			
#########################################
## 标题：Shell 教程                     #
## 时间：2019/10/17 9:50                #
#########################################
01. Shell教程
	Shell是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务
	01）Shell脚本
	02）Shell环境(bash)
	03）第一个Shell脚本
	04）运行Shell脚本的两种方法
		1、作为可执行程序   ./test.sh
		2、作为解释器参数   sh test.sh
02. Shell变量
	01）变量命名规范同其他编程语言
		1.只能是字母、数字或下划线，不能包含其他特殊字符
		2.以字母下划线开台
		3.不能包含关键字
	02）除了显示赋值以外，还可以用语句为变量赋值 for file in `ls /etc`   for file in $(ls /etc)
	04）使用变量
		使用一个定义过的变量，只要在变量名前加美元符号即可，赋值的时候不能用美元符号。
		your_name='qinjx'
		echo $your_name
		echo ${your_name} 用于字符串拼接的场合，解释器理解变量的边界
	05）只读变量
		使用readonly命令可以将变量定义为只读变量，只读变量的值不能被改变。
		修改只读变量会提示【变量名: readonly variable】
	06）删除变量
		使用unset命令可以删除变量 unset varable_name
		变量被删除后不能再次使用，使用时无错误提示无输出内容
	07）变量类型
		01、局部变量
			在脚本或命令中定义，仅在当前Shell实例中有效，其他Shell启动的程序不能访问局部变量。
		02、环境变量
			所有程序，包括Shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候Shell脚本也可以定义环境变量。
		03、Shell变量
			Shell变量使用Shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了Shell的正常运行
	08）Shell字符串
		字符串是Shell编程中最常用最有用的数据类型(除了数字和字符串，也没啥其他类型好用了)，字符串可以用单引号，也可以用双引号，也可以不用引号
		01、单引号
			· 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
			· 单引号字符串中不能出现单独一个单引号(对单引号使用转义符后也不行)，但可成对出现，作为字符串拼接使用。
		02、双引号
			· 双引号里可以有变量
			· 双引号里可以出现转义符
		03、拼接字符串
			拼接时不需要连接符
		04、获取字符串长度
			字符串变量前加"#"号可以输出字符串长度
		05、提取子字符串
			类似于切片法
	09）Shell数组
		bash只支持一维数组，并且没有限制数组的大小
		数组元素的下标由0开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，表达式值应大于或等于0.
		01、定义数组
			在Shell中用括号来表示数组，类似于Python的元组，数组元素用空格分隔开。
			数组名=(值1 值2 ... 值n)
			可以单独定义数组的各个分量，可以不使用连续的下标，而且下标的范围没有限制。
		02、读取数组
			读取数组的一般格式：${数组名[下标]}
			使用@符号可以获取数组中的所有元素：echo ${array_name[@]}
		03、获取数组的长度
			length=${#array_name[@]}  #取得数组元素的个数
			length=${#array_name[*]}  #同上
			lengthn=${#array_name[n]} #取得数组单个元素的长度
	10）Shell注释
		单行注释 #
		多行注释 :<<EOF …… EOF
		EOF可以用其他符号：<<' …… '   <<! …… !
03. Shell传递参数
	在执行Shell脚本时可以向脚本传递参数，脚本内获取参数的格式为：$n。n代表一个数字，1为执行脚本的第一个参数……
	处理参数的特殊字符
		参数处理	说明
		$#		传递到脚本的参数个数
		$*		以一个单字符串显示所有向脚本传递的参数。(所有参数是一个字符串)
		$$		脚本运行的当前进程ID号
		$!		后台运行的最后一个进程的ID号
		$@		与$*相同，但是使用时加引号，并在引号中返回每个参数。(所有参数每个都是一个字符串)
		$-		显示Shell使用的当前选项，与set命令功能相同
		$?		显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误
04. Shell数组
05. Shell基本运算符
	Shell和其他编程语言一样，支持多种运算符，包括：
	· 算术运算符
	· 关系运算符
	· 布尔运算符
	· 字符串运算符
	· 文件测试运算符
	原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如awk和expr，expr最常用。
	expr是一款表达式计算工具，使用它能完成表达式的求值操作。
	两点注意：
	· 表达式和运算符之间要有空格，例如 2+2不对，必须写成2 + 2
	· 完整的表达式要被``(反引号)包含。
	01）算术运算符
		下表列出二楼常用的算术运算符，假定变量a为10，变量b为20：
		运算符	说明			举例
		+		加法			`expr $a + $b` 结果为30
		-		减法			`expr $a - $b` 结果为-10
		*       乘法			`expr $a * $b` 结果为200
		/       除法			`expr $a / $b` 结果为2
		%       取余			`expr $b % $a` 结果为0
		=		赋值			a=$b
		==		相等			[$a == $b] 返回false
		!=		不相等		[$a != $b] 返回true
		注意：条件表达式要放在方括号之间，并且要有空格
		     表达式中乘号的前面必须加反斜杠进行转义
	02、关系运算符
		关系运算符值支持数字，不支持字符串，除非字符串的值是数字
		下表列出了常用的关系运算符，假定变量a为10，变量b为20：
		运算符	说明						举例
		-eq		检测两个数是否相等		[ $a -eq $b ] 返回false
		-ne		检测两个数是否不相等		[ $a -ne $b ] true
		-gt		检测左边的数是否大于右边的	[ $a -gt $b ] false
		-lt		检测左边的数是否小于右边的 [ $a -lt $b ] true
		-ge		左边的数是否大于等于右边的 [ $a -ge $b ] false
		-le		左边的数是否小于等于右边的 [ $a -le $b ] true
	03、布尔运算符
		运算符	说明									举例
		！		非运算，表达式为true则返回false		[ !false ]	true
		-o		或运算，有一个表达式为true则返回true	[ $a -lt 20 -o $b -gt 100] true
		-a 		与运算，两个标表达式都为true返回true	[ $a -lt 20 -a $b -gt 100] false
	04、逻辑运算符
		运算符	说明		举例
		&&		逻辑与	[[ $a -lt 100 && $b -gt 100]] false
		||		逻辑或	[[ $a-lt 100 || $b -gt 100 ]] true
	05、字符串运算符
		运算符	说明					举例
		=		字符串相等返回true	[ $a = $b ] 返回false
		!=		字符串不相等返回true	[ $a != $b ] true
		-z		字符串长度为0返回true	[ -z $a ] false
		-n		字符串长度不为0返回true[ -n "$a" ] true
		$		字符串不为空返回true	[ $a ] true
	06）文件测试运算符
		文件测试运算符用于检测Unix文件的各种属性
		操作符	说明					举例
		-b file	块设备返回true		[ -b $file ] false
		-c file	字符设备返回true		[ -c $file ] false
		-d file	目录返回true			[ -d $file ] false
		-f file 普通文件返回true		[ -f $file ] true
		-g file	设置了SGID位返回true	[ -g $file ] false
		-k file 设置了黏着位返回true	[ -k $file ] false
		-p file	有管道返回true		[ -p $file ] false
		-u file 设置二楼SUID返回true	[ -u $file ] false
		-r file 文件可读返回true		[ -r $file ] true
		-w file	文件可写返回true		[ -w $file ] true
		-x file 文件可执行返回true	[ -x $file ] true
		-s file 文件不为空返回true	[ -s $file ] true
		-e file 文件目录存在返回true	[ -e $file ] true
		-S file 文件是socket返回true	[ -S $file ] false
		-L file 文件是符号链接返true	[ -L $file ] false
06. Shell echo命令
	Shell的echo命令用于字符串输出
	01）显示普通字符串，引号可以省略
	02）显示转义字符 "\"
	03）显示变量
		read命令从标准输入中读取一行，并把输入行的每个字段的值指定Shell变量
		read name
		echo "$name It is a test"
	04）显示换行 "\n"
		需要开启转义 echo -e "it is test\nok"
	05）显示不换行 "\c" (也需要开启转义 -e)
		前后两行连续输出
	06）显示结果定向至文件
		echo "It is a test" > myfile
	07）原样输出字符串，不进行转义或取变量(用单引号)
	08）显示命令执行结果(用反引号"`")
07. Shell printf命令
	printf由POSIX标准所定义，因此使用printf的脚本比使用echo可移植性好
	printf使用引用文本或空格分隔的参数，外面可以在printf中使用格式化字符串，还可以制定字符串宽度、左右对齐方式等。默认printf不会像echo自动添加换行符，可以手动添加\n
	printf语法：printf format-string [arguments……]
		参数说明：
				formate-string：格式控制字符串
				arguments：参数列表
	%s %c %d %f都是格式替代负
	%-10s 指一个宽度为10个字符(-表示左对齐，没有则表示右对齐)，任何字符都会被显示在10个字符宽度的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。
	%-4.2f 指格式化为小数，其中.2指保留2位小数。
	01）printf的转义序列
		序列	说明
		\a 	警告字符，通常为ASCII的BEL字符
		\b 	后退
		\c 	抑制(不显示)输出结果中任何结尾的换行字符(只在%b格式指示符控制下的参数字符串中有效)，而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略
		\f 	换页(formfeed)
		\n  换行
		\r  回车
		\t  水平制表符
		\v	垂直制表符
		\\  一个字面上的反斜杠
		\ddd表示1到3位数八进制值的字符，仅在格式字符串中有效
		\0ddd表示1到3位的八进制值字符
09. Shell test命令
	相当于[ 条件表达式]
10. Shell流程控制
	sh的流程控制不可为空，例如，else不做任何事情的话，就不要写这个else
	01）if else (写成一行时需要在条件的后面加一个分号";")
		if condition1
		then
			command1
			……
		elif condition2; then
			command10
		else
			command11
			……
		fi
11. 循环语句
	01）for循环	
		for var in item1 item2 ... itemN
		do
			command1
			command2
			……
			commandN
		done
		for var in item1 item2 ...itemN; do command1;command2... done;
		当变量值在列表里，for循环即执行一次所有命令，使用变量名获取变量列表中的当前取值。命令可以为任何有效的shell命令和语句。in列表可以包含替换、字符串和文件名。
		in列表是可选的，如果不用它，for循环使用命令行的位置参数
	02）while循环
		while循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。其格式为：
		while condition
		do
			command
		done
		
		let 命令是 BASH 中用于计算的工具，用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量。如果表达式中包含了空格或其他特殊字符，则必须引起来。
		while循环可用于读取键盘信息，an<Ctrl+D>结束循环.
	03）无限循环
		while :
		do
			command
		done
		
		while true
		do
			command
		done
		
		for (( ; ; ))
	04）until循环
		until循环执行一系列命令直至条件为true时停止。
		until循环与while循环在处理方式上刚好相反。
		一般while循环优于until循环，但在某些时候也只是极少数情况下，until循环更加有用。
		until语法格式：
		until condition
		do
			command
		done
	05）case语句
		多选择语句，可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令，格式如下：
		case 值 in
		模式1）
			command1
			……
			;;
		模式2）
			command2
			……
			;;
		esac
	06）跳出循环
		1、break命令允许跳出所有循环(终止执行后面的所有循环)
		2、continue跳出当前循环(不是跳出所有循环，后面的还要执行)
	07）esac
		case的结束标记，每个case分支用右圆括号，用两个分号表示break。
12. Shell函数
	linux shell用户可以定义函数，然后在shell脚本中可以随便调用。格式如下：
	[ function ] funcname [()]
	
	{
		action;
		[return int;]
	}
	
	说明：
	· 1、可以带function fun()定义，也可以直接fun()定义，不带任何参数。
	· 2、参数返回，可以显示加return返回，如果不加，将以最后一条命令运行结果作为返回值。return后跟数值n(0-255)
	· 3、函数返回值在调用该函数后通过$?来获得。
	注意：所有函数在使用前必须定义。这意味着必须将函数放在脚本开始部分，直至Shell解释器首次发现它时，才可以使用。调用函数仅使用函数名即可。
	01）函数参数
		在Shell中，调用函数是可以向其传递参数。在函数体内部，通过$n的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数。
		注意：$10不能获取 第10个参数，获取第10个参数要${10}。当n>=10时，需要用${n}来获取参数。
		另外，还有几个特殊字符用来处理参数：
		参数	说明
		$#	传递到脚本的参数个数
		$*	以一个单字符显示所有向脚本传递的参数
		$$	脚本运行的当前进程ID号
		$!	后台运行的最后一个进程的ID号
		$@	与$*相同，但是使用时加引号，并在引号中返回每个参数
		$-	显示Shell使用的当前选项，与set命令功能相同
		$?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。
13. Shell输入输出重定向
	大多数UNIX系统命令从你的终端接受输入并将所产生的输出发送回到你的终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。
	01）重定向命令列表如下：
		命令				说明
		command > file	将输出重定向到file
		command < file	将输入重定向到file
		command >> file	将输出以追加方式重定向到file
		n > file		将文件描述符为n的文件重定向到file
		n >> file		将文件描述符为n的文件以追加的方式重定向到file
		n >& m			将输出文件m和n合并。
		n <& m			将输入文件m和n合并
		<< tag			将开始标记tag和结束标记tag之间的内容作为输入
		需要注意：文件描述符0通常是标准输入(STDIN),1是标准输出(STDOUT)，2是标准错误输出(STDERR)。
		重定向深入讲解：
		一般情况下，每个Unix/Linux命令运行时会打开三个文件：
		· 标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据
		· 标准输出文件(stdout)：stdout的文件描述符为1，Unix程序默认向stdout输出数据。
		· 标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。
	02）默认情况下，command > file 将stdout重定向到file，command < file 将stdin重定向到file。
	03）Here Document
		Here Document是Shell中的一种特殊的重定向方式，用来将输入重定向到一个交互式Shell脚本程序。
	04）/dev/null文件
		如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到/dev/null
		/dev/null是一个特殊文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是/dev/null文件非常有用，将命令的输出重定向到它，会起到禁止输出的效果。
		如果希望屏蔽stdout和stderr，可以这样写：
		$ command > /dev/null 2>&1
14. Shell 文件包含
	Shell也可以包含外部脚本。这样可以很方便的封装一些共用的代码作为一个独立的文件。语法格式如下：
	【. filename】或【source filename】

#########################################
## 标题：pandas教程                     #
## 时间：2019/10/21 9:50                #
#########################################
00. pandas处理Excel数据的应用
	01）安装环境
		1、pip install xlrd
		2、pip install pandas
		3、安装pandas模块还要有编码环境，确保电脑上有Net.4、VC-Compliler以及winsdk_web。
		   实际安装时并未特意安装这三个模块，可能系统上已经存在了。
	02）pandas操作Excel表单
		1、读取工作表
		   df=pd.read_excel(bookname,sheet_name='sheetname')
		   data=df.head([rownum]) #默认读取前5行的数据
		   data=df.values #读取所有数据，是一个列表data[0]表示第一行数据。
	03）pandas操作Excel的行列
		1、读取指定的单行，数据保存在列表里面
		   df=pd.read_excel('lemon.xlsx') #默认读取工作薄的第一个工作表
		   data=df.ix[0].values #0表示第一行，values读取数据不包含表头
		   print("读取指定行的数据：\n{0}".format(data))
		   