from enum import Enum
import re
file = open("/home/blusk/Documents/adventofcode2024/day_3/input")
res = 0
enabled = True
for line in file:
    reMatch = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",line)
    for m in reMatch:
        if "mul" in m and enabled:
            nums = re.findall("\d{1,3}",m)
            res = res + (int(nums[0]) * int(nums[1]))
        elif "don't" in m:
            enabled = False
        elif "do" in m:
            enabled = True

print(res)