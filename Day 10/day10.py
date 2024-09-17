import statistics

legalOpen = ["(","[", "{","<"]
legalClose = [")","]","}",">"]

def getData():
    with open("Day 10/data10.txt",'r') as file:
        data = file.read().strip().split("\n")
    return data

def part1():
    subsys = getData()
    errors = {")":0,"]":0,"}":0,">":0}

    # for part 2
    incomplete = subsys.copy()

    for s in subsys:
        order = []
        for each in s:
            if each in legalOpen:
                order.append(each)
            if each in legalClose:
                end = order.pop()
                if legalOpen.index(end) != legalClose.index(each):
                    errors[each] += 1
                    incomplete.remove(s)
                    continue
                
    print((errors[")"]*3)+(errors["]"]*57)+(errors["}"]*1197)+(errors[">"]*25137))

    return incomplete # returns list of incomplete lines for part 2

def part2(incomplete):
    score = []
    for i in incomplete:
        order = []
        for each in i:
            if each in legalOpen:
                order.append(each)
            if each in legalClose:
                order.pop()
        
        s = 0
        for o in reversed(order):
            s *= 5
            match(o):
                case "(":
                    s += 1
                case "[":
                    s += 2
                case "{":
                    s += 3
                case "<":
                    s += 4
        score.append(s)
    
    score.sort()
    print(statistics.median(score))

def main():
    incomp = part1()
    part2(incomp)

main()
    