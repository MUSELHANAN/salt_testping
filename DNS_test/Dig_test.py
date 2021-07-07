import os
import re
import csv
import time

def A_cmd_run(cmd_line):
    r = os.popen(cmd_line)
    test = r.read().splitlines()
    r.close()
    result_tmp = ''
    k = 0

    for test1 in test:
        b= re.findall('[A]\s\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', test1)
        for i in b:
            a= re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', i)
            for j in a:
                if k == 0:
                    print(j)
                    result_tmp=j
                else:
                    print(j)
                    result_tmp += ',' + j
                k += 1

    return result_tmp

def AAAA_cmd_run(cmd_line):
    r = os.popen(cmd_line)
    test = r.read().splitlines()
    r.close()
    result_tmp = ''
    k = 0

    for test1 in test:
        b= re.findall('[AAAA]\s\S{0,4}:\S{0,4}:\S{0,4}:\S*', test1)
        for i in b:
            a= re.findall('\S{0,4}:\S{0,4}:\S{0,4}:\S*', i)
            for j in a:
                if k == 0:
                    print(j)
                    result_tmp=j
                else:
                    print(j)
                    result_tmp += ',' + j
                k += 1

    return result_tmp

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M%S", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'
    f_first = open(result_filename, 'a')
    f_first.write("调度中心ip,域名,模拟DNS/用户ip,DNS所属区域,解析结果\n")

    count = 1               #循环次数

    with open("source.csv", encoding='utf-8') as file_dig_source:
        dig_source = csv.reader(file_dig_source)
        for i in dig_source:
            with open("ip_list_all.csv", encoding='gbk') as file_dig_ip:
                dig_ip = csv.reader(file_dig_ip)
                for j in dig_ip:
                    k = 0
                    while k < count:
                        if "." in i[0]:
                            dig_line = "dig @" + i[0] + " " + i[1] + ". +subnet=" + j[1]
                            print(dig_line)
                            dig_result_ip = A_cmd_run(dig_line)
                        elif ":" in i[0]:
                            dig_line = "dig @" + i[0] + " " + i[1] + ". +subnet=" + j[1] + " AAAA"
                            print(dig_line)
                            dig_result_ip = AAAA_cmd_run(dig_line)
                        else:
                            print("Error! Please check source.csv!")
                            break

                        f_first.write(i[0] + "," + i[1] + "," + j[1] + "," + j[0] + ',' + dig_result_ip + '\n')
                        k += 1

    Time_stop = time.strftime("%Y%m%d%H%M%S", time.localtime())
    f_first.close()

    print('End time: ' + Time_stop)
