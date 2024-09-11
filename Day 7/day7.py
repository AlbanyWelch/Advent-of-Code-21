import re

def daySeven():
    with open("Day 7/data7.txt",'r') as file:
        data = [int(x) for x in re.findall('[0-9]+',file.read())]

    total_fuel = {}
    for a in range(min(data),max(data)):
        fuel = 0
        for d in data:
            f = abs(d - a)
            fuel += f * (f + 1) // 2 # This was changed for part 2
        total_fuel[a] = fuel

    least = min(total_fuel.values())
    key = [k for k, v in total_fuel.items() if v == least][0]
    print("Total fuel needed: ", least, " at ",key)

daySeven()


        


