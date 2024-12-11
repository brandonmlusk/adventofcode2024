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

def incCount(x,y,arr):
    global totalCount
    if arr[x][y] != "X":
        totalCount = totalCount + 1
    arr[x][y] = "X"

file = open("/home/blusk/Documents/adventofcode2024/day_6/input")
arr = []
x,y = 0,0
totalCount = 0
for line in file:
    line = line[:-1]
    arr.append(list(line))
    if line.count("^"):
        x = len(arr) - 1 if len(arr) - 1 > 0 else 0
        y = line.index("^")

currentDir = Dir.FORWARD
while x > -1 and x < len(arr) and y > -1 and y < len(arr[x]):
    if currentDir == Dir.FORWARD and isObstruct(x,y,arr,currentDir):
        currentDir = Dir.RIGHT
    elif currentDir == Dir.FORWARD:
        incCount(x,y,arr)
        x = x - 1
    elif currentDir == Dir.RIGHT and isObstruct(x,y,arr,currentDir):
        currentDir = currentDir.BACKWARD
    elif currentDir == Dir.RIGHT:
        incCount(x,y,arr)
        y = y + 1
    elif currentDir == Dir.BACKWARD and isObstruct(x,y,arr,currentDir):
        currentDir = Dir.LEFT
    elif currentDir == Dir.BACKWARD:
        incCount(x,y,arr)
        x = x + 1
    elif currentDir == Dir.LEFT and isObstruct(x,y,arr,currentDir):
        currentDir = Dir.FORWARD
    else:
        incCount(x,y,arr)
        y = y - 1

print(totalCount)

