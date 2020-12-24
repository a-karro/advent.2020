from collections import defaultdict

import helpers

data = [s.upper() for s in open('data/day24.txt', 'r').read().splitlines()]

tiles = defaultdict(int)

for line in data:
    c = (0, 0, 0)
    while len(line) > 0:
        if line[0] in 'SN':
            n = line[:2]
            line = line[2:]
        else:
            n = line[0]
            line = line[1:]
        c = helpers.add_delta(c, helpers.HEX[n])
    tiles[c] = tiles[c] ^ 1


print("Puzzle 24.1: ", sum(tiles.values()))


cnt = 0
while cnt < 100:
    cnt += 1
    nw = dict()

    keys = list(tiles.keys())
    for k in keys:
        for n in [helpers.add_delta(k, r) for r in helpers.HEX.values()]:
            tiles[n] = tiles[n]

    keys = list(tiles.keys())
    for k in keys:
        neighbors = [helpers.add_delta(k, r) for r in helpers.HEX.values()]
        t = sum(tiles[n] for n in neighbors)
        if (t == 0 or t > 2) and tiles[k] == 1:
            nw[k] = 0
        elif t == 2 and tiles[k] == 0:
            nw[k] = 1

    for a, b in nw.items():
        tiles[a] = b

    print('day {}: {}'.format(cnt, sum(tiles.values())))

print("Puzzle 24.2: ", sum(tiles.values()))
