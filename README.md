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
   

  


