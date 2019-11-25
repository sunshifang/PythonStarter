print('''
爬虫
''')
'''
import requests        #导入requests包
url = 'http://192.168.2.107/otcwms/Page/WMS/CConsumingOutStockBill/CConsumingOutStockBillList.aspx?itemNo=c032503&pTypeNo=main'
headers = {'Host': 'www.douban.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive'
           }

headers = {
 # 假装自己是浏览器
 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
 # 把你刚刚拿到的Cookie塞进来
 'Cookie': 'ASP.NET_SessionId=osdyfavda4b5on55mqvqfn45; forums=7E880739E536E5807328C4683BCB8042A8A73D1E5C1A6BF648411962CC95F4FAE64DB309CCC44445051084503439778373BF5398FA1FA2694DA3B6CF474197C20A48C0C87C807E14D3F8D6011055C80B1771DB15E3692617CC2F0F68A864A73D30EFEFB61135AB9E269AFAE82F2D33DBC2C46AA9'
}
session = requests.Session()
response = session.get('http://192.168.2.107/otcwms/Page/WMS/CConsumingOutStockBill/CConsumingOutStockBillList.aspx?itemNo=c032503&pTypeNo=main', headers=headers)
print(response.text)
strhtml = requests.post(url,headers)        #Get方式获取网页数据
print(strhtml.text)
'''

'''
import requests
#from bs4 import BeautifulSoup

#第一步：取得用户名与密码的动态名称，名称是动态的，及其他动态登录信息
url = "http://www.v2ex.com/signin"

headers = { "User-Agent" : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36',
           "Referer": "http://www.v2ex.com/signin"
           }
session=requests.session()

response=session.get(url,headers=headers)
html=response.content
soup=BeautifulSoup(html,'html.parser') 
s1=str(soup)#观测登录页面，需要取得那些信息
username=input('请输入用户名:')
password=input('请输入用密码:')
#用户名与密码的动态名称
usernamecode=soup.find('input',{'placeholder':'用户名或电子邮箱地址'})['name']#每次可能不相同，本次是：2c014ff2140fe6171682d56a2228428f167195488a1d652cf5c6d18a0360a5d6
passwordcode=soup.find('input',{'type':'password'})['name']#本次结果是：2c014ff2140fe6171682d56a2228428f167195488a1d652cf5c6d18a0360a5d6
once=soup.find('input',{'name':'once'})['value']
next=soup.find('input',{'name':'next'})['value']
postData={
          usernamecode:username,
          passwordcode:password,
          'once':once,
          'next':next

          }
#第2步：真正提交
response=session.post(url,postData,headers)
status=response.status_code #得到结果：200,表明登录成功

#第3步：依据session进入任何想进入的页面
response = session.get('https://www.v2ex.com/settings',headers=headers) #OK
resonse = session.get('https://v2ex.com/mission/daily',headers=headers) #OK
resonse = session.post('https://v2ex.com/mission/daily',headers=headers) #OK
resonse = session.get('https://www.v2ex.com/member/'+username,headers=headers) #OK  

page=response.content.decode('utf-8') #汉字无乱码

#如果取得的page是json数据，则采用下面方法转换,如果不是json,则转换异常为：JSONDecodeError
import json
data=json.loads(page)
'''



import requests
import urllib
import random
from datetime import datetime
import http.cookiejar as cookielib

# session代表某一次连接
huihuSession = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
huihuSession.cookies = cookielib.LWPCookieJar(filename = "huihuCookies.txt")
 
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
header = {
    # "origin": "https://passport.huihu.cn",
    "Referer": "http://hh.haiper.com.cn/w/wander/user/login/",
    'User-Agent': userAgent,
}
 
def login(account, password):
    # 
    print ("开始模拟登录嘻嘻嘻")
 
    postUrl = "http://192.168.2.107/otcwms"
    postData = {
        "username": account,
        "password": password,
    }
    
    # 使用session直接post请求
    responseRes = huihuSession.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200    
    #responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    #print(f"text = {responseRes.text}")
    huihuSession.cookies.save()
def isLoginStatus():
    # 通过访问个人中心页面的返回状态码来判断是否为登录状态
    for i in range(2131,2134):
        routeUrl = "http://hh.haiper.com.cn/w/bench/extend/health/trade/all?nickname=&type=&gender=&level=&range%5Bstart%5D=2014-11-11+14%3A57&range%5Bend%5D=2018-06-06+14%3A57&page="+str(i)
        
    # 下面有两个关键点
        # 第一个是header，如果不设置，会返回500的错误
        # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
        # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
        # allow_redirects = False  就是不允许重定向
        try:
            responseRes = huihuSession.get(routeUrl, headers = header, allow_redirects = False)
            result = responseRes.text
        except:
            continue
        start = result.find('<div class="form-control-static form-control-static-list">')
        result = result[start:]
        #print (result)
        for j in range(1,16):
            start = result.find('擦擦擦图片')
            if start==-1:
                break
            else:
                result = result[start:]
                start = result.find('src="')
                result = result[start+5:]
                end = result.find('" class="img-rounded"')
                imgpath = result[:end]
                print (imgpath)
                if imgpath=='/attachment/':
                    continue
                randomname = datetime.now().strftime("%Y%m%d_%H%M%S") + str(random.randint(1,100))+'.jpg'
                try:
                    urllib.request.urlretrieve(imgpath,'./擦擦擦/'+randomname)
                except:
                    continue
        print (i)
    print(f"isLoginStatus = {responseRes.status_code}")
        #print(f"text = {responseRes.text}")
    if responseRes.status_code != 200:
        return False
    else:
        return True
if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    login("55016", "222222")
    isLogin1 = isLoginStatus()
    print(f"is login huihu = {isLogin1}")
