from collections import defaultdict

global foundPaths
foundPaths = 0
visited = defaultdict(int)

def findPaths(nodes, cave):
    global foundPaths

    if cave == 'end':
        foundPaths += 1
        return
   
    if cave.islower():
        visited[cave] += 1

        # checking smaller caves
        small_visited = 0
        for v in visited:
            small_visited += visited[v] > 1

            if visited[v] > 2:
                visited[cave] -= 1
                return
            
        if small_visited > 1:
            visited[cave] -= 1
            return

    for next in nodes[cave]:
        if next == 'start':
            continue
        findPaths(nodes,next)

    if cave.islower():
        visited[cave] -= 1


def main():
    with open("Day 12/data12.txt",'r') as file:
        data = file.read().strip().split("\n")
        caves = [d.split("-") for d in data]

    nodes = defaultdict(list)
    for i,j in caves:
        nodes[i].append(j)
        nodes[j].append(i)
        
    findPaths(nodes, "start")

    print(foundPaths)
    
main()