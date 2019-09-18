import re
print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))
print()

print("# .* 表示任意匹配除换行符（\\n、\\r）之外的任何单个或多个字符")
line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?).*',line,re.M|re.I)

if matchObj:
    print('matchObj.group(): ', matchObj.group(0,1))
    print('matchObj.group(1): ', matchObj.group(1))
    print('matchObj.group(2): ', matchObj.group(2))
print()
    
print('re.search方法')
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

print('line = "Cats are smarter than dogs";')
print("re.search( r'(.*) are (.*?) .*', line, re.M|re.I)")
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print ("searchObj.group(1,2) : ", searchObj.group(0,1,2))
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")
