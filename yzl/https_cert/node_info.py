import yaml


def ip_lists(vip):
    with open('vip.yaml', encoding='utf-8') as vip_data:
        data = yaml.safe_load(vip_data)
        try:
            return ([k for k, v in data.items() if vip in "".join(v)])
        except:
            pass


if __name__ == '__main__':
    vip = input("请输入节点VIP：")
    ip_lists = ip_lists(vip)
    ip_lists.sort()
    print("节点VIP：{0}\n节点设备数：{1}\n节点设备列表：{2}".format(vip, len(ip_lists), "|".join(ip_lists)))
