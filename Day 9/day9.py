import numpy as np

def getMap():
    with open("Day 9/data9.txt",'r') as file:
        data = file.read().strip().split("\n")
    
    w,h = len(data[0]),len(data)
    map = np.zeros((w,h))
    for i in range(0,h):
        for j in range(0,w):
            map[i,j] = data[i][j]

    return map

def part1(map):
    sum = 0
    # all zeros are automatically lowest points, so add 1 for each point found
    sum += len(np.argwhere(map==0))
    
    # for each number after 0, find if lowest point (number) and add to sum
    for i in range(1,9):
        found = np.argwhere(map==i)
        for f in found:
            point = map[f[0],f[1]]
            adj = getAdjacents(map,f[0],f[1])
            if point < np.min(adj):
                sum += point+1
                
    print(sum)

# changed slightly between part 1 and 2; part 1 appends map[x,y], while part 2 appends [x,y]
# for part 1 to work, change all appends to include 'map' before the coordinates
def getAdjacents(map, x, y):
    v = []

    if x > 0:
        v.append([x-1, y])
        # v.append(map[x-1,y])
    
    if x < len(map[0])-1:
        v.append([x+1, y])
        # v.append(map[x+1,y])

    if y > 0:
        v.append([x, y-1])
        # v.append(map[x,y-1])

    if y < len(map)-1:
        v.append([x, y+1])
        # v.append(map[x,y+1])

    return v

def part2(map):
    basins = []
    for i in range(0,5):
        points = np.argwhere(map==i)
        print(points)
        for p in points:
            basin = []
            neighbours = [p]

            while neighbours:
                current = neighbours.pop()
                basin.append(current)

                adj = getAdjacents(map, current[0],current[1])
                for a in adj:
                    if map[a[0],a[1]] == 9 or map[a[0],a[1]] == -1:
                        continue
                    elif map[a[0],a[1]] > map[current[0],current[1]]:
                        neighbours.append(a)
                map[current[0],current[1]] = -1   
            basins.append(len(basin))

    basins.sort(reverse=True)
    #print(basins[0:10]) # to see the first 10 basins
    print(basins[0]*basins[1]*basins[2])

    # 902880 (99,96,95) - my answer


def main():
    map = getMap()
    #part1(map)
    part2(map)

main()