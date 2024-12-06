def isMatch(word):
    if len(word) != 4:
        return False
    if word == "XMAS":
        return True
    if word == "SAMX":
        return True
    
file = open("/home/blusk/Documents/adventofcode2024/day_4/input")
arr = []
totalCount = 0
for line in file:
    arr.append(list(line[:-1]))

m = len(arr) # number of rows
n = len(arr[1]) # number of columns
for i in range(m):
    word = ""
    for j in range(n):
        if len(word) == 4:
            word = word[1:]
        word = word + arr[i][j]
        if isMatch(word):
            totalCount = totalCount + 1

for j in range(n):
    word = ""
    for i in range(m):
        if len(word) == 4:
            word = word[1:]
        word = word + arr[i][j]
        if isMatch(word):
            totalCount = totalCount + 1


for start in range(m):
    word = ""
    i = start
    k = 0
    while i < m and k < n:
        if len(word) == 4:
            word = word[1:]
        word = word + arr[i][k]
        if isMatch(word):
            totalCount = totalCount + 1
        i = i + 1
        k = k + 1

for start in range(1,n):
    word = ""
    i = 0
    k = start
    while i < m and k < n:
        if len(word) == 4:
            word = word[1:]
        word = word + arr[i][k]
        if isMatch(word):
            totalCount = totalCount + 1
        i = i + 1
        k = k + 1

for start in range(n-1,-1,-1):
    i = 0
    k = start
    word = ""
    while i < m and k > -1:
        if len(word) == 4:
            word = word[1:]
        word = word + arr[i][k]
        if isMatch(word):
            totalCount = totalCount + 1
        i = i + 1
        k = k - 1

for start in range(1,m):
    i = start
    k = n - 1
    word = ""
    while i < m and k > -1:
        if len(word) == 4:
            word = word[1:]
        word = word + arr[i][k]
        if isMatch(word):
            totalCount = totalCount + 1
        i = i + 1
        k = k - 1

print(totalCount)
