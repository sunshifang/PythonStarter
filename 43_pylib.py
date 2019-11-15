print('''
常用内建模块
01. datetime

from datetime import datetime
from datetime 这个datetime是模块名，这个模块中包含一个datetime类
如果仅导入import datetime，则必须引用全名datetime.datetime

01）获取当前日期和时间
''')
from datetime import datetime
now = datetime.now()
print("datetime.now() = ",datetime.now())
print("type(datetime.now()) = ",type(datetime.now()))

print('''
02）获取指定日期和时间
要获取指定某个日期和时间，我们直接用参数构造一个datetime
''')
dt = datetime(2015,4,19,12,20)
print("datetime(2015,4,19,12,20)",dt)

print('''
03）datetime转换为timestamp
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00
UTC+00:00时区的时刻，记为0(1970年以前的时间timestamp为负数)，当前
时间就是相对于epoch time的秒数，称为timestamp.
timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确
定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的
电气时间是以timestamp表示的，因为全球各地计算机在任意时刻的timestamp
都是完全相同的(假定时间以校准)。
把一个datetime类型转换为timestamp只需要简单调用timestamp()方法
Python的timestamp是一个浮点数，如果有小数位，表示毫秒数。
某些编程语言(如java javascript)的timestamp使用整数表示毫秒数，这种
情况下只需要把timestamp除以1000就得到Python的浮点数表示法。
''')
dt = datetime(2015,4,19,12,20)
print("datetime(2015,4,19,12,20) =",dt)

print('''
03）timestamp转换为datetime
''')
print("转换为本地时间：")
print("datetime.fromtimestamp(1429417200.0) =",datetime.fromtimestamp(1429417200.0))
print("")
print("转换为UTC时间：")
print("datetime.utcfromtimestamp(1429417200.0) =",datetime.utcfromtimestamp(1429417200.0))

print('''
04）str转换为datetime
''')
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print("datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S') =",cday)

print('''
05）datetime转换为str
''')
now = datetime.now()
print("datetime.now().strftime('%a, %b %d %H:%M') =",now.strftime('%a, %b %d %H:%M'))

print('''
06）datetime加减
''')
from datetime import timedelta
now = datetime.now()
print("datetime.now() =",now)
print("datetime.now() + timedelta(hours=10) =",datetime.now() + timedelta(hours=10))
print("datetime.now() - timedelta(days=1) =",datetime.now() - timedelta(days=1))

print('''
07）本地时间转换为UTC时间
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指
UTC+0:00时区的时间。
datetime类型有一个时区属性tzinfo，但是其值默认为None，所以无法区分这个datetime到底是
哪个时区，除非强行给datetime设置一个时区。
如果系统时区恰好是UTC+8:00,代码tzinfo=timezone(timedelta(hours=8))就是正确的，否则，
不能强制设置时区。
''')
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print("now = ",now)
dt = now.replace(tzinfo=tz_utc_8)
print("now.replace(tzinfo=tz_utc_8) =",dt)

print('''
08. 时区转换
我们可以通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
''')
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print("utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)")
print("utc_dt =",utc_dt)
print("用astimezong()转换时区为北京时间：")
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print("utc_dt.astimezone(timezone(timedelta(hours=8))) =",bj_dt)
print("转换为东京时间：")
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print("utc_dt.astimezone(timezone(timedelta(hours=9))) =",tokyo_dt)
print('''
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基
准时间。
利用带时区的datetime通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区专户已到其他时区，任何带时区的datetime都可以正确转换。
小结：
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime,最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区无关。


02. collections

01）namedtuple
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并
可以使用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以
根据属性来引用，使用十分方便。
使用场景：tuple表示一个不变集合，点坐标p=(1,2),看到(1,2)很难看出这个tuple表示的是坐
标，定义一个类又不值得，小题大做，这时就可以使用namedtuple.
''')
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print("p.x = %s, p.y= %s" % (p.x,p.y))
print("isinstance(p,Point) = %s" % isinstance(p,Point))
print("isinstance(p,tuple) = %s" % isinstance(p,tuple))

print('''
02）deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性
存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
''')
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

print('''
03）defaultdict
使用dict时，如果引用的key不存在，就会抛出keyError。如果希望key不存在是，返回一个默认
值，就可以使用defaultdict.
有可能Python3已经有顺序了
''')
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print("dd['key1'] =",dd['key1'])
print("dd['key2'] =",dd['key2'])

print('''
04) OrderDict
使用dict时，key是无序的。在对dict做迭代时，无法确定key的顺序。OrderDict可以保持顺序
OrderedDict的key会按照插入的顺序排列，不是key本身的顺序

''')
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print("dict([('a',1),('b',2),('c',3)]) =",d)
d['z']=33
d['y']=33
d['x']=33
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print("OrderedDict([('a',1),('b',2),('c',3)]) = ",od)
od['z']=1
print(od)

print("dict实现的先进先出队列")
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

print('''
05) ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。chainMap本身也是一个dict，但是查找的
时候，会按照在内部的dict一次查找。
什么时候使用ChainMap最合适？举个例子，应用程序往往需要传入参数，参数可以通过命令行传入，
可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命
令行参数，如果没有，再查环境变量，如果没有，就使用默认参数。

06）Counter
Counter是一个简单的计数器，实际上也是dict的子类
''')
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

print('''
03. base64
Base64是一种用64个字符来表示任意二进制数据的方法
用记事本打开exe, jpg, pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法
显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二
进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
Base64的原来很简单:

首先，准备以包含64个字符的数组：
['A','B','C', ... 'a','b','c', ... '0','1', ... '+','/']

然后，对二进制数据进行处理，每3个字节一组，一共是 3*8=24bit 划为4组，每组正好6个bit:

这样我们得到4个数组作为索引，然后查表，获得相应的4个字符，就是编码后的字符串

所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的
文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办，Base64用\x00在末尾补足
后，再在编码的末尾加上一个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"
的base64编码，其实就是把字符+和/分别变成-和_
''')
import base64
code = base64.b64encode(b'binary\x00string')
print("base64.b64encode(b'binary\x00string') => ",code)
code = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print("base64.b64decode(b'YmluYXJ5AHN0cmluZw==') => ",code)
code = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print("base64.b64encode(b'i\xb7\x1d\xfb\xef\xff') => ",code)
code = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print("base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff') => ",code)

print('''
还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，一般没有必要
Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
Base64适用于小段内容的编码，比如数字证书签名，Cookie的内容等等。
由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码
后会把=号去掉。
去掉=字符后怎么解码呢？因为Base74是把3个字节变成4个字节，所以Base64编码的长度永远是4的倍
数，因此，需要加上=号，把Base64字符串长度变为4的倍数，就可以正常解码了。


04. struct
准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组等于
二进制str。而在C语言里，我们可以很方便地用struct、union。在Python中，比方说要把一个32位
无符号整数变成字节，也就是4个长度的bytes，你的配合位运算符这么写：
>>> n = 10240099
>>> b1 = (n & 0xff000000) >> 24
>>> b2 = (n & 0xff0000) >> 16
>>> b3 = (n & 0xff00) >> 8
>>> b4 = n & 0xff
>>> bs = bytes([b1, b2, b3, b4])
>>> bs
b'\x00\x9c@c'
非常麻烦，如果换成浮点数就无能为力了
Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换，以后再研究。


05. hashlib
摘要算法简介
Python提供了常见的摘要算法，如MD5,SHA1等等
摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长
度固定的数据串(通常用16进制的字符串表示)。
摘要函数是一个单向函数，反向推导十分困难。
''')
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print("'how to use md5 in python hashlib?'加密后的结果是")
print(md5.hexdigest())
print("如果数据很大，可以多吃调用update()")

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

print("")
print("SHA!的调用方法与MD5的调用方法相同")
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

print('''
06. hmac
为了防止黑客通过彩虹表根据根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计
算，需要增加一个salt来使得相同的输入也能得到不同的哈希，这样就大大增加了黑客破解的难度。
如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，把salt
看做一个口令，加salt的哈希就是：计算一段message的哈希时，根据不同口令计算出不同的哈希，
要验证哈希值，必须同时提供正确的口令。
这实际上就是hmac算法：keyed-hashing for Message Authentication。它通过一个标准算法，在计
算哈希的过程中，把key混入计算过程中。
和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用
Hmac替代我们的自己的salt算法，可以使程序算法更标准，也更安全。
小结
Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算"杂凑"后的hash，使用
hmac算法比标准hash算法更安全，因为针对的message，不同的key会产生不同的hash。
''')
import hmac
message = b'Hello world!'
key = b'secret'
h = hmac.new(key,message,digestmod='md5')
print(h.hexdigest())

print('''
07. itertolls
itertools模块提供了用于操作迭代对象的函数
itertools提供了几个“无限”迭代器：
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个
元素生成出来，事实上也不可能在内存中创建无限多个元素。
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhie()等函数根据条件判断来截取出一个
有限序列。
itertools提供的几个迭代器操作函数更加有用：
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
groupby()把迭代器中相邻的重复元素挑出来放在一起
''')
import itertools
'''
natuals = itertools.count(1)
for n in natuals:
    print(n) 

cs = itertools.cycle('abc')
for c in cs:
    print(c)
'''
ns = itertools.repeat('A',3)
for n in ns:
    print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('ABC','XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))


print('''
08. contextlib
在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源
的一个方法是try ... finally。

try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close()

但写起来有些繁琐，Python的with语句允许我们非常方便的使用资源，而不必担心资源没有关闭。上
面的代码可以简化为：
with open('/path/to/file','r') as f:
    f.read()

并不是只有open()函数返回的fp对象才能使用with语句，实际上，任何对象，只要正确实现了上下文
管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)

这样，我们就可以把自己写的资源对象用于with语句
with Query('Bob') as q:
    q.query()

01）@contextmanager
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，如下：

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

@contextmanager这个decorator接受一个generator,用yield语句把with ... as var 把变量输出出去
然后，with语句就可以正常地工作了。

很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以使用@contextmanager实现。
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

代码执行的顺序是：
    1. with语句首先执行yield之前的语句，因此打印出<h1>;
    2. yield调用会执行with语句内部的所有语句，因此打印出hello和world;
    3. 最后执行yield之后的语句，打印出</h1>

02) @closing
如果一个对象没有实现上下文，我们就不能把它用于with语句。这时候，可以用closing()来把对象
变为上下文对象。例如用with语句使用urlopen()

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

closing也是一个经过@contextmanager装饰的generator，这个generator编写起来非常简单：

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
它的作用就是把任意对象变为上下文对象，并支持with语句。


09. urllib
urllib提供了一系列用于操作url的功能

01）Get
url的request模块可以非常方便地抓取url内容，也就是发送一个GET请求到指定的页面，然后返回
HTTP的响应。
from urllib import request

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

02) Post
如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

03）Handler
如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，如下
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass


10. XML
XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解

01）DOM vs SAX
操作XML有两种方法，DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要
自己处理事件。
正常情况下优先考虑SAX，因为DOM实作太占内存。
在Python中使用SAX解析XML非常简洁，通常我们关系的事件是start_element, end_element 以及
char_data,准备好这三个函数，就可以解析XML了
举个例子，当SAX解析器读到一个节点时：
<a href="/">python</a>
会产生三个事件
    1. start_element, 读取<a href="/">时；
    2. char_data，读取python时；
    3. end_element，读取</a>时。
需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来
在EndElementHandler里面再合并。

生成XML的解构一般都很简单，拼接字符串即可。要生成复杂的XML，建议用JSON
 
''')

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


print('''
11. HTMLParser
虽然HTML本质上是XML，但由于HTML语法不那么严格，不能用DOM或SAX来解析。HTMLParser简单易用。

feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
特殊字符有两种，一种是英文表述的&nbsp; ，一种是数字表示的&#1234; 这两种字符都可以通过
Parser解析出来。
''')
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

    
