def isMatch(x,y,arr,m,n):
    first = arr[x-1][y-1] if x - 1 > -1 and y - 1 > -1 else None
    second = arr[x+1][y+1] if x + 1 < m and y + 1 < n else None
    third = arr[x+1][y-1] if x + 1 < m and y - 1 > -1 else None
    fourth = arr[x-1][y+1] if x - 1 > -1 and y + 1 < n else None
    #F.T
    #...
    #H.S
    if not first or not second or not third or not fourth:
        return False
    one = first + second
    two = third + fourth
    if ("MS" in one or "SM" in one) and ("MS" in two or "SM" in two):
        return True
    return False
    
file = open("/home/blusk/Documents/adventofcode2024/day_4/input")
arr = []
totalCount = 0
for line in file:
    arr.append(list(line[:-1]))

m = len(arr) # number of rows
n = len(arr[1]) # number of columns
for i in range(m):
    for j in range(n):
        if arr[i][j] == "A":
            if isMatch(i,j,arr,m,n):
                totalCount = totalCount + 1
print(totalCount)

