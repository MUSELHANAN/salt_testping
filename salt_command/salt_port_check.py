import os
import time

def cmd_run(line):

    r = os.popen(line)
    test = r.read().splitlines()
    r.close()

    a = "connected timeout"
    for i in test:
        if "Connected to" in i:
            a = "OK"
            break

    return a

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'

    f_first = open(result_filename, 'a')
    f_first.write("源IP,目的IP,端口,连通性\n")

    f1 = open('source_ip.csv', encoding='utf-8')
    f2 = open('detanation_ip.csv', encoding = 'utf-8')
    f3 = open('port.csv', encoding = 'utf-8')
    s_ip = f1.read().splitlines()
    d_ip = f2.read().splitlines()
    port = f3.read().splitlines()
    f1.close()
    f2.close()
    f3.close()
    for i in s_ip:
        for j in d_ip:
            for k in port:
                command_PT = 'salt ' + i + ' cmd.run "telnet ' + j + ' ' + k + '"'
                result_PT = cmd_run(command_PT)
                f_first.write(i + "," + j + "," + k + "," + result_PT + "\n")
                print(result_PT)

    f_first.close()