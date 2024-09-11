def getData():
    data = []
    code = open("Day 3/data3.txt",'r')
    for c in code:
        data.append(c.strip("\n"))
    code.close()
    return data

def dayThree_P1(data):
    gamma = ""
    epsilon = ""
    count = 0
    for i in range(0,12): # 12 bits
        for d in data:
            if d[i] == "1":
                count += 1

        if count > (len(data)/2): # if 1 is majority
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
        count = 0
    
    print("Gamma Rate: "+str(int(gamma,2))+" Epsilon Rate: "+str(int(epsilon,2))+"\n")
    print("Power: "+str(int(gamma,2)*int(epsilon,2))+"\n")

def dayThree_P2(data):

    length = len(data[0])
    data = [int(i,2) for i in data]

    # Oxygen Rate
    o2_data = data.copy()
    pos = length - 1
    while pos >= 0 and len(o2_data) > 1:
    # Find the most common bit
        one = sum([((x & (1 << pos)) >> pos) for x in o2_data])
        zero = len(o2_data) - one

        if zero > one:
            o2_data = list(filter(lambda x: not (x & (1 << pos)), o2_data))
        else:
            o2_data = list(filter(lambda x: (x & (1 << pos)), o2_data))

        pos -= 1

    # CO2 Rate
    co2_data = data.copy()
    pos = length - 1
    while pos >= 0 and len(co2_data) > 1:
    # Find the most common bit
        one = sum([((x & (1 << pos)) >> pos) for x in co2_data])
        zero = len(co2_data) - one

        if zero > one:
            co2_data = list(filter(lambda x: (x & (1 << pos)), co2_data))
        else:
           co2_data = list(filter(lambda x: not (x & (1 << pos)), co2_data))

        pos -= 1

    print("Oxygen: "+str(o2_data[0])+" CO2: "+str(co2_data[0]))
    print("Life Support: "+str(o2_data[0]*co2_data[0]))
    

def main():
    data = getData()
    dayThree_P1(data)
    dayThree_P2(data)

main()
