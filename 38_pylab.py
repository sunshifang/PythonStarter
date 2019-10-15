from pylab import *
import numpy as np

'''
X = np.linspace(-np.pi,np.pi,256,endpoint=True)
print('x = np.linspace(-np.pi,np.pi,256,endpoint=True)')
print('x是一个numpy数组，包含了从-π到+π等间隔的256个值')
print('C和S则分别是这256个值对应的余弦和正弦函数值组成的numpy数组')
C,S = np.cos(X),np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.show()
'''
'''
print('matplotlib的默认配置')
print('***************************************')
print('# 创建一个8*6点的图，并设置分辨率为80')
figure(figsize=(8,6),dpi=80)
print()

print('# 创建一个1*1的子图，接下来的图样绘制在其中的第一块(也是唯一的一块)')
subplot(1,1,1)
X = np.linspace(-np.pi,np.pi,256,endpoint=True)
C,S = np.cos(X),np.sin(X)

print('# 绘制余弦曲线，使用蓝色的、连续的、宽度为2(像素)的线条')
plt.plot(X,C,color="blue",linewidth=2.0,linestyle='-')

print('# 绘制正弦曲线，使用绿色的、连续的、宽度为1(像素)的线条')
plt.plot(X,S,color='green',linewidth=1.0,linestyle='-')

print('# 设置横轴上下限')
plt.xlim(-4.0,4.0)

print('# 设置横轴刻度')
#plt.xticks(np.linspace(-4,4,17,endpoint=True))
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'+\pi/2$',r'$+\pi$'])


print('# 设置纵轴上下限')
plt.ylim(-2.0,2.0)

print('# 设置横轴刻度')
#plt.yticks(np.linspace(-1,1,5,endpoint=True))
plt.yticks([-1,0,+1],[r'$-1$',r'$0$',r'$+1$'])

print('# 以分辨率72来保存图片')
savefig('tmp/excerice_1.png',dpi=172)

print('# 移动脊柱')
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

print('# 添加图例')
plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
legend(loc='upper left')

print('# 特殊点做注释')
t = 2*np.pi/3
plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='blue')

annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')

annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

print('# 精益求精')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))


print('# 在屏幕上显示')
plt.show()
'''

print('# 创建一个1*1的子图，接下来的图样绘制在其中的第一块(也是唯一的一块)')
x = np.arange(0, 100)
plt.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
#作图1
plt.subplot(2,3,1)
plt.plot(x, x)
#作图2
plt.subplot(2,3,2)
plt.plot(x, -x)
#作图3
plt.subplot(2,3,3)
plt.plot(x, x ** 2)

#作图4
plt.subplot(2,3,4)
plt.plot(x, np.sin(x))

#作图5
plt.subplot(2,3,5)
plt.plot(x, 2*x)

#作图6
plt.subplot(2,3,6)
plt.plot(x, np.tan(x))


plt.show()


