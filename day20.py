from helpers import flatten
from functools import reduce
from operator import mul

raw = open('data/day20.txt', 'r').read().split('\n\n')


def to_int(line):
    return [int(line.replace('.', '0').replace('#', '1'), 2),
            int(line[::-1].replace('.', '0').replace('#', '1'), 2)]


tiles = dict()
for r in raw:
    lines = r.split('\n')
    k = int(lines[0][5:9])
    b = list()
    b.extend(to_int(lines[1]))
    b.extend(to_int(lines[len(lines)-1]))
    b.extend(to_int(''.join(x[0] for x in lines[1:])))
    b.extend(to_int(''.join(x[len(x)-1] for x in lines[1:])))
    tiles[k] = b

flat_borders = list(flatten(tiles.values()))
outers = [x for x in flat_borders if flat_borders.count(x) == 1]

corners = [k for k, v in tiles.items() if sum(1 for x in v if x in outers) == 4]

print("Puzzle 20.1: ", reduce(mul, corners))
