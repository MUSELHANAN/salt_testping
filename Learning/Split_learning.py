import os

def mul_spaces_replace(file_name):      #字符串中多个空格转变为单个空格

    r = open(file_name, 'r')
    test = r.read().splitlines()
    for test1 in test:
        while test1.replace("  ", " ") != test1:
            test1 = test1.replace("  ", " ")
        for test2 in test1.split():
            print(test2)
    r.close()

def Test_split(file_name):      #split函数默认就能将多个空格作为分隔符
    r = open(file_name, 'r')
    test = r.read().splitlines()
    for test1 in test:
        test2 = test1.split()
        for test3 in test2:
            print(test3)
    r.close()

if __name__=='__main__':

    file_name = 'findall_testfile.txt'
    mul_spaces_replace(file_name)
    print('\n')
    Test_split(file_name)