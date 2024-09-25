from collections import defaultdict

def part1(poly,rules):
    for _ in range(40):
        new_poly = ""
        for p in range(len(poly)-1):
            pair = poly[p:p+2]
            new_poly += pair[0]
            if pair in rules:
                new_poly += rules[pair]
        new_poly += pair[1]
        poly = new_poly

    c = {}
    for p in poly:
        if p not in c:
            c[p] += 1

    print(max(c.values()) - min(c.values()))

def part2(poly,rules):
    ply = defaultdict(int)

    for p in range(len(poly)-1):
        ply[poly[p:p+2]] += 1

    for _ in range(40):
        new_ply = defaultdict(int)
        for pair,num in ply.items():
            new_ply[pair[0]+rules[pair]] += num
            new_ply[rules[pair]+pair[1]] += num
        ply = new_ply

    c = defaultdict(int)
    for p in ply:
        for l in p:
            c[l] += ply[p]

    c = {k: (v + 1) // 2 for k, v in c.items()}
    print((max(c.values()) - min(c.values()))-1)

def main():
    with open("Day 14/data14.txt",'r') as file:
        data = file.read().strip().split("\n")
    poly = data[0]
    rules = [d.split(' -> ') for d in data if '->' in d]
    rules = {rule[0]:rule[1] for rule in rules}

    #part1(poly,rules)
    part2(poly,rules)

# Part 1: 3095
# Part 2: 3152788426517

main()