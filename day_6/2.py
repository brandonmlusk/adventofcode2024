from enum import Enum
class Dir(Enum):
    FORWARD = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4

def isObstruct(x,y,arr,dir):
    match dir:
        case Dir.FORWARD:
            return (x - 1 > -1 and arr[x-1][y] == "#")
        case Dir.BACKWARD:
            return (x + 1 < len(arr) and arr[x+1][y] == "#")
        case Dir.RIGHT:
            return (y + 1 < len(arr[x]) and arr[x][y+1] == "#")
        case Dir.LEFT:
            return (y - 1 > -1 and arr[x][y-1] == "#")

def incCount(x,y,arr,totalCount):
    if arr[x][y] != "X":
        arr[x][y] = "X"
        return totalCount + 1
    return totalCount
    
def runSim(inputArr,x,y,startDir):
    currentDir = startDir
    totalCount = 0
    arr = inputArr.copy()
    visited = set()
    while x > -1 and x < len(arr) and y > -1 and y < len(arr[x]):
        if (x,y,currentDir) in visited:
            return True
        elif currentDir == Dir.FORWARD and isObstruct(x,y,arr,currentDir):
            currentDir = Dir.RIGHT
        elif currentDir == Dir.FORWARD:
            visited.add((x,y,currentDir))
            arr[x][y] = "X"
            x = x - 1
        elif currentDir == Dir.RIGHT and isObstruct(x,y,arr,currentDir):
            currentDir = currentDir.BACKWARD
        elif currentDir == Dir.RIGHT:
            visited.add((x,y,currentDir))
            arr[x][y] = "X"
            y = y + 1
        elif currentDir == Dir.BACKWARD and isObstruct(x,y,arr,currentDir):
            currentDir = Dir.LEFT
        elif currentDir == Dir.BACKWARD:
            visited.add((x,y,currentDir))
            arr[x][y] = "X"
            x = x + 1
        elif currentDir == Dir.LEFT and isObstruct(x,y,arr,currentDir):
            currentDir = Dir.FORWARD
        else:
            visited.add((x,y,currentDir))
            arr[x][y] = "X"
            y = y - 1
    return False

file = open("/home/blusk/Documents/adventofcode2024/day_6/input")
arr = []
x,y = 0,0
totalCycles = 0
for line in file:
    line = line[:-1]
    arr.append(list(line))
    if line.count("^"):
        x = len(arr) - 1 if len(arr) - 1 > 0 else 0
        y = line.index("^")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        prev = arr[i][j]
        arr[i][j] = "#"
        if runSim(arr,x,y,Dir.FORWARD):
            totalCycles = totalCycles + 1
        arr[i][j] = prev

print(totalCycles)

