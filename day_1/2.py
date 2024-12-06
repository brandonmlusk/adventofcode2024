file = open("/home/blusk/Documents/adventofcode2024/day_1/input")
sim = 0
listA = []
listB = []
for line in file:
    numbers = line.split("   ")
    listA.append(int(numbers[0]))
    listB.append(int(numbers[1]))

listA.sort()
listB.sort()
counts = {}
for b in listB:
    counts[b] = counts.get(b,0) + 1
for a in listA:
    sim = sim + (a*counts.get(a,0))
print(sim)
