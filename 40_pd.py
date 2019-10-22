import numpy as np
import pandas as pd

print("************************************************")
print("                pandas用法总结")
print("************************************************")

print("一、生成数据表")
print("1.首先导入pandas库，一般都会用到Numpy库，导入备用")
print("  import numpy as np")
print("  import pandas as pd")
print("")

print("2.导入csv或者xlsx文件")
print("  df1=pd.DataFrame(pd.read_csv('bill.csv',header=1))")
print("  其中，header指定行作为数据表的标题")
print("  df2=pd.DataFrame(pd.read_excel('bill.xlsx'))")
df1=pd.DataFrame(pd.read_csv('bill.csv',header=0))
df2=pd.DataFrame(pd.read_excel('bill.xlsx'))
print(df1)
print(df2)
print("")

print("3.用pandas创建数据表")
df=pd.DataFrame({'id':[1001,1002,1003,1004,1005,1006],
                 'date':pd.date_range('20191021',periods=6),
                 'city':['北京','上海','广州',' 深圳 ','上海','ChongQing'],
                 'age':[23,44,54,32,32,60],
                 'cagegory':['100-A','100-B','110-B','110-C','210-A','130-F'],
                 'price':[1200,np.nan,2133,5433,np.nan,4432]},
                columns=['id','date','city','category','age','price'])
'''
print("  手动创建的数据表df.values[默认显示全部数据，无标题]为：\n{0}".format(df.values))
print("")
print("  手动创建的数据表df.head(6)[默认显示5行，有标题]为：\n{0}".format(df.head(6)))
print("")
print("  手动创建的数据表df.sample(6)[默认显示5行，有标题]为：\n{0}".format(df.sample(6)))    
print("")

print("二、数据表信息查看")
print("1.维度查看")
print("  df.shape={0}".format(df.shape))
print("")

print("2.数据表基本信息(维度、列名称、数据格式、所占空间等)")
print("  df.info()显示如下数据(函数的返回值为None):")
print(df.info())
print("")

print("3.每一列数据的格式")
print("  df.dtypes显示内容如下：")
print(df.dtypes)
print("")

print("4.某一列格式：")
print("  df['B'].dtype显示内容是：{0}".format(df['city'].dtype))
print("")

print("5.空值")
print("  df.isnull()显示的内容是: \n{0}".format(df.isnull()))
print("")

print("6.查看某一列空值")
print("  df['B'].isnull()")
print(df['city'].isnull())
print("")

print("7.查看某一列的唯一值")
print("  df['B'].unique()【重复的上海只显示一次】")
print(df['city'].unique())
print("")

print("8.查看数据表的值")
print("  df.values 显示结果如下：")
print(df.values)
print("")

print("9.查看列名称")
print("  df.columns 显示结果如下：")
print(df.columns)
print("")

print("10.查看前5行数据、后5行数据")
print("   df.head() 默认显示前5行数据")
print("   df.tail() 默认显示后5行数据")
print(df.head())
print(df.tail())
print("")

print("三、数据表清洗")
print("1.用指定的数字或字符填充空值")
print("  df.fillna(value=0)【value可以自定义】的处理结果如下：")
print(df.fillna(value=0))
print("")

print("2.使用列的平均值对NA进行填充")
print("  df['price'].fillna(df['price'].mean())的操作结果如下：")
print(df['price'].fillna(df['price'].mean()))
print("")

print("3.清除指定字段的字符空格")
print("  df['city']=df['city'].map(str.strip)的操作结果如下：")
df['city']=df['city'].map(str.strip)
print(df.values)
print("")

print("4.大小写转换")
print("  df['city']=df['city'].str.lower()的操作结果如下：")
df['city']=df['city'].str.lower()
print(df.values)
print("")

print("5.更改数据格式")
print("  df['price'].astype('int')的操作结果如下：")
df['price']=df['price'].fillna(value=0)
df['price']=df['price'].astype('int')
print(df.values)
print("")

print("6.更改列名称")
print("  df.rename(columns={'category':'category-size'})操作结果如下：")
df=df.rename(columns={'category':'category-size'})
print(df.head())
print("")

print("7.删除后出现的重复值")
print("  df['city'].drop_duplicates()操作后的结果如下：")
df['city']=df['city'].drop_duplicates()
print(df.head(6))
print("")

print("8.删除先出现的重复值")
print("  df['city'].drop_duplicates(keep='last')操作后的结果如下：")
df['city']=df['city'].drop_duplicates(keep='last')
print(df.head(6))
print("")

print("9.数据替换")
print("  df['city'].replace('chongqing','cq')")
df['city']=df['city'].replace('chongqing','cq')
print(df.head(6))
print("")
'''
print("四、数据预处理")
df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008],
                  "gender":['male','female','male','female','male','female','male','female'],
                  "pay":['Y','N','Y','Y','N','Y','N','Y'],
                  "m-point":[10,12,20,40,40,40,30,20]})
print(df1.head(8))
print("")
'''
print("1.数据表合并")
print("1.1 merge")
print("    df_inner=pd.merge(df,df1,how='inner') #匹配合并-内连接,交集的结果如下：")
print("    ================================================================")
df_inner=pd.merge(df,df1,how='inner')
print(df_inner.head(10))
print("")

print("    df_left=pd.merge(df,df1,how='left') #匹配合并-左连接,交集的结果如下：")
print("    ================================================================")
df_left=pd.merge(df,df1,how='left')
print(df_left.head(10))
print("")

print("    df_right=pd.merge(df,df1,how='right') #匹配合并-右连接,交集的结果如下：")
print("    ================================================================")
df_right=pd.merge(df,df1,how='right')
print(df_right.head(10))
print("")

print("    df_outer=pd.merge(df,df1,how='outer') #匹配合并-外连接,并集的结果如下：")
print("    ================================================================")
df_right=pd.merge(df,df1,how='outer')
print(df_right.head(10))
print("")

print("1.2 append")
result=df1.append(df,sort=False)
print("    result=df1.append(df,sort=False)的结果如下：")
print("    sort参数需指定，否则会有警告，但能执行")
print(result)
print("")

print("1.2 append")
result=df1.append(df,sort=True)
print("    result=df1.append(df,sort=True)的结果如下：")
print("    sort是对字段名称进行排序")
print(result)
print("")
     
print("1.3 join")
#result=df.join(df1,on='id')
print("    result=df.join(df1,on='id')的结果如下：")
print("    join方法报错,以后有机会研究")
#print(result)
print("")

print("1.4 concat连接很复杂，以后研究，用到时再说")
print("    frames=[df1,df2,df3]")
print("    result=pd.concat(frames)")
print("")

print("2. 设置索引")
print("   索引列被放置到第一列，再次设置其他列为索引列，原来的索引列不可见了")
print("   df_inner.set_index('id')")
df_inner.set_index('id')
print(df_inner)
print("")

print("3. 按照特定列的值排序")
df_inner=df_inner.sort_values(by=['age'])
print("   df_inner.sort_values(by=['age'])执行结果：")
print(df_inner)
print("")

print("4. 按照索引列排序")
df_inner=df_inner.sort_index()
print("   df_inner=df_inner.sort_index()执行结果：")
print(df_inner)
print("")

print("5.根据某列值设定给定列的值")
print("  相当于Excel在某个列中使用if公式的效果")
print("  df_inner['group']=np.where(df_inner['price']>3000,'high','low')")
df_inner['group']=np.where(df_inner['price']>3000,'high','low')
print(df_inner)
print("")

print("6.对复合多个条件的数据进行分组标记【以后再研究，没弄明白】")
print("  df_inner.loc[(df_inner['city']=='北京')&(df_inner['price'}>=4000),'sign']=1")
df_inner.loc[(df_inner['city']=='北京')&(df_inner['price']>=4000),'sign']=1
print(df_inner)
print("")

print("7.对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size")
print("  比较复杂，以后再研究吧")
print("pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size'])")
#df2=pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size'])
#print(df2)
print("")

print("8.将完成分裂后的数据表和原df_inner数据表进行匹配")
print("  df_inner=pd.merge(df_inner,split,right_index=True,left_index=True)")
print("  意思不甚明白，用到的时候再研究吧")
split=df
df_inner=pd.merge(df_inner,split,right_index=True,left_index=True)
print(df_inner)
print("")

print("五、数据提取")
print("    主要用到三个函数loc,iloc和ix，loc函数按标签值进行提取，iloc按位置进行提取。ix可同时按标签和按位置进行提取，已经废弃了")
print("")

print("1.按索引提取单行数值")
print("  df_inner.loc[3]")
data=df_inner.loc[3]
print("df_inner.loc[3]的结果是：\n{0}".format(data))
print("")
data=df_inner.loc[3].values
print("df_inner.loc[3].values的结果是：\n{0}".format(data))
print("")

print("2.按索引提取区域行数值")
print("  df.iloc[0:5]的结果是：")
data=df.iloc[0:5]
print(data)
print("")
print("  df.iloc[0:5].values的结果是：")
data=df.iloc[0:5].values
print(data)
print("")
print("  df.loc[0:5]的结果是：")
data=df.loc[0:5]
print(data)
print("")

print("3.重设索引")
print("  df_inder.reset_index()")
print(df)
print("")
df=df.sort_values(by=['age'])
print("  按年龄排序的数据：")
print(df)
print("")

df.set_index("id")
df=df.sort_index()
print("  按索引排序的数据：")
print(df)
print("")

df=df.sort_values(by=['age'])
print("  再次按年龄排序的数据：")
print(df)
print("")

df.reset_index()
df.sort_index()
print("  取消索引并按索引排序的数据：")
print(df)
print("")

print("4.设置日期为索引")
print("  df=df.set_index('date'),date列移动到首列")
df=df.set_index('date')
print(df)
print("")

print("  df=df.set_index('city')清除索引后设置，不会隐藏列")
df=df.reset_index()
df=df.set_index('city')
print(df)
print("")

print("  df=df.set_index('id')不清除索引直接设置，会隐藏列")
print("  前一个索引列city不见了")
df=df.set_index('id')
print(df)
print("")

print("5.提取24日之前的所有数据")
print("  df=df['date'][:'2019-10-24']")
print("  date不是索引列，提取数据会报错！")
print("  date索引，咋整都出错")
df.reset_index()
df.set_index('date')
df.sort_index()
#df=df[:'2019-10-24']
dfa=df.loc[df['date']>='20191024']
print(dfa)
print("")
      
print("6.使用iloc按位置区域提取数据")
print("  df.iloc[:3,:2] #冒号前后的数字不再是索引的标签名称而是数据所在的位置，从0开始，前三行，前两列")
dfa=df.iloc[:3,:2]
print(dfa)
print("")
df=df.reset_index()
dfa=df.iloc[:3,:2]
print(dfa)
print("")

print("7.适应iloc按位置单独提取数据")
print("  df.iloc[[0,2,5],[4,5]] #提取0、2、5行，4、5列")
#dfa=df1
dfa=df1.iloc[[0,2,3],[1,2]]
print(dfa)
print("")

print("8.使用ix按索引标签和位置混合提取数")
df=df.sort_values(by=['date'])
print(df)
print("")
print("  df.iloc[:'2019-10-24'] #24号之前，前四列数据")
dfa=df.loc[df['date']>'20191024']
dfa=dfa.iloc[:,:3]
#dfa=dfa.loc[:5]
print(dfa)
print("")
'''
print("9.判断某列是否为某值")
print("  df['city'].isin(['北京'])")
print(df)
print(df['city'].isin(['北京']))
print("")

print("10.判断某列是否为多个值")
print("  df['city'].isin(['北京','上海'])")
print(df)
print(df['city'].isin(['北京','上海']))
print("")

print("11.提取前三个字符，并生成数据表")
print("   pd.DataFrame(category.str[:3])")
df2=pd.DataFrame(df['city'].str[:1])
print(df2)
print("")

print("六、数据筛选")
print("    使用与、或、非三个条件配合大于、小于、等于对数据进行筛选，并进行计数和求和")
print("")

print("1.使用'与'进行筛选")
print(df)
print("")
df20=df.loc[(df['age']>25)&(df['city']=='上海'),['id','city','age']]
print(df20)
