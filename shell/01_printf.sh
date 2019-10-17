printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876
printf "\n\n"

printf "单引号与双引号效果一样\n"
printf '%d %s\n' 1 "abc"
printf "没有引号也可以输出\n"
printf %s abcdef
printf "格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string被重用"
printf "%s\n" abc abcdef 
printf "%s\n" abc def
printf "%s %s %s\n" a b c d e f g h i j
printf "如果没有arguments，那么%s用NULL代替，%d用0代替\n"
printf "windows下，\%s用空格代替\n"
printf "%s and %d \n"
printf "\n"

printf "转义字符\n"
printf "1.转义符只在格式符中有效，参数中的转义符无效\n"
printf "a string, no processing:<%s>\n" "A\nB"
printf "2.只在%b格式指示符控制下的参数字符串中有效"
printf "a string, no processing:<%b>\n" "A\nB"
printf "3.\a不换行"
printf "www.runoob.com \a"
