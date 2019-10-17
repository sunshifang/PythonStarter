a=10
b=20
if [ $a == $b ] ; then
	echo "a 等于 b"
elif test $a -gt $b; then
	echo "a 大于 b"
elif test $a -lt $b
then
	echo "a 小于 b"
else
	echo "没有符合的条件"
fi
printf "计算表达式\n"
<<!
num1=$[2*3]
num2=$[1+5]
!
num1=$[2*3]
num2=`expr 1 + 5`
if test $num1 -eq $num2
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi