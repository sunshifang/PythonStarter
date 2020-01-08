plt.figure(figsize=(17,7))
plt.rcParams['font.sans-serif']='SimHei'
plt.subplot(1,1,1,xmargin=0.01,ymargin=0.1)

#x = ['井海峰','蒋鹏','黄明喜','吕永全','齐华香','任亚萍','谈文丽','安振东','邢宝桦']
x = np.array([1,2,3,4,5,6,7,8,9])
#y1 = np.array([108,150,138,119,212,188,117,174,205])
#y2 = np.array([108,150,138,119,212,188,117,174,205])
y1 = np.array(list(df['相等A'][0:9]))
y2 = np.array(list(df['合格A'][0:9]))
y3 = np.array(list(df['有差A'][0:9]))
y4 = np.array(list(df['差大A'][0:9]))
plt.bar(x,y1,width=0.2,label="相等")
plt.bar(x+0.2,y2,width=0.2,label="合格")
plt.bar(x+0.4,y3,width=0.2,label="有差")
plt.bar(x+0.6,y4,width=0.2,label="差大")

#设置数据标签
for a,b in zip(x,y1):
    plt.text(a,b,round(b,1),ha='center',va='bottom',fontsize=12)
for a,b in zip(x,y2):
    plt.text(a+0.2,b,round(b,2),ha='center',va='bottom',fontsize=12)
for a,b in zip(x,y3):
    plt.text(a+0.4,b,round(b,2),ha='center',va='bottom',fontsize=12)
for a,b in zip(x,y4):
    plt.text(a+0.6,b,round(b,2),ha='center',va='bottom',fontsize=12)
plt.legend(fontsize=20)
#plt.xlabel('姓名',fontsize=15,labelpad=1)
plt.ylabel('百分比',fontsize=25)
plt.yticks(fontsize=20)
plt.xticks(x+0.2,['任亚萍','井海峰','黄明喜','谈文丽','齐华香','邢宝桦','吕永全','蒋鹏','安振东'],fontsize=20) #,rotation=12
plt.title(label='2019年12月份盘点',fontsize=35)
plt.grid(b=True,axis='y') 
plt.subplots_adjust(left=0,bottom=0,right=1,top=10,wspace=5,hspace=55)
plt.tight_layout()
plt.savefig('盘点结果.jpg')
