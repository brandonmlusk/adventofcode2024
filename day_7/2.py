def backtrack(pos,sum,row,target):
    if pos == len(row):
        return sum == target
    for op in ["+","*","||"]:
        if op == "+":
            newSum = sum + row[pos]
        elif op == "*":
            newSum = sum * row[pos]
        else:
            newSum = int(str(sum)+str(row[pos]))
        if backtrack(pos + 1, newSum, row, target):
            return True
    return False

file = open("/home/blusk/Documents/adventofcode2024/day_7/input")
arr = []
totalSum = 0
for line in file:
    line = line[:-1]
    line = line.replace(":","")
    arr.append(list(map(int, line.split())))

for row in arr:
    if backtrack(2,row[1],row,row[0]):
        totalSum = totalSum + row[0]

print(totalSum)

