from collections import defaultdict

numbers = [int(x) for x in open('data/day15.txt', 'r').read().split(',')]


def counter(limit, n):
    tt = defaultdict(list)
    for t, c in enumerate(n):
        tt[c] = [t + 1]

    t = len(n)
    cur = n[t - 1]
    while t <= limit - 1:
        t += 1
        prev = tt[cur]
        if prev:
            if len(prev) == 1:
                cur = 0
            else:
                cur = prev[1] - prev[0]
        else:
            cur = 0
        if len(tt[cur]) > 0:
            tt[cur] = [tt[cur][-1], t]
        else:
            tt[cur] = [t]
    return cur


print("Puzzle 15.1: ", counter(2020, numbers))
print("Puzzle 15.2: ", counter(30000000, numbers))
