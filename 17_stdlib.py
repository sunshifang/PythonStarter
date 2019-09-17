import builtins
import os
import shutil
import glob
import sys
import re
import math
import random
from urllib.request import urlopen
import zlib
from timeit import Timer


'''
printin("获取当前工作目录：")
print("os.getcwd() => {}".format(os.getcwd()))
os.chdir('d:/anjian')
print("执行os.chdir('d:/anjian')后：")
print("os.getcwd() => {}".format(os.getcwd()))
os.system('mkdir aaaa')
os.chdir('aaaa')
print("os.system('mkdir aaaa')")
print("os.chdir('aaaa')")
print("os.getcwd() => {}".format(os.getcwd()))
print(dir(os))
help(os)

print("## shutil #########################")
#shutil.copyfile('E:\coder\PythonStarter\func.py', 'd:\anjian\aaaa\func.py')
os.system('cp E:\coder\PythonStarter\func.py, d:\anjian\aaaa\func.py')
print(os.system('ls -l'))
os.chdir('e:/coder/PythonStarter')
print(glob.glob('*.py'))
print()

print(sys.argv)
print("错误输出重定向")
sys.stderr.write("Warning,log file not found")
print()
print()

print("字符串正则匹配")
print("re.findall(r'\bf[a-z]*','which foot or hand fell fastest')")
print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))
print("re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')")
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print()
print()

print("数学")
print("math.cos(math.pi / 4) => {}".format(math.cos(math.pi / 4)))
print("math.log(1024, 2) => {}".format(math.cos(math.pi / 4)))
print()
print()

print("random提供了生成随机数的工具")
print("random.choice(['apple', 'pear', 'banana']) => {}".format(random.choice(['apple', 'pear', 'banana'])))
print("random.sample(range(100), 10) => {}".format(random.sample(range(100), 10)))
print("random.random() => {}".format(random.random()))
print("random.randrange(6) => {}".format(random.randrange(6)))


print("访问互联网")
#for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
for line in urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    #if 'EST' in line or 'EDT' in line:  # look for Eastern Time
    print(line)


print("日期时间")
from datetime import date
now = date.today()
print("date.today() => %s" % now)
print('now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")')
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
print()
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)



print("数据压缩")
print("s = b'whitch which has which witches wrist watch'")
s = b'whitch which has which witches wrist watch'
print("len(s) => %s " % len(s))
t=zlib.compress(s)
print("t=zlib.compress(s)")
print(len(t))
print("zlib.decompress(t)")
s=zlib.decompress(t)
print(s)
print("zlib.crc32(s)")
u=zlib.crc32(s)
print(u)



print("性能度量")
print("Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()")
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print("Timer('a,b = b,a', 'a=1; b=2').timeit()")
print(Timer('a,b = b,a', 'a=1; b=2').timeit())



print("测试模块")
#测试模块未见效果
def average(values):
    """Computes the arithmetic mean of a list of nubmers.
    print(average([20,30,70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
values = [20,30,70]
doctest.testmod(average(values))


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main()
'''
