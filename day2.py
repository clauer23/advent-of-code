import numpy, re

data = open("day2.txt", 'r').read()

nums = data.splitlines()

aim = 0

horizontal = 0

depth = 0

for i in nums:
    if re.search(r"forward\s\d", i):
        horizontal+=int(i[-1])
        depth+=aim*int(i[-1])
    elif re.search(r"down\s\d", i):
        aim-=int(i[-1])
    elif re.search(r"up\s\d", i):
        aim+=int(i[-1])


print(horizontal *depth)