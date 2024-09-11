def dayOne_P1():
    inc = 0

    prv = 0
    cur = 0

    lines = open("Day 1/data1.txt", 'r')
    for l in lines:
        cur = int(l)
        if prv != 0:
            if cur > prv:
                print(str(cur) + "(Increased)")
                inc += 1
            else:
                print(str(cur) + "(Decreased)")
        else:
            print(str(cur) + "N/A - Not pervious measurement")
        prv = cur

    lines.close()
    print(inc)

def dayOne_P2():
    inc = 0
    data = []
    prvSum = 0
    curSum = 0

    lines = open("Day 1/data1.txt", 'r')
    for l in lines:
        data.append(int(l))
    lines.close()

    for i in range(0, len(data)-2):
        curSum = data[i] + data[i+1] + data[i+2]
        if prvSum == 0:
            print(str(curSum)+" No previous sum")
        else:
            if curSum > prvSum:
                inc += 1
                print(str(curSum)+" - Increased")
            else:
                print(str(curSum)+" - Decreased/No Change")
        prvSum = curSum
            
    print(inc)

#dayOne_P1()
dayOne_P2()
