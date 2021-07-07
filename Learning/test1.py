def nametest():
    names = globals()
    iplist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    n = 5
    for i in range(5):
        print(i)
        names['iplist' + str(i)] = iplist[i::n]

    print(iplist0)

nametest()


'''def a():
    for i in range(3):
        globals()['part' + str(i)] = i
    print(part0)
    print(part1)
    print(part2)
a()
print(part0)'''