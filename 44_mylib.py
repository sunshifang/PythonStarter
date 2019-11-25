print('''
除了内建模块外，Python还有大量的第三方模块。
基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，
只要找到对应的模块名字，即可pip安装。

一、Pillow
PIL: Python Imaging Library, 已经是Python平台事实上的图像处理标准库。
PIL功能非常强大，但API却非常简单易用。
Pillow是PIL的兼容版本，支持Python3.x，又加入了许多新特性。

01. 操作图像
from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')


二、requests
requests是urllib的升级版，增加了许多高级功能，使用却很方便。
import requests
r = requests.get('https://www.douban.com')
print(r.status_code)
print(r.text)
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
print(r.text)
print("")

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)
print(r.text)

三、chardet
字符串编码一直是令人头疼的问题，尤其是我们在处理一些不规范的第三方网
页的时候。虽然Python提供了Unicode表的str和bytes两种数据类型，并且可以
通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes
做decode()不好做。
对应未知编码的bytes，要把它转换成str,需要先猜测"编码",猜测的方法是先
收集各种编码的特征字符，根据特征字符判断，就能有很大概率"猜对".
当然不能从头自己写这个检测编码的功能，chardet这个第三方库来检测编码，
简单易用。
>>> chardet.detect(b'Hello, world!')
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

>>> data = '离离原上草，一岁一枯荣'.encode('gbk')
>>> chardet.detect(data)
{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

>>> data = '离离原上草，一岁一枯荣'.encode('utf-8')
>>> chardet.detect(data)
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

四、psutil = process and  system utilites
用Python编写脚本来简化日程的运维工作是Python的一个重要用途。在linux
下，有许多系统命令可以让我们时刻监控系统的运行状态，如ps, top, free
要获取这些系统信息，Python可以通过subprocess模块调用并获取结果，但
这样做很麻烦，尤其是要写很多解析代码。
在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。它
不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux/OSX
/UNIX/Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

01. 获取CPU信息
>>> import psutil
>>> psutil.cpu_count() # CPU逻辑数量
4
>>> psutil.cpu_count(logical=False) # CPU物理核心
2
# 2说明是双核超线程, 4则是4核非超线程
>>> for x in range(10):
...     psutil.cpu_percent(interval=1, percpu=True)
... 
[14.0, 4.0, 4.0, 4.0]
[12.0, 3.0, 4.0, 3.0]
[8.0, 4.0, 3.0, 4.0]
[12.0, 3.0, 3.0, 3.0]
[18.8, 5.1, 5.9, 5.0]
[10.9, 5.0, 4.0, 3.0]
[12.0, 5.0, 4.0, 5.0]
[15.0, 5.0, 4.0, 4.0]
[19.0, 5.0, 5.0, 4.0]

[9.0, 3.0, 2.0, 3.0]

02. 获取内存信息
>>> psutil.virtual_memory()
svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
>>> psutil.swap_memory()
sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)

03. 获取磁盘信息
>>> psutil.disk_partitions() # 磁盘分区信息
[sdiskpart(device='/dev/disk1', mountpoint='/', fstype='hfs', opts='rw,local,rootfs,dovolfs,journaled,multilabel')]
>>> psutil.disk_usage('/') # 磁盘使用情况
sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)
>>> psutil.disk_io_counters() # 磁盘IO
sdiskio(read_count=988513, write_count=274457, read_bytes=14856830464, write_bytes=17509420032, read_time=2228966, write_time=1618405)


04. 获取网络信息
>>> psutil.net_io_counters() # 获取网络读写字节／包的个数
snetio(bytes_sent=3885744870, bytes_recv=10357676702, packets_sent=10613069, packets_recv=10423357, errin=0, errout=0, dropin=0, dropout=0)
>>> psutil.net_if_addrs() # 获取网络接口信息
{
  'lo0': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0'), ...],
  'en1': [snic(family=<AddressFamily.AF_INET: 2>, address='10.0.1.80', netmask='255.255.255.0'), ...],
  'en0': [...],
  'en2': [...],
  'bridge0': [...]
}
>>> psutil.net_if_stats() # 获取网络接口状态
{
  'lo0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=16384),
  'en0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=1500),
  'en1': snicstats(...),
  'en2': snicstats(...),
  'bridge0': snicstats(...)
}

05. 获取进程信息
''')


print('''
virtualenv
为一个应用创建一套“隔离”的Python运行环境

图形界面
我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问TK的接口；
TK是一个图形库，支持多个操作系统，使用Tcl语言开发；
TK会调用操作系统提供的本地GUI接口，完成最终的GUI。
''')

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
