import os
import time

def cmd_run(line):

    r = os.popen(line)
    test = r.read().splitlines()
    r.close()

    if test[1]=="    True":
         a = "True"
    else:
         a = "fail"

    return a

def writeFile(filename, ip, result):
    f = open(filename, "a")
    f.write(ip + "," + result + "\n")
    f.close()

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'

    f_first = open(result_filename, 'a')
    f_first.write("设备ip,tp结果\n")
    f_first.close()

    f = open('ip_list.csv', encoding='utf-8')
    test_ip = f.read().splitlines()
    for i in test_ip:
        command_tp = 'salt ' + i + ' test.ping'
        result_tp = cmd_run(command_tp)
        writeFile(result_filename, i, result_tp)
        print(result_tp)

    f.close()