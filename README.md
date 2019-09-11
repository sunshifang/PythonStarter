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
   
   
	
	
   
   

  


