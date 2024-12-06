from enum import Enum
def loop(numbers,direction,singleLevel):
    for n in range(1,len(numbers)):
        diff = int(numbers[n-1])-int(numbers[n])
        if(direction == Direction.UNDEF):
            direction = Direction.DEC if diff > 0 else Direction.INC
        if not isValid(direction, diff):
            if not singleLevel:
                return False
            for n in range(len(numbers)):
                l1 = numbers[:]
                l1.pop(n)
                if loop(l1,Direction.UNDEF,False):
                    return True
            return False
    return True


def isValid(direction, diff):
    if(diff > 0 and direction == Direction.INC):
        return False
    elif(diff < 0 and direction == Direction.DEC):
        return False
    elif(abs(diff) < 1 or abs(diff) > 3):
        return False
    return True

file = open("/home/blusk/Documents/adventofcode2024/day_2/input")
class Direction(Enum):
    UNDEF = 0
    INC = 2
    DEC = 3
safeReports = 0
for line in file:
    numbers = line.split(" ")
    if loop(numbers, Direction.UNDEF, True):
        safeReports = safeReports + 1
    else:
        print(line)

print(safeReports)