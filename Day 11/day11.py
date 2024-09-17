def setupOcto():
    with open("Day 11/data11.txt",'r') as file:
        data = file.read().strip().split("\n")

    allOcto = []
    for line in data:
        o = []
        for octo in line:
            o.append(int(octo))
        allOcto.append(o)

    return allOcto

flashes = 0

def flash(allOcto,x,y):
    global flashes
    flashes += 1
    adjacent = [(r, c) for r in range(x-1, x+2) for c in range(y-1, y+2) if (r != x or c != y) and 0 <= r < len(allOcto) and 0 <= c < len(allOcto[0])]
    for a in adjacent:
        allOcto[a[1]][a[0]] += 1
        if allOcto[a[1]][a[0]] == 10:
            flash(allOcto,a[0],a[1])
            allOcto[a[1]][a[0]] += 1

def simulation(allOcto):
    steps = [] # for part 2
    for i in range(250): # was changed from 100 to 250 for part 2
        prev_flashes = flashes # for part 2
        for y in range(len(allOcto)):
            for x in range(len(allOcto[0])):
                allOcto[y][x] += 1
                if allOcto[y][x] == 10: # flashes
                    flash(allOcto,x,y)
                    allOcto[y][x] += 1

        for y in range(len(allOcto)):
            for x in range(len(allOcto[0])):
                if allOcto[y][x] > 9:
                    allOcto[y][x] = 0

        # PART 2 #
        if (flashes - prev_flashes) == 100:
            steps.append(i+1)
        
    print(flashes) # 1719
    if len(steps) > 0:
        print("First Sync Flash: ", steps[0]) # 232

def main():
    all = setupOcto()
    simulation(all)

main()