import re
from collections import Counter, defaultdict

def mainLoop_p1():
    time = 0
    with open("Day 6/data6.txt",'r') as file:
        fish = [int(x) for x in re.findall('[0-9]+',file.read())]

    while time < 256:
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
        time += 1
        print(time)

    print("Time: ",time," Fish: ",len(fish))

def mainLoop_p2():
    days = 256

    with open("Day 6/data6.txt",'r') as file:
        initial = [int(x) for x in re.findall('[0-9]+',file.read())]

    fish = Counter(initial)

    for _ in range(days):
        new_fish = defaultdict(int)
        for f in fish:
            if f == 0:
                new_fish[6] += fish[0]
                new_fish[8] += fish[0]
            else:
                new_fish[f-1] += fish[f]

        fish = new_fish

    print("Fish: ",sum(fish.values()))

#mainLoop_p1() # for part 1
mainLoop_p2() # for part 2

    
