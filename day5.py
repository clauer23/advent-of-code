import re, numpy as np

data = open("day5.txt", 'r').read()

nums = data.splitlines()

counts = np.full((1000, 1000), 0)
count = 0

points = []

for i in nums:
    points.append(re.split(" -> ", i))

for j in range(0, len(points)):
    for k in range(0, 2):
        points[j][k] = points[j][k].split(',')
        for i in range(0, len(points[j][k])):
            points[j][k][i] = int(points[j][k][i])

for i in points:
    if i[0][0] == i[1][0]:
        if i[1][1]>=i[0][1]:
            for j in range(i[0][1], i[1][1]+1):
                counts[j][i[0][0]] += 1
        else:
            for j in range(i[1][1], i[0][1]+1):
                counts[j][i[0][0]] += 1
    elif i[0][1] == i[1][1]:
        if i[1][0]>=i[0][0]:
            for j in range(i[0][0], i[1][0]+1):
                counts[i[0][1]][j] += 1
        else:
            for j in range(i[1][0], i[0][0]+1):
                counts[i[0][1]][j] += 1
    else:
        if i[1][0]>=i[0][0]:
            if i[1][1]>=i[0][1]:
                for j in range(i[0][0], i[1][0]+1):
                    counts[j+i[0][1]-i[0][0]][j] += 1
            else:
                for j in range(i[0][0], i[1][0]+1):
                    counts[i[0][0]+i[0][1]-j][j] += 1
        else:
            if i[1][1]>=i[0][1]:
                for j in range(i[1][0], i[0][0]+1):
                    counts[i[0][0]+i[0][1]-j][j] += 1
            else:
                for j in range(i[1][0], i[0][0]+1):
                    counts[j+i[1][1]-i[1][0]][j] += 1



for i in range(0, len(counts)):
    for j in range(0, len(counts[i])):
        if counts[i][j] >= 2:
            count += 1

print(points)
print(counts)
print(count)
