data = open("day1.txt", 'r').read()

nums = data.splitlines()

count=0
previous = 0
for i in nums[1:]:
    if int(i)>previous:
        count+=1
    previous = int(i)

print(count)