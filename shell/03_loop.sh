for loop in 1 2 3 4 5;do echo $loop;done

echo "顺序输出字符串中的字符"
a=1
for str in "This" "is" "a" "string"
do
    echo "${str}\n"
	echo $a
	a=$[a+1]
done
echo

echo "基本的while循环"
int=1
while(( $int<=5 ))
do
	echo $int
	let "int++"
done
<<!
echo "while循环用于读取键盘信息，按<Ctrl+D>结束循环"
echo "按下<Ctrl-d>退出"
echo -n "输入你最喜欢的网站名："
while read FILM
do
	echo "是的！$FILM 是一个好网站"
done
echo
!
echo "until循环"
a=0
until [ $a -gt 10 ]
do
	echo $a
	let "a++"
done
echo

echo "case多选择语句"
echo "输入1到4之间的数字："
#read aNum
aNum=2
case $aNum in
	1) echo "你输入了$aNum"
	;;
	2) echo "你输入了2"
	;;
	3) echo "你输入了3"
	;;
	4) echo "你输入了4"
	;;
	*) echo "你没有输入1-4之间的数字"
	;;
esac
echo

echo "break命令跳出循环"
<<!
while :
do
	echo -n "输入1到5之间的数字：<Ctrl-D>结束！"
	read aNum
	case $aNum in
		1|2|3|4|5) echo "你输入的数字为 $aNum!"
		;;
		*) echo "你输入的数字不是1到5之间的！游戏结束！"
			break
		;;
	esac
done
echo

echo "continue跳出当前循环"

while :
do
	echo -n "输入1到5之间的数字："
	read aNum
	case $aNum in
		1|2|3|4|5) echo "你输入的数字为 $aNum!"
		;;
		*) echo "你输入的数字不是1到5之间的！"
			continue
			echo "游戏结束！"
		;;
	esac
done
echo
!

echo "函数的定义及调用"
demoFun(){
	echo "这是我的第一个Shell函数！"
}

echo "------函数开始执行------"
demoFun
echo "------函数执行完毕------"
echo

echo "带返回值的函数"
funWithReturn(){
	echo "这个函数会对输入的两个数字进行相加运算……"
	echo "输入第一个数字：1"
	#read aNum
	aNum=1
	echo "输入第二个数字：2"
	#read anotherNum
	anotherNum=2
	echo "两个数字分别为 $aNum 和 $anotherNum !"
	let "a=aNum+anotherNum"
	#'exprt a = $aNum + $anotherNum'
	return $a
}
funWithReturn
echo "输入的两个数字之和为 $? !"
echo

echo "带参数的函数"
funWithParam(){
	echo "第一个参数为 $1 !"
	echo "第二个参数为 $2 !"
	echo "第十个参数为 $10 !"
	echo "\$10不能调用第10个参数,超过一位数字时要用\${10}的形式"
	echo "第十个参数为 ${10} !"
	echo "第十一个参数为 ${11} !"
	echo "参数的总个数为 $# !"
	echo "第一个参数为 $1 !"
	echo "作为一个字符串输出所有的参数 $* !"
	echo "第一个参数为 $1 !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
. ./test.sh