import re

def part1():
    with open("Day 8/data8.txt",'r') as file:
        data = file.read().strip().split("\n")
    outputs = [(d[(d.find("|")) + 1:]).split() for d in data]

    lengths = [2,3,4,7]
    digits = 0
    for out in outputs:
        for o in out:
            if len(o) in lengths:
                digits += 1
            
    print(digits)

def part2():
    with open("Day 8/data8.txt",'r') as file:
        data = file.read().strip().split("\n")
    outputs = [(d[(d.find("|")) + 1:]).split() for d in data]
    inputs = [(d[:d.find("|")]).split() for d in data]

    total = 0

    for input in inputs:
        code = decode(input)
        out = ""
        for o in outputs[inputs.index(input)]:
            o = ''.join(sorted(o))
            for c in code:
                if code[c] == o:
                    out += str(list(code).index(c))
        total += int(out)

    print(total)

def decode(input):
    decode = {}

    for i in input:
        i = ''.join(sorted(i))
        if len(i) == 2:
            decode[1] = i
        elif len(i) == 3:
            decode[7] = i
        elif len(i) == 4:
            decode[4] = i
        elif len(i) == 7:
            decode[8] = i

    for i in input:
        if i not in decode:
            i = ''.join(sorted(i))
            length = len(i)
            if length == 5: # values 2, 3 or 5
                if len(set(i).intersection(decode[7])) == 3:
                    decode[3] = i
                elif len(set(i).intersection(decode[4])) == 2:
                    decode[2] = i
                else:
                    decode[5] = i

            if length == 6: # values 0, 6, 9
                if len(set(i).intersection(decode[7])) == 2:
                    decode[6] = i
                elif len(set(i).intersection(decode[4])) == 4:
                    decode[9] = i
                else:
                    decode[0] = i

    return {key: decode[key] for key in sorted(decode)}
    
def main():
    part1()
    part2()

main()