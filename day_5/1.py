def validate (dep, nums,i):
    for d in dep.get(nums[i],[]):
        if nums.count(d) == 0:
            continue
        idx = nums.index(d)
        if idx > i:
            return False
    return True

file = open("/home/blusk/Documents/adventofcode2024/day_5/input")
dep = {}
medianSum = 0
for line in file:
    line = line[:-1]
    if "|" in line:
        numbers = line.strip().split("|")
        dep.setdefault(int(numbers[1]),[])
        dep.get(int(numbers[1])).append(int(numbers[0]))
    elif line == "":
        continue
    else:
        nums = list(map(int, line.split(",")))
        valid = True
        for i in range(len(nums)):
            if not validate(dep,nums,i):
                valid = False
                break
        if valid:
            medianSum = medianSum + nums[len(nums)//2]

print(medianSum)

