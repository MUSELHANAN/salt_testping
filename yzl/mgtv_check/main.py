import node_info
import os
import re


def cache_rule_verfy(ip, correct_cacherule, cacherule):
    missiing_part = [item for item in correct_cacherule if item not in cacherule]
    extra_part = [item for item in cacherule if item not in correct_cacherule]
    if len(missiing_part) == 0 and len(extra_part) == 0:
        print(ip + "缓存规则库核查正确")
    elif len(missiing_part) != 0:
        print(ip + "缓存规则库缺少的部分为：" + ",".join(missiing_part))
    elif len(extra_part) != 0:
        print(ip + "缓存规则库多出的部分为：" + ",".join(extra_part))


def auth_verify(ip, correct_auth, auth):
    missiing_part = [item for item in correct_auth if item not in auth]
    extra_part = [item for item in auth if item not in correct_auth]
    if len(missiing_part) == 0 and len(extra_part) == 0:
        print(ip + "防盗链核查正确")
    elif len(missiing_part) != 0:
        print(ip + "防盗链缺少的部分为：" + ",".join(missiing_part))
    elif len(extra_part) != 0:
        print(ip + "防盗链多出的部分为：" + ",".join(extra_part))


def certi_verify(ip, correct_certi, certi):
    missiing_part = [item for item in correct_certi if item not in certi]
    extra_part = [item for item in certi if item not in correct_certi]
    if len(missiing_part) == 0 and len(extra_part) == 0:
        print(ip + "证书核查正确")
    elif len(missiing_part) != 0:
        print(ip + "证书缺少的部分为：" + ",".join(missiing_part))
    elif len(extra_part) != 0:
        print(ip + "证书多出的部分为：" + ",".join(extra_part))


if __name__ == '__main__':
    cache_rule_lists = ['disp.titan.mgtv.com', 'pcdowncmnet.titan.mgtv.com', 'pcdowncmnetzte.titan.mgtv.com',
                        'pcvideocmnet.titan.mgtv.com', 'pcvideocmnetzte.titan.mgtv.com',
                        'pcvideocmnetzte-v6.titan.mgtv.com']
    # MGTV-SNS
    auth_lists = ['1000000601', '1000000602']
    # MGTV-CCS
    #auth_lists = ['1000000607', '1000000606', '1000000605', '1000000604', '1000000603']
    certi_lists = ['disp.titan.mgtv.com', 'pcdowncmnet.titan.mgtv.com', 'pcdowncmnetzte.titan.mgtv.com',
                   'pcvideocmnet.titan.mgtv.com', 'pcvideocmnetzte.titan.mgtv.com',
                   'pcvideocmnetzte-v6.titan.mgtv.com']

    vips = input("请输入节点VIP（如多个节点，请以空格分隔）：").split(" ")
    while '' in vips:
        vips.remove('')

    for vip in vips:
        ip_lists = node_info.ip_lists(vip)
        ip_lists.sort()
        print("节点VIP：{0}\n节点设备数：{1}\n节点设备列表：{2}".format(vip, len(ip_lists), "|".join(ip_lists)))
        for ip in ip_lists:
            cache_rule = re.split("[ \n]", os.popen("sh cacherule_check.sh " + ip).read())
            cache_rule.remove("")
            certi = re.split("[ \n]", os.popen("sh certi_check.sh " + ip).read())
            certi.remove("")
            auth = re.split("[ \n]", os.popen("sh auth_check.sh " + ip).read())
            auth.remove("")

            cache_rule_verfy(ip, cache_rule_lists, cache_rule)
            certi_verify(ip, certi_lists, certi)
            auth_verify(ip, auth_lists, auth)
