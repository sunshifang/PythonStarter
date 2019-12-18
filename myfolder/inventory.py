import pandas as pd
import numpy as np
import os as os

pd.set_option('max_columns', 20)
pd.set_option('max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.2f' % x) # 禁用科学计数法
pd.set_option('display.max_rows',None)

#01 打开文件
df_output_stock = pd.read_excel(r'I:\#Data\20191216\限额领料单列表.XLS', logfile=open(os.devnull, 'w'))
df_erp_stock = pd.read_excel(r'I:\#Data\20191216\库存展望.XLS', logfile=open(os.devnull,'w'))
df_bar_stock = pd.read_excel(r'I:\#Data\20191216\库存汇总表.xlsx', logfile=open(os.devnull,'w'),usecols=[0,6])
df_inv_stock = pd.read_excel(r'I:\#Data\20191216\库存盘点单列表.xlsx', logfile=open(os.devnull,'w'),usecols=[0,1,2,4,5,6,7,8,9])

#print(df_inv_stock)
df_inv_stock['盘点日期'] = df_inv_stock.apply(lambda row:row[1][0:5])

#02 对限额领料单进行分类汇总，求出出库数量
df_output_stock_sum = df_output_stock.groupby('材料编码').aggregate({'计划出库数量':'sum'}).reset_index()

#03 连接表
df = pd.merge(df_erp_stock,df_output_stock_sum,left_on='存货编码',right_on='材料编码',how='left').fillna(0)[0:6877]

#04 计算列
df['预分单库存'] = df.apply(lambda row: float(row.现存量) - row.计划出库数量, axis=1)
df['存货信息存货名称'] = df.apply(lambda row:row[1] if(len(row[1])<=5) else row[1][0:5]+'...',axis=1)
df['存货信息规格型号'] = df.apply(lambda row:row[2] if(len(str(row[2]))<=15) else str(row[2])[0:15]+'...',axis=1)

#05 修改列名称
df.rename(columns={'存货信息存货编码':'存货编码',
                   '存货信息存货名称':'存货名称',
                   '存货信息规格型号':'规格型号',
                   '存货信息主计量单位':'单位',
                   '计划出库数量':'出库合计'},inplace=True)


#06 连接ERP库存表与条码库存表
df1 = pd.merge(df,df_bar_stock,left_on='存货编码',right_on='资材编号',how='left').fillna(0)

#07 显示列信息
df1 = df1[['存货编码','存货名称','规格型号','单位','库管员','现存量','出库合计','预分单库存','期末数量']]
df1.to_excel('result.xlsx',index=False)

#df_inv_stock['单据日期'] = df_inv_stock.apply(lambda row:row[1][:10])
df3 = df_inv_stock.groupby(['创建人','单据日期']).aggregate({'单据编号':'count'})
#df2 = df_inv_stock[df_inv_stock['创建人']=='安振东']
#df2 = df2[['单据日期','品名','规格','创建人']]
df2 = df_inv_stock[df_inv_stock['单据日期']>'2019/12/01']
#df2=df2.groupby(['创建人','单据日期']).aggregate({'单据日期':'count'})
df4 = pd.pivot_table(
    df2,
    values='单据编号',
    columns='创建人',
    index='单据日期',
    aggfunc='count',
    fill_value=0,
    #margins=True,
    margins_name='合计')
df3 = df4.reset_index()

import matplotlib.pyplot as plt
plt.figure(figsize=(20,16))

person = ['井海峰','蒋鹏','黄明喜','吕永全','齐华香','任亚萍','谈文丽','安振东','邢宝桦']
i=0
for p in person:
    i = i + 1
    plt.subplot(3,3,i)
    x = df3['单据日期']
    y = df3[p]
    plt.bar(x,y,label="test")
    plt.legend()

plt.subplots_adjust(wspace=5,hsapce=5)
plt.show()

plt.savefig('test1.jpg')
