from collections import defaultdict

lines = open('data/day17.txt', 'r').read().splitlines()

space_3d = defaultdict(lambda: '.')
space_4d = defaultdict(lambda: '.')

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        space_3d[x, y, 0] = c
        space_4d[x, y, 0, 0] = c


def get_near_3d(x, y, z):
    res = list()
    for z_ in range(z-1, z+2):
        for y_ in range(y-1, y+2):
            for x_ in range(x-1, x+2):
                if x == x_ and y == y_ and z == z_:
                    continue
                res.append([x_, y_, z_])
    return res


def get_near_4d(x, y, z, w):
    res = list()
    for w_ in range(w - 1, w + 2):
        for z_ in range(z - 1, z + 2):
            for y_ in range(y - 1, y + 2):
                for x_ in range(x - 1, x + 2):
                    if x == x_ and y == y_ and z == z_ and w == w_:
                        continue
                    res.append([x_, y_, z_, w_])
    return res


for t in range(6):
    new_3d = defaultdict(lambda: '.')
    ranges = space_3d.keys()
    range_x = min(v[0] for v in ranges) - 1, max(v[0] for v in ranges) + 2
    range_y = min(v[1] for v in ranges) - 1, max(v[1] for v in ranges) + 2
    range_z = min(v[2] for v in ranges) - 1, max(v[2] for v in ranges) + 2
    for x in range(range_x[0], range_x[1]):
        for y in range(range_y[0], range_y[1]):
            for z in range(range_z[0], range_z[1]):
                active_neighbors = sum(1 for a, b, c in get_near_3d(x, y, z) if space_3d[a, b, c] == '#')
                if space_3d[x, y, z] == '#':
                    if 2 <= active_neighbors <= 3:
                        new_3d[x, y, z] = '#'
                    else:
                        new_3d[x, y, z] = '.'
                if space_3d[x, y, z] == '.' and active_neighbors == 3:
                    new_3d[x, y, z] = '#'
    space_3d = new_3d.copy()

for t in range(6):
    new_4d = defaultdict(lambda: '.')
    ranges = space_4d.keys()
    range_x = min(v[0] for v in ranges) - 1, max(v[0] for v in ranges) + 2
    range_y = min(v[1] for v in ranges) - 1, max(v[1] for v in ranges) + 2
    range_z = min(v[2] for v in ranges) - 1, max(v[2] for v in ranges) + 2
    range_w = min(v[3] for v in ranges) - 1, max(v[3] for v in ranges) + 2
    for x in range(range_x[0], range_x[1]):
        for y in range(range_y[0], range_y[1]):
            for z in range(range_z[0], range_z[1]):
                for w in range(range_w[0], range_w[1]):
                    active_n_4d = sum(1 for a, b, c, d in get_near_4d(x, y, z, w) if space_4d[a, b, c, d] == '#')
                    if space_4d[x, y, z, w] == '#':
                        if 2 <= active_n_4d <= 3:
                            new_4d[x, y, z, w] = '#'
                        else:
                            new_4d[x, y, z, w] = '.'
                    if space_4d[x, y, z, w] == '.' and active_n_4d == 3:
                        new_4d[x, y, z, w] = '#'

    space_4d = new_4d.copy()

print("Puzzle 17.1: ", sum(1 for x in space_3d.values() if x == '#'))
print("Puzzle 17.2: ", sum(1 for x in space_4d.values() if x == '#'))
