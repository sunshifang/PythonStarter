print('''
http协议简介

在web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示
出来。服务器和浏览器之间的传输协议就是HTTP, 所以：
    ·HTML是一种用量定义网页的文本，会HTML，就可以编写网页；
    ·HTTP是在网络上传输HTML的协议，用于服务器和浏览器的通信。
    
Chrome浏览器调试网页
·Elements：显示网页结构
·Network显示浏览器和服务器的通信

Http请求头结构
·GET /HTTP/1.1
  GET 表示一个读取请求，将从服务器获得网页，
  /   表示URL的路径，URL总是以 / 开头，/ 就表示首页
  HTTP/1.1 表示采用的HTTP协议的版本是1.1 。目前HTTP协议的版本是1.1, 但大部分服务器也支持
           1.0版本，主要区别在于1.1版本允许http请求复用一个TCP连接，以加快传输速度。
·从第二行开始，每一行都类似于Xxx: abcdf; 比如：
  Host: www.sina.com.cn 表示请求的域名是www.sina.com.cn。如果一台服务器有多个网站，服务器
                        就需要通过Host来区分浏览器请求的是哪个网站。
  Response Headers: 显示服务器返回的原始响应数据
  HTTP响应分为Header和Body两部分(Body是可选项)，我们在Network中看到的Header重要行如下：
  ·200 ok
  200表示一个成功的响应，后面的ok是说明。
  失败的响应有404 Not Found: 网页不存在， 500 Internal Server Error: 服务器内部错误
  ·Content-Type: text/html
  content-Type指示响应内容，这里是text/hmel表示HTML网页。浏览器就是依靠Content-Type来判断
  响应的内容是网页还是图片，是视频还是音乐。
HTTP响应的body就是HTML源码。
当浏览器读取到新浪首页的HTML源码后，它会解析HTML, 显示页面，然后根据HTML里面的各种链接，
再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSSd等各种资源，
最终显示出一个完整的页面。所以Network下面有很多额外的HTTP请求。

HTTP请求
步骤1：浏览器向服务器发送HTTP请求，包括
    方法：GET仅请求资源，POST会附带用户数据；
    路径：/full/url/path；
    域名：由Host头指定 → Host: www.sina.com.cn
    其他相关的Header；
    如果是POST，那么请求还包括一个Body，包含优化数据。
步骤2：服务器向浏览器返回HTTP响应，包括
    响应代码：200表示成功，3XX表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务端错误
    响应类型：由Content-Type指定，例如Content-Type: text/hmtl;charset=utf-8表示响应类型是
              HTML文本，并且编码是UTI-8，Content-Type:image/jpeg表示响应类型是JPEG图片；
    其他相关的Header；
    通常服务器的HTTP响应会携带内容，也就是一个Body，包含响应的内容，网页的源码在Body中。
步骤3：如果浏览器还需要继续向服务器请求其他资源，如图片，就再次发出HTTP请求，重复步骤1,2。

Web采用的HTTP协议采用了非常简单的请求响应模式，从而大大简化了开发。当我们编写一个页面时，
我们只需要在HTTP响应中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求
图片和视频，它就会发送另一个HTTP请求，因此,一个HTTP请求只处理一个资源。

HTTP协议同时具备极强的扩展性，虽然浏览器请求的是http://www.sina.com.cn的首页，但是新浪在
HTML中可以链入其他服务器的资源，比如<img src="http://i1.sinaimg.cn/home/2013/35.png">，从
而将请求压力分散到各个服务器上，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，
就形成了World Wide Web，简称“三大不留”（www）。

HTTP格式
每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。
HTTP协议是一种文本协议，所以，它的格式也非常简单。HTTP GET请求的格式：
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

每个Header一行一个，换行符是\r\n
HTTP POST请求的格式：
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3


body data

当遇到两个连续的\r\n时，Header部分结束，后面的数据全是Body。
HTTP响应的格式：
200 ok
Header1: Value1
Header2: Value2
Header3: Value3


body data

HTTP响应如果包含body，也就是通过\r\n\r\n来分隔的。请再次注意：
Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本；如果是图片，Body就是图片
的二进制数据。
当存在Content-Encoding时，Body的数据是被压缩的，最常见的压缩方式是gzip，所以，看到了
Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少
Body的大小，加快网络传输。
''')
           
  
