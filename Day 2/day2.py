def dayTwo():
    horz = 0
    depth = 0
    aim = 0

    file = open("Day 2/data2.txt", 'r')
    for line in file:
        command = line.split()
        match (command[0]):
            case "up":
                #depth -= int(command[1]) # Part 1
                aim -= int(command[1])
            case "down":
                #depth += int(command[1]) # Part 1
                aim += int(command[1])
            case "forward":
                horz += int(command[1])
                depth += aim*int(command[1])

    file.close()

    print("Horizontal: "+str(horz)+" Depth: "+str(depth))
    print("Multi = "+ str(horz*depth))
        
dayTwo()