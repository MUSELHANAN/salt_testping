import re
import os

f1 = open("1.txt", 'r')
text1 = f1.read().splitlines()
for i in text1:
    a = re.findall('.*?\..*?\|', i)
    if a==[]:
        pass
    else:
        b = a[0].split()
        print(b[0])
f1.close()

'''f2 = open("2.txt", "r")
text2 = f2.read()
a = re.search('\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}', text2)
print(a.group())
f2.close()'''

'''f3 = open("3.txt", 'r')
text3 = f3.read().splitlines()
for i in text3:
    if "防盗链" in i:
        print(i.split("|")[1])'''

'''f4 = open('4.txt', 'r')
text4 = f4.read()
a = re.search('\%\S*?\%', text4)
if a is not None:
    b = a.group().split('%')[1]
    print(b)'''