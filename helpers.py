from collections import Iterable

DIRS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

COMPASS = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}


COMPASS_INV = {
    'N': (0, 1),
    'S': (0, -1),
    'W': (-1, 0),
    'E': (1, 0)
}


HEX = {
    'E': (+1, -1, 0),
    'NE': (+1, 0, -1),
    'NW': (0, +1, -1),
    'W': (-1, +1, 0),
    'SW': (-1, 0, +1),
    'SE': (0, -1, +1)
}


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def add_delta(point, delta, offset=1):
    r = []
    for i, x in enumerate(point):
        r.append(x + delta[i]*offset)
    return tuple(r)


def match_brackets(l_, brackets='()'):
    op = -1
    opc = clc = 0
    for i, c in enumerate(l_):
        if c == brackets[0]:
            opc += 1
            if op < 0:
                op = i
        if c == brackets[1]:
            clc += 1
            if opc == clc:
                return op, i+1
    raise ValueError("Didn't find matching brackets")


def pad(s):
    return ' ' + s + ' '


def get_first_bracket_content(string, brackets='()'):
    try:
        i = match_brackets(string, brackets)
        return string[i[0]+1:i[1]-1]
    except ValueError:
        return ""


def strip_sides(string, length):
    return string[length:len(string)-length]


def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
