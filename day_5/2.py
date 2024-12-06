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
        res = []
        for i in range(len(nums)):
            def dfs(num):
                if num not in nums or num in res:
                    return
                for d in dep.get(num,[]):
                    dfs(d)
                res.append(num)
            dfs(nums[i])
        if res != nums:
            medianSum = medianSum + res[len(res)//2]

print(medianSum)

