import re
import itertools
from collections import defaultdict


chunks = open('data/day16.txt', 'r').read().split('\n\n')

parts = dict()
for line in chunks[0].split('\n'):
    p, data = line.split(':')
    a, b, c, d = [int(x) for x in re.findall(r'(\d+)', data)]
    el = list(range(a, b + 1))
    el.extend(list(range(c, d + 1)))
    parts[p] = set(el)

ticket = [int(x) for x in chunks[1].split('\n')[1].split(',')]

near_tickets = [[int(x) for x in t.split(',')] for t in chunks[2].split('\n')[1:]]

good = list()
good.append(ticket)
inv = 0

valid = list(itertools.chain.from_iterable(parts.values()))
for t in near_tickets:
    g = True
    for i in t:
        if i not in valid:
            g = False
            inv += i
    if g:
        good.append(t)

print("Puzzle 15.1: ", inv)

names = defaultdict(list)

for pos in range(len(good[0])):
    rr = [n[pos] for n in good]
    for k, v in parts.items():
        if sum(1 for x in rr if x in v) == len(good):
            names[k].append(pos)


while True:
    unique = list()
    for k in names.keys():
        if len(names[k]) == 1:
            unique.append(names[k][0])
    if len(unique) == len(names.keys()):
        break
    for k, v in names.items():
        if len(v) > 1:
            for u in unique:
                if u in v:
                    v.remove(u)

s = 1
for k, v in names.items():
    if 'departure' in k:
        s = s * ticket[v[0]]

print("Puzzle 15.2: ", s)
