echo "echo 相当于print，用于显示信息"

echo "for循环要有done结尾"
for skill in `ls`; do
    echo "I am good at ${skill} Script"
done
echo ""

echo "变量被删除后不能再次使用，使用时无错误提示无输出内容"
myUrl="http://www.baidu.com"
echo $myUrl
unset myUrl
echo $myUrl
echo ""

echo "使用readonly命令可以将变量定义为只读变量，只读变量的值不能被改变"
myUrl="http://www.baidu.com"
#readonly myUrl
unset myUrl
echo myUrl
myUrl="http://www.google.com"
echo "获取字符串长度"
str="abcd"
echo "字符串abcd的长度是："${#str}
echo ""

echo "提取子字符串"
str="runoob is a great site"
echo 'str="'${str}'"'
echo '执行${str:1:4}的结果是'${str:1:4}
ehoe ""

echo "向脚本传递参数"
echo "第一个参数为：$1"
echo "参数的个数为：$#"
echo "传递的参数作为一个字符串显示：$*"
echo "传递的参数作为多个字符串显示：$@"

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
echo 

echo "表达式运算"
a=10
b=20
 val=`expr $a + $b`
 echo "a + b : $val"
 
 val=`expr $a - $b`
 echo "a-b:$val"
 
 val=`expr $a \* $b`
 echo "a*b:$val"
 
 val=`expr $b / $a`
 echo "a/b:$val"
 
 val=`expr $b % $a`
 echo "b%a:$val"
 
if [ $a == $b ]
then
   echo "a 等于 b"
fi

if [ $a != $b ]
then
   echo "a 不等于 b"
fi
echo

echo "关系运算符"
if [ $a -eq $b ]
then
	echo "$a -eq $b : a 等于 b"
else
	echo "$a -eq $b : a 不等于 b"
fi

if [ $a -ne $b ]
then
	echo "$a -ne $b : a 不等于 b"
else
	echo "$a -ne $b : a 等于 b"
fi

if [ $a -ge $b ]
then
	echo "$a -ge $b : a 大于等于 b"
else
	echo "$a -ge $b : a 小于 b"
fi

if [ $a -le $b ]
then
	echo "$a -le $b : a 小于等于 b"
else
	echo "$a -le $b : a 大于 b"
fi
echo

echo "布尔运算a=10 b=20"
if [ $a != $b ]
then
	echo "$a != $b : a 不等于 b"
else
	echo "$a != $b : a 等于 b"
fi

if [ $a -lt 100 -a $b -gt 15 ]
then
	echo "$a 小于 100 且 $b 大于 15 ：返回 true"
else
	echo "$a 小于 100 且 $b 大于 15 ：返回 false"
fi

if [ $a -lt 100 -o $b -gt 100 ]
then
	echo "$a 小于 100 或 $b 大于 100 : 返回 true"
else
	echo "$a 小于 100 或 $b 大于 100 : 返回 false"
fi

if [ $a -lt 5 -o $b -gt 100 ]
then
	echo "$a 小于 5 或 $b 大于 100：返回 true"
else
	echo "$a 小于 5 或 $b 大于 100：返回 false"
fi
echo

echo "逻辑运算"
if [[ $a -lt 100 && $b -gt 100 ]]
then
	echo "返回 True"
else
	echo "返回false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
	echo "返回 true"
else
	echo "返回 false"
fi
echo

echo "字符串运算"
a="abc"
b="efg"

if [ $a = $b ]
then
	echo "$a = $b : a 等于 b"
else
	echo "$a = $b : a 不等于 b"
fi

if [ $a != $b ]
then
	echo "$a != $b : a 不等于 b"
else
	echo "$a != $b : a 等于 b"
fi

if [ -z $a ] 
then
	echo "-z $a : 字符串长度为0"
else
	echo "-z $a : 字符串长度不为0"
fi

if [ -n "$a" ] 
then
	echo "-n $a : 字符串长度不为0"
else
	echo "-n $a : 字符串长度为0"
fi

if [ $a ] 
then
	echo "$a : 字符串不为空"
else
	echo "$a : 字符串为空"
fi
echo

echo "文件检测"
file="./test1.sh"
if [ -r $file ]
then
	echo "文件可读"
else
	echo "文件不可读"
fi

if [ -w $file ]
then
	echo "文件可写"
else
	echo "文件不可写"
fi

if [ -x $file ]
then
	echo "文件可执行"
else
	echo "文件不可执行"
fi

if [ -f $file ]
then
   echo "文件为普通文件"
else
   echo "文件为特殊文件"
fi

if [ -d $file ]
then
   echo "文件是个目录"
else
   echo "文件不是个目录"
fi

if [ -d $file ]
then
   echo "文件为空"
else
   echo "文件不为空"
fi

if [ -e $file ]
then
   echo "文件存在"
else
   echo "文件不存在"
fi
echo

echo "echo命令--输出字符串"
echo "It is a test"
echo 'It is s test'
echo It is a test
echo "转义符\\显示特殊字符，如单引号\'"
echo \'It is a test\'
echo

echo "显示变量：请输入您要显示的变量："
#read name
name=123
echo "您输入的内容是：$name"
echo

echo "显示换行"
echo -e "OK\n"
echo "It is a test"
echo -e "it is test\nok"
echo "\n"

echo "显示不换行"
echo -e "ok!! \c"
echo "it is a test"
echo 

echo "显示结果定向至文件"
echo "It is a test!!!">myfile
cat myfile
echo

echo "单引号原样输出字符串"
echo "name=$name"
echo 'name=$name'
echo

echo "显示命令执行结果"
echo "\`date=\`"`date`
echo "\`date=\``date`"



