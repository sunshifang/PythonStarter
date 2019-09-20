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
   
print()

print("查找和替换")
phone = '2004-595-559 # 这是一个电话号码'
num = re.sub(r'#.*$','',phone)
print("phone = '2004-595-559 # 这是一个电话号码'")
print("re.sub(r'#.*$','',phone) # 通过查找和替换，删除注释")
print ("电话号码 : ", num)

print("re.sub(r'\D', '', phone)")
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
print()
'''
print("repl 参数是一个函数")
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD564'
print(re.sub('(?p<value>\d+)', double, s))
#print("s = 'A23G4HFD564'")
#print("print(re.sub('(?p<value>\d+)', double, s))")
#print(re.sub('(?p<value>\d+)', double, s))）


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
print(re.sub('(?p<value>\d+)', double, s))

'''
print("在字符串中找到正则表达式所匹配的所有子串")
pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456',0,12)
print("result1 = pattern.findall('runoob 123 google 456')",result1)
print("result2 = pattern.findall('run88oob123google456',0,12)",result2)
print()


print("re.finditer在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回")
it = re.finditer(r'\d+','12a32bc43jf3')
print("re.finditer(r'\d+','12a32bc43jf3')")
for match in it:
    print(match.group())

print()


print("re.split 方法按照能够匹配的子串将字符串分割后返回列表")




'''





'''
