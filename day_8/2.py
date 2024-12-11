file = open("/home/blusk/Documents/adventofcode2024/day_8/input")
arr = []
ant = {}
uniqueLoc = set()
totalCount = 0
def isValid(x,y,arr):
    if x > -1 and x < len(arr) and y > -1 and y < len(arr[0]):
        return True
def calcSlope(p1,p2):
    distRow = (p1[0] - p2[0])
    distCol = (p1[1] - p2[1])
    return (distRow, distCol)
    
for line in file:
    line = line[:-1]
    for i in range(len(line)):
        c = line[i]
        if c != ".":
            ant.setdefault(c,[])
            ant.get(c).append((len(arr),i))
    arr.append(list(line))

for key,value in ant.items():
    for i in range(len(value)):
        for j in range(i+1,len(value)):
            p1 = value[i]
            p2 = value[j]
            m = calcSlope(p1,p2)
            x = p1[0]
            y = p1[1]
            while isValid(x,y,arr):
                if (x,y) not in uniqueLoc:
                    uniqueLoc.add((x,y))
                x = x + m[0]
                y = y + m[1]
            x = p1[0]
            y = p1[1]
            m = calcSlope(p2,p1)
            while isValid(x,y,arr):
                if (x,y) not in uniqueLoc:
                    uniqueLoc.add((x,y))
                x = x + m[0]
                y = y + m[1]

print(len(uniqueLoc))

