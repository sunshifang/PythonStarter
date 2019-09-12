import sys
import func

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\nPython路径为：',sys.path,'\n')
print('func自定义模块的内容：',dir(func))
print('当前定义的所有名称：',dir())
print('主提示符：',sys.ps1)
print('副提示符：',sys.ps2)
