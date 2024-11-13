def part1(tm):
    data = bin(int(tm, 16))[2:].zfill(len(tm) * 4)
    
    
    ver_sum,all_packets,_ = findPackets(data)
    return ver_sum, all_packets

def findPackets(data, ind = 0):
    ver_sum = 0
    packet_info = []

    version = int(data[ind:ind+3],2)
    ver_sum += version
    ind += 3

    typeID = int(data[ind:ind+3],2)
    ind += 3

    if typeID == 4: # Literal Number
        literals = ""
        while True:
            group = data[ind:ind+5]
            ind += 5
            literals += group[1:]
            if group[0] == '0':
                break
        literals = int(literals,2)

        packet_info = [version,typeID,literals]

    else: # Operator
        lengthID = data[ind]
        ind += 1
        sub_packets = []

        if lengthID == '0':
            sub_packs = int(data[ind:ind+15],2)
            ind += 15
            subpack_end = sub_packs + ind

            while ind < subpack_end:
                sub_ver_sum, sub_packet, ind = findPackets(data, ind)
                ver_sum += sub_ver_sum
                sub_packets.append(sub_packet)
            
        elif lengthID == '1':
            bits = int(data[ind:ind+11],2)
            ind += 11

            for _ in range(bits):
                sub_ver_sum, sub_packet, ind = findPackets(data,ind)
                ver_sum += sub_ver_sum
                sub_packets.append(sub_packet)

        packet_info = [version, typeID, int(lengthID),sub_packets]
        
    return ver_sum, packet_info, ind

def part2(packets):
    result = operations(packets)
    return result


def operations(packet):
    version, typeID = packet[0],packet[1]

    if typeID == 4:
        return packet[2]
    
    sub_packets = packet[3]

    if typeID == 0:  # Sum packet
        return sum(operations(sub) for sub in sub_packets)
    elif typeID == 1:  # Product packet
        product = 1
        for sub in sub_packets:
            product *= operations(sub)
        return product
    elif typeID == 2:  # Minimum packet
        return min(operations(sub) for sub in sub_packets)
    elif typeID == 3:  # Maximum packet
        return max(operations(sub) for sub in sub_packets)
    elif typeID == 5:  # Greater than packet (2 sub-packets)
        first, second = operations(sub_packets[0]), operations(sub_packets[1])
        return 1 if first > second else 0
    elif typeID == 6:  # Less than packet (2 sub-packets)
        first, second = operations(sub_packets[0]), operations(sub_packets[1])
        return 1 if first < second else 0
    elif typeID == 7:  # Equal to packet (2 sub-packets)
        first, second = operations(sub_packets[0]), operations(sub_packets[1])
        return 1 if first == second else 0


def main():
    with open("Day 16/data16.txt",'r') as file:
        tm = file.read().strip()
    
    versions, packets = part1(tm)
    print(versions) 

    result = part2(packets)
    print(result)
    # Part 1: 1012, Part 2: 2223947372407

main()