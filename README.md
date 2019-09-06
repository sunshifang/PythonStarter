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
   



   

  


