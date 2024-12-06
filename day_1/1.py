file = open("/home/blusk/Documents/adventofcode2024/day_1/input")
totalDiff = 0
listA = []
listB = []
for line in file:
    numbers = line.split("   ")
    listA.append(int(numbers[0]))
    listB.append(int(numbers[1]))

listA.sort()
listB.sort()
for a,b in zip(listA, listB):
    totalDiff = totalDiff + abs(a-b)
print(totalDiff)
