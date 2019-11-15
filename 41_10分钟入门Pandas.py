import numpy as np
import pandas as pd

print("***** 数据结构简介******")
print("基本原则：数据正确对齐是必须的!")
print("")

print("一、Series")
print("    Series是一维标记的数组，能够保存任何数据类型(整数、字符串、浮点数、Python对象等")
print("    轴标签统称索引。创建Series的基本方法：")
print("    s=pd.Series(data,index=index)")
print("    传递的索引是轴标签列表。因此根据数据的不同可分为几种情况：")
print("1.来自ndarray")
print("  如果data是ndarray，则索引的长度必须与数据的长度相同。如果没有传递索引，将创建一个具有值的索引")
print("  s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])")
s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
print(s)
print("")
      
print("2.从字典")
print("  Series可以从dicts实例化")
print("  d={'b':1,'a':0,'c':2}")
print("  pd.Series(d)")
d={'b':1,'a':0,'c':2}
s1=pd.Series(d)    
print(s1)
print("")

print("  如果传递索引，则将列出与索引中的标签对应的数据中的值。")
print("  pd.Series(d,index=['b','c','d','a'])")
s2=pd.Series(d,index=['b','c','d','a'])
print(s2)
print("注意：NaN（不是数字）是pandas中使用的标准缺失数据标记。")
print("")

print("3.从标量值")
print("  如果data是标量值，则必须提供索引。将重复该值以匹配索引的长度")
print("  s=pd.Series(5.,index=['a','b','c','d','e']")
s3=pd.Series(5.,index=['a','b','c','d','e'])
print(s3)
print("")

print("4.Series是类似ndarray的数据类型")
print("  Series的行为和ndaary非常相似，并且是大多数NumPy函数的有效参数。但是，切片等操作也会对索引进行切片.")
print("  s[0]的结果是：")
print(s[0])
print("")

print("  s[:3]的结果是：")
print(s[:3])
print("")

print("  s[s > s.median()]的结果是：")
print(s[s > s.median()])
print("")

print("  s[[4,3,1]]的结果是：")
print(s[[4,3,1]])
print("")

print("  np.exp(s)的结果是：")
print(np.exp(s))
print("")

print("  s.array的结果是：")
print("  在没有索引的情况下执行某些操作时(例如，禁用自动对齐)，访问该数组非常有用。")
print(s.array)
print("")

print("5.Series是类似dict(字典)的数据类型")
print("s的内容如下:")
print(s)
print("")
print("s['a']=",s['a'])
print("s['e']=",s['e'])
print("  如果未包含标签，则会引发异常")
print("  使用get方法，缺少的标签将返回None或指定的默认值")
print("s.get('f')=",s.get('f'))
print("s['f']=")
print("  执行该语句会返回一大堆错误")
print("")

print("6.矢量化操作和标签对齐Series")
print("s的内容如下:")
print(s)
print("")
print("s + s 的结果如下：")
print(s+s)
print("s * 2 的结果如下：")
print(s * 2)
print("np.exp(s)")
print(np.exp(s))
print("")

print("二、数据帧")
print("DataFrame是一个二维标记数据结构，具有可能不同类型的列。")
print("您可以将其视为电子表格或SQL表，或Series对象的字典。它通常")
print("是最常用的0andas对象。与Series一样，DataFrame接受许多")
print("不同类型的输入：")
print("·1D ndarray，list, dicts或Series的Dict")
print("·二维numpy.ndarray")



      



      



      
      
