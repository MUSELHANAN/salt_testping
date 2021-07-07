# -*- coding: UTF-8 -*-
import urllib.request
import urllib.error
import csv
import ssl
import ipaddress
import socket
import datetime
import time
import multiprocessing
import subprocess

from urllib.request import urlretrieve


def Schedule(blocknum, blocksize, totalsize):
    global  speed,speed_str
    speed = (blocknum * blocksize) / (time.time() - start_time)
    speed_str = "%s" % format_size(speed)


def format_size(bytes):
    try:
        bytes = float(bytes)
        kB = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"
    if kB >= 1024:
        M = kB / 1024
        if M >= 1024:
            G = M / 1024
            return "%.3fGbps" % (G*8)
        else:
            return "%.3fMbps" % (M*8)
    else:
        return "%.3fKbps" % (kB*8)

#日志
def log(request_time,node,ip,port,result,response_time,download_speed,path):
    print (request_time,node,ip,port,result,response_time,download_speed,path,sep='|')
    csv_writer.writerow([request_time,node,ip,port,result,response_time,download_speed,path])

#HTTP请求
def request_http(ip,port,path,node):
    try:
        ip_version_judge=ipaddress.ip_address(ip)
        if ip_version_judge.version == 4:
            request_url_without_headers="http://"+ip+":"+port+path

        if ip_version_judge.version == 6:
            request_url_without_headers="http://["+ip+"]:"+port+path


        request_time=time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        time_start=datetime.datetime.now().timestamp()

        headers={'Range' : 'bytes=0-2000000','User-Agent' : 'ZTE_boce'}
        request_url=urllib.request.Request(request_url_without_headers,headers=headers)
        response=urllib.request.urlopen(request_url,timeout=5)

        time_end=datetime.datetime.now().timestamp()
        response_time=round((time_end-time_start),3)

        if download_enalbe==0:
            log(request_time,node,ip,port,str(response.status)+' '+str(response.getheader('Nginx-Cache')),response_time,'NULL',path)

        if download_enalbe==1:
            filename = 'download.data'
            urlretrieve(request_url_without_headers,filename,Schedule)
            download_speed=speed_str
            log(request_time,node,ip,port,str(response.status)+' '+str(response.getheader('Nginx-Cache')),response_time,download_speed,path)



    except urllib.error.HTTPError as e :
        log(request_time,node,ip,port,str(e.code)+str(e.reason),'NULL','NULL',path)
    except urllib.error.URLError as e:
        log(request_time,node,ip, port, e.reason,'NULL','NULL', path)
    except socket.timeout as e:
        log(request_time,node,ip,port,'Socket timeout','NULL','NULL',path)
    except :
        log(request_time,node,ip,port,'other reasons','NULL','NULL',path)

#HTTPS请求
def request_https(ip,port,path,node):
    try:
        ip_version_judge=ipaddress.ip_address(ip)
        if ip_version_judge.version == 4:
            request_url_without_headers="https://"+ip+":"+port+path

        if ip_version_judge.version == 6:
            request_url_without_headers="https://["+ip+"]:"+port+path


        request_time=time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        time_start=datetime.datetime.now().timestamp()

        headers={'Range' : 'bytes=0-2000000','User-Agent' : 'ZTE_boce'}
        request_url=urllib.request.Request(request_url_without_headers,headers=headers)
        response=urllib.request.urlopen(request_url,timeout=5,context=ssl._create_unverified_context())


        time_end=datetime.datetime.now().timestamp()
        response_time=round((time_end-time_start),3)

        if download_enalbe==0:
            log(request_time,node,ip,port,str(response.status)+' '+str(response.getheader('Nginx-Cache')),response_time,'NULL',path)

        if download_enalbe==1:
            filename = 'download.data'
            urlretrieve(request_url_without_headers,filename,Schedule)
            download_speed=speed_str
            log(request_time,node,ip,port,str(response.status)+' '+str(response.getheader('Nginx-Cache')),response_time,download_speed,path)

    except urllib.error.HTTPError as e :
        log(request_time,node,ip,port,str(e.code)+str(e.reason),'NULL','NULL',path)
    except urllib.error.URLError as e:
        log(request_time,node,ip, port, e.reason,'NULL','NULL', path)
    except socket.timeout as e:
        log(request_time,node,ip,port,'Socket timeout','NULL','NULL',path)
    except :
        log(request_time,node,ip,port,'other reasons','NULL','NULL',path)


if __name__=='__main__':
    time_start=time.time()
    print('Python start at %s'%time_start)
    global download_enalbe
    #下载测试置于1，不测试置于0
    download_enalbe=1

    #输入文件名
    file_input_ip='ip.csv'
    file_input_source='source.csv'

    #输出文件名
    time_now=time.strftime("%Y%m%d%H%M", time.localtime())
    file_output_name='check_result_'+str(time_now)+'.csv'
    file_output=open(file_output_name,'w',newline='')
    csv_writer=csv.writer(file_output)
    csv_writer.writerow(['时间','节点','IP', '端口', '拨测结果','首包响应时长（s）','下载速率','资源'])

    with open(file_input_source,encoding='utf-8') as f_source:
        with open (file_input_ip,encoding='utf-8') as f_ip:
            reader_source=csv.reader(f_source,delimiter=',')
            reader_ip=csv.reader(f_ip,delimiter=',')
            file_source=list(reader_source)
            file_ip=list(reader_ip)
            #循环次数
            count=0
            while(count < 500 ):
                for i in file_source:
                    for j in file_ip:
                        start_time = time.time()
                        if i[0] == 'http':
                            #IP，端口，资源，节点
                            request_http(j[1],i[1],i[2],j[0])
                        if i[0] =='https':
                            request_https(j[1],i[1],i[2],j[0])
                count=count+1
                #time.sleep(5)

    f_ip.close()
    f_source.close()
    file_output.close()
    time_stop=time.time()
    print('time comsuming is %s'%(time_stop-time_start))
