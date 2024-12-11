from enum import Enum

class Space(Enum):
    FREE = 1
    USED = 2
class Block(object):
    id = -1
    sz = 0
    occupied = Space.FREE

def swap(u,f):
    f.id = u.id
    u.id = -1
    f.occupied = Space.USED
    u.occupied = Space.FREE
def split(u,f):
    # free block is bigger than used
    diff = f.sz - u.sz
    f.occupied = Space.USED
    u.occupied = Space.FREE
    f.sz = u.sz
    f.id = u.id
    u.id = -1
    s = Block()
    s.sz = diff
    return s

def printMap(usedMap):
    for b in range(len(usedMap)):
        block = usedMap[b]
        for s in range(block.sz):
            if block.id == -1:
                print(".", end="")
            else:
                print(block.id, end="")
    print()


file = open("/home/blusk/Documents/adventofcode2024/day_9/input")
freeMap = []
usedMap = []
for line in file:
    line = line[:-1]
    for i in range(len(line)):
        c = line[i]
        # [index, count]
        if i % 2 == 0:
            b = Block()
            b.id = len(usedMap)//2
            b.sz = int(c)
            b.occupied = Space.USED
            usedMap.append(b)
        else:
            b = Block()
            b.sz = int(c)
            usedMap.append(b)
            

for i in range(len(usedMap)-1,-1,-1):
    u = usedMap[i]
    if u.occupied == Space.FREE:
        continue
    for j in range(len(usedMap)):
        f = usedMap[j]
        if f.occupied == Space.USED or f.sz < u.sz or i < j:
            continue
        elif f.sz == u.sz:
            swap(u,f)
            break
        else:
            usedMap.insert(j+1,split(u,f))
            break

index = 0
checksum = 0
for b in range(len(usedMap)):
    block = usedMap[b]
    for s in range(block.sz):
        if block.id != -1:
            checksum = checksum + (index * block.id)
        index = index + 1
print(checksum)
    


