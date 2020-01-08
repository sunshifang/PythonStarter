import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']='SimHei'

# 生成数据
'''
x = np.linspace(0, 20, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(50, 100, 20)
y3 = np.random.randint(50, 100, 20)
print('x=',x)
print('y1=',y1)
print('y2=',y2)
print('y2=',y2)
'''
x = [1,2,3,4,5,6,7,8,9]
y1 = [2.4,4.3,8.6,10.9,8.2,11.3,15.5,1.4,16.6]
y2 = [13.0,25.3,29.9,29.3,35.4,34.0,39.1,46.9,54.5]

# 堆积柱状图
plt.bar(x, y1, color='r', label='有差')
plt.bar(x, y2, bottom=y1, color='g', label='差大')
#plt.bar(x, y3, bottom=y1+y2, color='c', label='英语')

# 显示范围
plt.xlim(-2, 22)
plt.ylim(0, 280)

# 添加图例
plt.legend(loc='upper right')
plt.grid(axis='y', color='gray', linestyle=':', linewidth=2)

plt.show()


