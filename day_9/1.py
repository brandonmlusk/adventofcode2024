file = open("/home/blusk/Documents/adventofcode2024/day_9/input")
freeMap = []
usedMap = []
for line in file:
    line = line[:-1]
    for i in range(len(line)):
        c = line[i]
        # [index, count]
        if i % 2 == 0:
            usedMap.append([len(usedMap)//2,int(c)])
        else:
            freeMap.append([i,int(c)])
            usedMap.append([])

while (len(usedMap) - 1) > freeMap[0][0]:
    if len(usedMap[-1]) == 0:
        usedMap.pop(-1)
    diff = usedMap[-1][1] - freeMap[0][1]
    # more used space than free
    if diff > 0:
        usedMap[freeMap[0][0]].append([usedMap[-1][0],freeMap[0][1]])
        usedMap[-1][1] = diff
        freeMap.pop(0)
    # more free space than used
    elif diff < 0:
        usedMap[freeMap[0][0]].append([usedMap[-1][0], usedMap[-1][1]])
        freeMap[0][1] = abs(diff)
        usedMap.pop(-1)
    # same amount of free space as used
    else:
        usedMap[freeMap[0][0]].append([usedMap[-1][0], freeMap[0][1]])
        freeMap.pop(0)
        usedMap.pop(-1)

checksum = 0
curr = 0
for i in range(len(usedMap)):
    m = usedMap[i]
    if i % 2 == 0:
        for j in range(m[1]):
            checksum = checksum + (curr * m[0])
            curr = curr + 1
    else:
        for n in m:
            for j in range(n[1]):
                checksum = checksum + (curr * n[0])
                curr = curr + 1
print(checksum)
    


