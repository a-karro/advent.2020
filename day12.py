import helpers


def rotate(wp, d):
    r = d[0]
    o_ = int(d[1:]) // 90
    if r == 'R':
        o_ = 4 - o_
    o_ = o_ % 4
    if o_ == 0:
        return wp
    if o_ == 1:
        return -wp[1], wp[0]
    if o_ == 2:
        return -wp[0], -wp[1]
    if o_ == 3:
        return wp[1], -wp[0]


lines = open('data/day12.txt', 'r').read().splitlines()

dd = 'ESWN'
d = 0
x = y = 0
for l in lines:
    op = l[0]
    offs = int(l[1:])
    if op in dd:
        x, y = helpers.add_delta((x, y), helpers.COMPASS[op], offs)
    if l[0] in 'R':
        d = (d + offs // 90) % 4
    if l[0] in 'L':
        d = (d - offs // 90) % 4
    if l[0] in 'F':
        x, y = helpers.add_delta((x, y), helpers.COMPASS[dd[d]], offs)

print("Puzzle 12.1: ", helpers.manhattan((0,0), (x, y)))

x = y = 0
wp = 10, 1

for l in lines:
    dd = l[0]
    ofs = int(l[1:])
    if dd in 'NSWE':
        wp = helpers.add_delta(wp, helpers.COMPASS_INV[dd], ofs)
    if dd in 'RL':
        wp = rotate(wp, l)
    if dd in 'F':
        x, y = helpers.add_delta((x, y), wp, ofs)

print("Puzzle 12.2: ", helpers.manhattan((0, 0), (x, y)))
