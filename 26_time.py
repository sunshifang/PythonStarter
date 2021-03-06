import time
import calendar

print()

ticks = time.time()
print("当前时间戳为:",ticks)
print()

localtime = time.localtime(time.time())
print("本地时间为：",localtime)
print()

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)
print()

print("格式化成2016-03-20 11:45:39形式")
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print()

print("格式化成Sat Mar 28 22:24:24 2016形式")
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print()

print("将格式字符串转换为时间戳")
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
print()

print("获取本地时区名称")
print (time.strftime("%Z", time.localtime()))
print()

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)
