from itertools import combinations

numbers = [int(x) for x in open('data/day09.txt', 'r').readlines()]

pr_len = 25
preambles = [[a+b for a, b in combinations(numbers[:pr_len], 2)]]

res = -1
for c, n in enumerate(numbers[pr_len:]):
    f = False
    for x in preambles:
        if n in x:
            f = True
    if not f:
        res = n
        break
    preambles.append([a + b for a, b in combinations(numbers[c+1: pr_len + c+1], 2)])
    preambles.pop(0)

print("Puzzle 9.1: ", res)

t = b = s = 0
while s != res:
    if s < res:
        s += numbers[b]
        b += 1
    else:
        s -= numbers[t]
        t += 1

print("Puzzle 9.2: ", min(numbers[t:b]) + max(numbers[t:b]))
