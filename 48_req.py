import requests
if __name__ == "__main__":

    #登录请求的url（通过抓包工具获取）
    #post_url = 'http://192.168.2.107/otcwms/Page/WMS/CConsumingOutStockBill/CConsumingOutStockBillList.aspx?itemNo=c032503&pTypeNo=main'
    post_url = 'http://192.168.2.107/otcwms/Login.aspx'
    #创建一个session对象，该对象会自动将请求中的cookie进行存储和携带
    session = requests.session()
    print("session = ",session)
    #伪装UA
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    formdata = {
        'txtUsername': '55016',
        'txtPass': '222222',
        'textBox1': '7948'
    }
    #使用session发送请求，目的是为了将session保存该次请求中的cookie
    session.post(url=post_url,data=formdata,headers=headers)

    get_url = 'http://192.168.2.107/otcwms/Page/WMS/CConsumingOutStockBill/CConsumingOutStockBillList.aspx?itemNo=c032503&pTypeNo=main'
    #再次使用session进行请求的发送，该次请求中已经携带了cookie
    response = session.get(url=get_url,headers=headers)
    #设置响应内容的编码格式
    response.encoding = 'utf-8'
    #将响应内容写入文件
    with open('./renren.html','w') as fp:
        fp.write(response.text)
