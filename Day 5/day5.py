import numpy
import re

def buildMap():
    with open("Day 5/data5.txt",'r') as file:
        data = file.read().strip().split("\n")
    
    map = numpy.zeros((1000,1000))

    for line in data:
        coor = [int(x) for x in re.findall('[0-9]+',line)]

        #for plotting ONLY vertical and horizontal lines (for part 1)
        #if coor[0] == coor[2] or coor[1] == coor[3]:
        equ = max(abs(coor[2] - coor[0]), abs(coor[3] - coor[1]))
        x_equ = (coor[2]-coor[0])/equ
        y_equ = (coor[3]-coor[1])/equ
        for i in range(equ + 1):
            x = round(coor[0]+ i * x_equ)
            y = round(coor[1] + i * y_equ)
            map[x,y] += 1

    return map

def dayFive(map):
    count = 0
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if map[i][j] >= 2:
                count += 1
    return count

def main():
    map = buildMap()
    count = dayFive(map)
    print(count)

main()