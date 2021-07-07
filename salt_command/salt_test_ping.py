import os
import time
import threading

def salt_testping(iplist):
    for i in iplist:
        command_tp = 'salt ' + i + ' test.ping'
        r = os.popen(command_tp)
        test = r.read().splitlines()

        if len(test) == 2:
            if test[1] == "    True":
                a="True"
            else:
                a="Connetcted fail!"
        else:
            a="Device is not exist!"

        r.close()

        result_list.append(str(i) + "," + a + "\n")
        print(str(i) + "," + a + "\n")

def judge_ipnum(list):
    if len(list) == 1:
        n = 1
    elif len(list) == 2:
        n = 2
    elif len(list) == 3:
        n = 3
    elif len(list) == 4:
        n = 4
    else:
        n = 5

    return n

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'

    result_list=["设备ip,tp结果\n"]

    f = open('ip_list.csv', encoding='utf-8')
    test_ip = f.read().splitlines()

    n = judge_ipnum(test_ip)
    names = globals()
    for i in range(n):
        names['iplist' + str(i)] = test_ip[i::n]

    for j in range(n):
        names['t' + str(j)] = threading.Thread(target=salt_testping, args=(names.get('iplist' + str(j))))

    for k in range(n):
        names['t' + str(k)].start()
    for l in range(n):
        names['t' + str(l)].join()

    f_result = open(result_filename, 'a')
    for result_line in result_list:
        f_result.write(result_line)

    f.close()
    f_result.close()