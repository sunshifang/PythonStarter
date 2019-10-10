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
	  
	  