import sys
import func

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\nPython路径为：',sys.path,'\n')
print('func自定义模块的内容：',dir(func))
print('当前定义的所有名称：',dir())
