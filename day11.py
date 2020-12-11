from copy import deepcopy
import helpers

seats = list()


for line in open('data/day11.txt', 'r').read().splitlines():
    seats.append(['.'] + [x for x in line] + ['.'])

seats.insert(0, ['.'] * (len(seats[0])))
seats.append(['.'] * (len(seats[0])))
dx = len(seats[0]) - 2
dy = len(seats) - 2

deltas = {(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)}


def is_in_range(ex, ey, p):
    x, y = p
    return 1 <= x <= ex and 1 <= y <= ey


def count_empty_adjacent(s, x, y):
    r = 0
    for d in deltas:
        x_, y_ = helpers.add_delta((x, y), d)
        r += s[y_][x_] != '#'
    return r


def count_empty_far(s, x, y):
    r = 0
    for d in deltas:
        x_, y_ = helpers.add_delta((x, y), d)
        taken = False
        while is_in_range(dx, dy, (x_, y_)):
            taken = taken or s[y_][x_] == '#'
            if taken or s[y_][x_] != '.':
                break
            x_, y_ = helpers.add_delta((x_, y_), d)
        if not taken:
            r += 1
    return r


def engine(s, f_count, limit):
    while True:
        res = []
        for y in range(1, dy+2):
            for x in range(1, dx+2):
                if s[y][x] in '#L':
                    k = f_count(s, x, y)
                    if k == 8 and s[y][x] == 'L':
                        res.append(((x, y), '#'))
                    elif s[y][x] == '#' and k <= len(deltas) - limit:
                        res.append(((x, y), 'L'))
        if len(res) == 0:
            break
        for c, new in res:
            s[c[1]][c[0]] = new
    return s


def count_taken(s):
    c = 0
    for y in range(1, len(s) - 1):
        for x in range(1, len(s[0]) - 1):
            c += s[y][x] == '#'
    return c


old = deepcopy(seats)
print("Puzzle 11.1: ", count_taken(engine(seats, count_empty_adjacent, 4)))
seats = deepcopy(old)
print("Puzzle 11.2: ", count_taken(engine(seats, count_empty_far, 5)))
