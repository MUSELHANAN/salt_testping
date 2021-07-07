import os
import time

def cmd_run(filename,line,ip):

    r = os.popen(line)
    test = r.read().splitlines()
    r.close()

    f = open(filename,'a')
    for i in test:
        if '/mnt/my' in i:
            j = i.split()
            print(j)
            f.write(ip +',' + j[0] + ',' + j[1] + ',' + j[2] + ',' + j[3] + ',' + j[4] + '\n')

    f.close()

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'

    f_first = open(result_filename, 'a')
    f_first.write("设备ip,磁盘名称,磁盘总量,磁盘使用量,磁盘剩余容量,利用率\n")
    f_first.close()

    f = open('ip_list.csv', encoding='utf-8')
    test_ip = f.read().splitlines()
    for i in test_ip:
        command_tp = 'salt ' + i + " cmd.run 'df -hm'"
        print(command_tp)
        cmd_run(result_filename,command_tp, i)

    f.close()