import heapq
from collections import defaultdict

def part1(cave):
    rows, cols = len(cave[0]), len(cave)

    # Dijkstra's Algorithm
    pq = [(0,0,0)]
    min_risk = {(0,0):0}

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while pq:
        cur_risk, x, y = heapq.heappop(pq)

        if (x,y) == (rows -1,cols-1):
            return cur_risk
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_risk = cur_risk + cave[nx][ny]
            
                if (nx,ny) not in min_risk or new_risk < min_risk[(nx,ny)]:
                    min_risk[(nx,ny)] = new_risk
                    heapq.heappush(pq, (new_risk,nx,ny))

    return -1

def part2(cave, multi):
    rows, cols = len(cave[0]),len(cave)
    nrows, ncols = rows*multi, cols*multi

    full_map = [[0]*ncols for _ in range(nrows)]

    for i in range(nrows):
        for j in range(ncols):
            tile_inc = (i // rows) + (j // cols)
            base_risk = cave[i % rows][j % cols]
            new_risk = (base_risk + tile_inc - 1) % 9 + 1
            full_map[i][j] = new_risk

    return full_map


def main():
    with open("Day 15/data15.txt",'r') as file:
        data = file.read().strip().split("\n")

    cave = [[int(d) for d in data[i]] for i in range(len(data))]
    shortest = part1(cave) # P1 : 755, P2: 3016
    print(shortest)

    # Part 2
    full_map = part2(cave, 5)
    shortest = part1(full_map)
    print(shortest)
    

main()