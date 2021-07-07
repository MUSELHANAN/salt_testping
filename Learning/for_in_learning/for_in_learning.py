# -*- coding: utf-8 -*-
import csv

'''list1 = ['1','2']
list2 = ['a','b']

for i in list1:
    for j in list2:
        print(str(i)+','+j)'''


with open("1.csv", encoding='utf-8') as f1:
    with open("2.csv", encoding='utf-8') as f2:
        text1 = csv.reader(f1)
        text2 = csv.reader(f2)
        for i in text1:
            index = 0
            for index, j in enumerate(text2):
                print(i + j)



'''with open("1.csv", encoding='utf-8') as f1:
    text1 = csv.reader(f1)
    for i in text1:
        with open("2.csv", encoding='utf-8') as f2:
            text2 = csv.reader(f2)
            for j in text2:
                print(i + j)'''