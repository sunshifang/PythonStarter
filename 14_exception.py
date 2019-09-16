import sys

'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")


try:
    f = open('tmp/foo.txt')
    s = f.readline()
    print('读入的结果是：{0}'.format(s))
    i = int(s.strip())
except OSError as err:
    print('OS error: {}'.format(err))
except ValueError:
    print('Could not convert data to an integer.')
except:
    print('Unexcepted error:',sys.exc_info()[0])
    raise
else:
    print("else excuted")


class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self,value)
			
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)



def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is',result)
    finally:
        print('executing finally clause')

divide(2,1)
divide(2,0) #被零除
divide('2', '1')

'''


with open("tmp/foo.txt") as f:
    for line in f:
        print(line, end="")
print("再次执行f.seek(0,0)时，程序会报错，因为f已经被关闭了")
try:
    f.seek(0,0)
except:
    print("错误信息{0}，错误是：{1}".format(sys.exc_info()[0],'200'))

