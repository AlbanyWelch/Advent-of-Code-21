import numpy as np

def firstFold(points,fold):
    line = int(fold[1])
    if fold[0] == 'x': # fold left
        for p in points:
            if p[0] < line:
                continue
            else:
                p[0] = line - (p[0] - line)
    else: # fold up
        for p in points:
            if p[1] < line:
                continue
            else:
                p[1] = line - (p[1] - line)

    return [list(x) for x in set(tuple(x) for x in points)]

def remainingFolds(points, folds):
    for fold in folds:
        line = int(fold[1])
        if fold[0] == 'x': # fold left
            for p in points:
                if p[0] < line:
                    continue
                else:
                    p[0] = line - (p[0] - line)
        else: # fold up
            for p in points:
                if p[1] < line:
                    continue
                else:
                    p[1] = line - (p[1] - line)
        points = [list(x) for x in set(tuple(x) for x in points)]
    return points


def main():
    with open("Day 13/data13.txt",'r') as file:
        data = file.read().strip().split("\n")
    points = [d.split(',') for d in data if ',' in d]
    folds = [d[11:len(d)].split("=") for d in data if 'fold' in d]

    points = [[int(i) for i in row] for row in points]

    points = firstFold(points,folds[0])
    print(len(points)) # 790

    points = remainingFolds(points, folds[1:])
    
    grid = ''
    for i in range(10):
        for j in range(40):
            if [j,i] in points:
                grid += '#'
            else:
                grid += '.'
        grid += '\n'
    print(grid) # PGHZBFJC


main()