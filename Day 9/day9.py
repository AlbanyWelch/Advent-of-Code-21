import numpy as np

def getMap():
    with open("Day 9/data9.txt",'r') as file:
        data = file.read().strip().split("\n")
    
    map = np.zeros((100,100))
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
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

    if x > 0 < 99:
        v.append([x-1, y])
    
    if x < 99:
        v.append([x+1, y])

    if y > 0:
        v.append([x, y-1])

    if y < 99:
        v.append([x, y+1])

    return v

def part2(map):
    basins = []
    for i in range(0,8):
        points = np.argwhere(map==i)
        for p in points:
            basin = []
            size = 0
            basin.append(p)
            while len(basin) > 0:
                for b in basin:
                    adj = getAdjacents(map, b[0],b[1])
                    for a in adj:
                        if (map[p[0],p[1]])+1 == map[a[0],a[1]] and map[a[0],a[1]] != 9:
                            size += 1
                            basin.append([a[0],a[1]])
                    basin.remove(b)
            basins.append(size)

    #print(basins)


        




def main():
    map = getMap()
    #part1(map)
    part2(map)

main()