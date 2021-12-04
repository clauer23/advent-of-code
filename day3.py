import re

data = open("day3.txt", 'r').read()

nums = data.splitlines()

gamma = ''
epsilon = ''

ones = [0,0,0,0,0,0,0,0,0,0,0,0]

zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(nums)):
    for j in range(0, len(nums[i])):
        if nums[i][j] == '1':
            ones[j]+=1
        else:
            zeros[j]+=1

for i in range(0, len(ones)):
    if ones[i]>zeros[i]:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2)*int(epsilon, 2))

oxyNums = nums
newOxyNums = []
co2Nums = nums
newCo2Nums = []

ones = [0,0,0,0,0,0,0,0,0,0,0,0]

zeros = [0,0,0,0,0,0,0,0,0,0,0,0]


for i in range(0, len(nums[0])):
    for j in range(0, len(oxyNums)):
        if oxyNums[j][i] == '1':
            ones[i]+=1
        else:
            zeros[i]+=1
    for j in range(0, len(oxyNums)):
        if ones[i]>=zeros[i]:
            if oxyNums[j][i]=='1':
                newOxyNums.append(oxyNums[j])
        else:
            if oxyNums[j][i]=='0':
                newOxyNums.append(oxyNums[j])
    if len(newOxyNums)==1:
        print(newOxyNums)
        print(zeros, ones)
        oxy = int(newOxyNums[0],2 )
        break
    else:
        oxyNums = newOxyNums
        newOxyNums = []

ones = [0,0,0,0,0,0,0,0,0,0,0,0]

zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(nums[0])):
    for j in range(0, len(co2Nums)):
        if co2Nums[j][i] == '1':
            ones[i]+=1
        else:
            zeros[i]+=1
    for j in range(0, len(co2Nums)):
        if ones[i]<zeros[i]:
            if co2Nums[j][i]=='1':
                newCo2Nums.append(co2Nums[j])
        else:
            if co2Nums[j][i]=='0':
                newCo2Nums.append(co2Nums[j])
    if len(newCo2Nums)==1:
        print(newCo2Nums)
        print(zeros, ones)
        co2 = int(newCo2Nums[0], 2)
        break
    else:
        co2Nums = newCo2Nums
        newCo2Nums = []

print(oxy)
print(co2)
print(oxy*co2)