# -*- coding: UTF-8 -*-
import os
import re
import time
import threading

def cert_check(ip):
    command_line = 'salt ' + ip + ' state.sls yzl.CDNpzcheck.sls_dir.cert_check'

    r = os.popen(command_line)
    test = r.read().splitlines()
    r.close()

    result_temp = ''
    j = 0
    for i in test:
        a = re.findall('.*?\..*?\|', i)
        if a == []:
            continue
        else:
            b = a[0].split()
            if j == 0:
                result_temp = b[0]
            else:
                result_temp += ',' + b[0]
            j += 1

    if result_temp == '':
        result_temp = '该关键字无证书记录'
    return [result_temp, j]
def cacherule_check(ip):
    command_line = 'salt ' + ip + ' state.sls yzl.CDNpzcheck.sls_dir.cacherule_check'

    r = os.popen(command_line)
    test = r.read()
    r.close()

    a = re.search('\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}', test)

    if a is not None:
        b = a.group()
    else:
        b = '该关键字无规则库记录'

    return b
def authinfo(ip):
    command_line = 'salt ' + ip + ' state.sls yzl.CDNpzcheck.sls_dir.authinfo_check'

    r = os.popen(command_line)
    test = r.read().splitlines()
    r.close()

    result_temp = ''
    j = 0
    for i in test:
        if "防盗链" in i:
            if j == 0:
                result_temp = i.split("|")[1]
            else:
                result_temp += i.split("|")[1]
            j += 1
    if result_temp == '':
        result_temp = '该关键字无防盗链记录'
    return [result_temp, j]
def whitelist(ip):
    command_line = 'salt ' + ip + ' state.sls yzl.CDNpzcheck.sls_dir.whitelist_check'

    r = os.popen(command_line)
    test = r.read()
    r.close()

    a = re.search('\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}', test)

    if a is not None:
        b = a.group()
    else:
        b = '该关键字无白名单记录'

    return b

def change_sls(origin_word, keyword):
    cmd_line = "sed -i 's/" + origin_word + "/" + keyword + "/g' sls_dir/*.sls"
    r = os.popen(cmd_line)
    r.close()
def check_sls():
    r = os.popen("cat sls_dir/*.sls")
    text = r.read()
    r.close()

    a = re.search('\%\S*?\%', text)
    if a is not None:
        b = a.group().split("%")[1]
    else:
        b = "keyword"
    return b

def salt_cp_check(domain_keyword, ip_list):

    for i in ip_list:
        list_cert.append(i + "," + domain_keyword + "," + cert_check(i)[0] + "\n")
        list_authinfo.append(i + "," + domain_keyword + "," + authinfo(i)[0] +"\n")
        list_finalresult.append(i + "," + domain_keyword + "," + str(cert_check(i)[1]) + "," + cacherule_check(i) +
                            "," + str(authinfo(i)[1]) + "," + whitelist(i) + "\n")

def judge_ipnum(list):
    if len(list) == 1:
        n = 1
    elif len(list) > 1 and len(list) <= 20:
        n = 2
    elif len(list) > 20 and len(list) <= 30:
        n = 3
    elif len(list) > 30 and len(list) <= 40:
        n = 4
    elif len(list) > 40 and len(list) <= 50:
        n = 5
    else:
        n = 10

    return n

def wirte_file(list1, list2, list3):

    result_filename = 'check_result.csv'
    cert_result_filename = 'cert_result.csv'
    authinfo_result_filename = 'authinfo_result.csv'

    f_finalresult = open(result_filename, 'a')
    for i in list1:
        f_finalresult.write(i)

    f_certresult = open(cert_result_filename, 'a')
    for j in list2:
        f_certresult.write(j)

    f_authinfo = open(authinfo_result_filename, 'a')
    for k in list3:
        f_authinfo.write(k)

    f_certresult.close()
    f_authinfo.close()
    f_finalresult.close()

if __name__ =="__main__":
    domain_keyword = input("请输入要查询的域名关键字：")
    Time_start = time.time()
    Time_now = time.strftime("%Y%m%d%H%M", time.localtime())

    f = open('ip_list.csv', encoding='utf-8')
    test_ip = f.read().splitlines()
    f.close()

    n = judge_ipnum(test_ip)
    names = globals()
    for i in range(n):
        names['iplist' + str(i)] = test_ip[i::n]

    origin_word = check_sls()
    change_sls(origin_word, domain_keyword)

    now_dir = os.getcwd()
    new_dir = now_dir + "/check_result_" + str(Time_now)
    os.mkdir(new_dir)
    os.chdir(new_dir)

    list_cert = ["设备ip,域名关键字,匹配域名\n"]
    list_authinfo = ["设备ip,域名关键字,匹配防盗链\n"]
    list_finalresult = ["设备ip,域名关键字,证书(域名数量),规则库，防盗链(数量)，域名白名单\n"]

    for j in range(n):
        names['t' + str(j)] = threading.Thread(target=salt_cp_check, args=(domain_keyword, names.get('iplist'+str(j))))

    for k in range(n):
        names['t' + str(k)].start()
    for l in range(n):
        names['t' + str(l)].join()

    wirte_file(list_finalresult, list_cert, list_authinfo)
    os.chdir(now_dir)

    Time_end = time.time()
    print('time comsuming is %s'%(Time_end-Time_start))