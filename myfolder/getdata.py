
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os as os


def getResult(x):
    if(x.结存_x==x.结存_y):
        return '相等'
    elif((x.盘点差>=-0.15) & (x.盘点差<0.05)):
        return '合格'
    elif(((x.盘点差>=-1.5) & (x.盘点差<-0.15)) | ((x.盘点差>=0.05) & (x.盘点差<1))):
        return '有差'
    elif((x.盘点差<-1.5) | (x.盘点差>=1)):
        return '差大'
    
pd.set_option('max_columns', 20)
pd.set_option('max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.2f' % x) # 禁用科学计数法
#pd.set_option('display.max_rows',None)

#打开文件
df_ERP_output_stock1 = pd.read_excel(r'I:\\#Data\\201912\\20191228\\12限额领料单列表.XLS',usecols=[2,3,6,4]).fillna(0)
df_ERP_output_stock2 = pd.read_excel(r'I:\\#Data\\201912\\20191228\\1限额领料单列表.XLS',usecols=[2,3,4,6]).fillna(0)
df_bar_output_stock1 = pd.read_excel(r'I:\\#Data\\201912\\20191228\\1领料出库单列表.XLSx',usecols=[6,10]).fillna(0)
df_erp_inv = pd.read_excel(r'I:\\#Data\\201912\\20191228\\库存展望.XLS',usecols=[6,7,8,9,10,11]).fillna(0)
df_bar_inv = pd.read_excel(r'I:\\#Data\\201912\\20191228\\库存汇总表.xlsx',usecols=[0,6])
df_stagnate = pd.read_excel(r'I:\\#Data\\201912\\20191228\\盘点完成.xlsx',usecols=[0,4,7])
#df_inv_check = pd.read_excel(r'I:\\#Data\\201912\\20191228\\库存盘点单列表.xlsx',usecols=[0,1,2,4,5,6,7,8,9])
#df_erp_inv=df_erp_inv.iloc[0:10]
df11 = pd.pivot_table(df_ERP_output_stock1,values='计划出库数量',index='材料编码',aggfunc='sum')
df12 = pd.pivot_table(df_ERP_output_stock2,values='计划出库数量',index='材料编码',aggfunc='sum')
    
#df1是ERP结存
df1 = pd.merge(df_erp_inv,df11,left_on='存货编码',right_on='材料编码',how='left').fillna(0)
df1 = pd.merge(df1,df12,left_on='存货编码',right_on='材料编码',how='left').fillna(0)
df1['现存量']=df1['现存量'].astype('float')
df1['结存'] = df1.apply(lambda x:x.现存量-x.计划出库数量_x-x.计划出库数量_y,axis=1)
#df1
#########################################################################
    
#1月份出库合计
df21 =pd.pivot_table(df_bar_output_stock1,values='计划数量',index='资材编号',aggfunc='sum')
    
#12月份条码结存
df2 = pd.merge(df_bar_inv,df21,on='资材编号',how='left').fillna(0)
df2['结存'] = df2.apply(lambda x:x.期末数量+x.计划数量,axis=1)
    
##########################################################################
df0 = pd.merge(df1,df2,left_on='存货编码',right_on='资材编号',how='inner')
df = pd.merge(df0,df_stagnate,on='存货编码',how='left').fillna(0)
df['出库率'] = df.apply(lambda x:'高' if((x.计划出库数量_x+x.计划出库数量_y)>0) else '低',axis=1)
df['盘点差'] = df.apply(lambda x:0 if(x.结存_x==0) else (x.结存_x-x.结存_y)/x.结存_x,axis=1)
df['结论'] = df.apply(lambda x:getResult(x),axis=1)

#选择数据后，不能进行数据透视表操作
#df = df[['存货编码','存货名称','规格型号','单位','库管员','结存_x','结存_y','出库率','盘点差','现存量_y','类别','结论']]

###########################################################################
df = df.pivot_table(index='库管员',columns='结论',values='资材编号',aggfunc='count',margins=True,margins_name='合计')
#计算百分比
df['合格A1']=df.apply(lambda x:x.合格/x.合计*100,axis=1)
df['差大A']=df.apply(lambda x:x.差大/x.合计*100,axis=1)
df['有差A']=df.apply(lambda x:x.有差/x.合计*100,axis=1)
df['相等A']=df.apply(lambda x:x.相等/x.合计*100,axis=1)
df['合格A']=df.apply(lambda x:x.合格A1+x.相等A,axis=1)
#df.sort_values(by=['合格A'],ascending=True)

df.reset_index()
df = df[0:9].sort_values(by=['合格A'],ascending=False)
