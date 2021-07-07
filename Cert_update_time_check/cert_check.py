import os
import time

def cmd_run(line):

    r = os.popen(line)
    test = r.read().splitlines()
    r.close()

    a = "No certificate!"
    b = ""

    for line in test:
        if "< HTTP/" in line:
            b = line.split()[2]
            print(b)
            break
    if b == '200':
        for line in test:
            if "expire date" in line:
                a = line.split('e:')[1]
                break
            else:
                a = "No results!"

    return [a, b]

if __name__=='__main__':
    Time_start = time.strftime("%Y%m%d%H%M", time.localtime())

    result_filename = 'check_result_' + str(Time_start) + '.csv'

    f_first = open(result_filename, 'a')
    f_first.write("设备ip,域名,状态码,证书更新时间\n")


    f = open('ip_list.csv', encoding='utf-8')
    test_ip = f.read().splitlines()
    f.close()

    f2 = open('url_list.csv', encoding='utf-8')
    url = f2.read().splitlines()[0]
    domain = url.split('/')[2]
    f2.close()
    #print(domain)
    #print(url)

    for i in test_ip:
        command_cc = 'salt ' + i + ' cmd.run "curl --resolve \'' + domain + ':443:127.0.0.1\' -Iv /dev/null \'' + url + '\'"'
        print(command_cc)
        result_cc = cmd_run(command_cc)
        f_first.write(i + "," + domain + "," + result_cc[1] + "," + result_cc[0] + "\n")
        print(result_cc)

    f_first.close()