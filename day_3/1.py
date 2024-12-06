from enum import Enum
import re
file = open("/home/blusk/Documents/adventofcode2024/day_3/input")
res = 0
for line in file:
    reMatch = re.findall("mul\(\d{1,3},\d{1,3}\)",line)
    for m in reMatch:
        nums = re.findall("\d{1,3}",m)
        res = res + (int(nums[0]) * int(nums[1]))

print(res)