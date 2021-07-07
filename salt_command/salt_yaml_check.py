import os
import time

def cmd_run(line):

    r = os.popen(line)
    test = r.read().split()
    r.close()

    if test == []:
        a = "No this file!"
    else:
        a =test[5]

    return a

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'

    f_first = open(result_filename, 'a')
    f_first.write("省份,设备ip,文件大小\n")

    f = open('ip_list.csv', encoding='utf-8')
    test_ip = f.read().splitlines()
    for i in test_ip:
        b = i.split(",")
        print(b[0], b[1])
        command_tp = 'salt ' + b[1] + ' cmd.run "cat /home/zte_node/log_exporter/*.yaml" |grep '
        result_tp = cmd_run(command_tp)
        f_first.write(b[0] + "," + b[1] + "," + result_tp + "\n")
        print(result_tp)

    f.close()
    f_first.close()