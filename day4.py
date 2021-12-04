import re, numpy as np

data = open("day4.txt", 'r').read()

nums = data.split("\n\n")

bingos = nums[0].split(',')
cards  = nums[1:]

trues = np.full((len(cards), 5, 5), False)

bingo = None

for i in bingos:
    for j in cards:
        j=j.splitlines()
    for j in range(0, len(cards)):
        match = re.search(i, cards[j])
        if match:
            p = match.end()//3
            
            trues[j][p//5][p%5] = True
        for u in range(0,5):
            if trues[j][u].all() or np.transpose(trues[j])[u].all():
                bingo = j
                bingoNum = i
                break
        if bingo:
            break
    if bingo:
        break

for i in trues:
    print(i)
if bingo:
    print(bingo, cards[bingo], trues[bingo], bingoNum)
