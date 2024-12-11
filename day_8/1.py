file = open("/home/blusk/Documents/adventofcode2024/day_8/input")
arr = []
ant = {}
uniqueLoc = set()
totalCount = 0
def isValid(x,y,arr):
    if x > -1 and x < len(arr) and y > -1 and y < len(arr[0]):
        return True
def calcDist(p1,p2):
    distRow = (p1[0] - p2[0]) * 2
    distCol = (p1[1] - p2[1]) * 2
    aRow = distRow + p2[0]
    aCol = distCol + p2[1]
    return (aRow, aCol)
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
            a = calcDist(p1,p2)
            b = calcDist(p2,p1)
            if isValid(a[0], a[1], arr) and a not in uniqueLoc:
                uniqueLoc.add(a)
                totalCount = totalCount + 1
            if isValid(b[0], b[1], arr) and b not in uniqueLoc:
                uniqueLoc.add(b)
                totalCount = totalCount + 1

print(totalCount)

