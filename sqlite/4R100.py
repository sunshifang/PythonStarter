print('='*50)
print('   4R100故障排除系统V20.01')
print('='*50)
print('1:===不送气====')
print('2:===不送丝====')
print('3:===高速送丝==')
print('4:===送丝不稳==')
print('5:===退出系统==')
print('$'*50)
while True:
    code=int(input('请输入故障代码:'))
    print('')
    if code==1:
        DC_solenoid=int(input('==请输入电磁阀552A与553A电压值，40V或4V=='))
        print('')
        if DC_solenoid==40:
            print('==测量电磁阀阻值：18欧左右==')
        elif DC_solenoid==4:
            print('==电磁阀堵塞==')
        else:
            print('==检测送丝板3J83,4J83供电：40V有否==')
        print('='*50)
    elif code==2:
        DC_motor=input('请输入电机碳刷电极间电压有或无：')
        print('')
        if DC_motor=='有':
            print('==检查碳刷及支架接触良好否：电机阻值1-3欧==')
        else:
            print('==检查送丝板1J83与2J83线路电压及送丝板供电==')
        print('='*50)
    elif code==3:
        H_motor=int(input('启动送丝，测537,534电压正常值2.1V；高速时5V，请写5或0；'))
        if H_motor==5:
            print('==磁芯松动或脱落==')
        else:
            print('更换转速板')
        print('='*50)
    elif code==4:
        M_motor=input('启动送丝，测537与534电压值是2.1V,电压波动填写大或否；')
        if M_motor=='是':
            print('==电机转速磁芯与电机轴松动==')
        else:
            print('==先检查送丝轮磨损情况及挡片位置，检查531,534,535,537及转速板；')
        print('='*50)
    elif code==5:
        break
    else:
        print('你输入代码有无，请重新输入；')
