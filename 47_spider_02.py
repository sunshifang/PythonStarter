
from bs4 import BeautifulSoup
import requests


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
print(s1)
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
print(postData)
'''
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
