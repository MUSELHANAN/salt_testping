import os
import time

def cmd_run(filename, line):

    r = os.popen(line)
    test = r.read().splitlines()
    r.close()

    f = open(filename, 'a')

    for i in test:
        i = i.split("_")
        result = ""
        k=0
        for j in i:
            if k == 0:
                result = j
            else:
                result = result + "," + j
            k+=1

        f.write(result + "\n")

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
        command_tp = 'salt ' + i + ' cmd.run "ls /home/mr/zycdnupload/zy_sort_log/cdn/80000003 |grep 20210426 "'
        cmd_run(result_filename, command_tp)

    f.close()