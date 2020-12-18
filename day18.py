lines = open('data/day18.txt', 'r').read().splitlines()


def match_par(l_):
    op = -1
    opc = clc = 0
    for i, c in enumerate(l_):
        if c == '(':
            opc += 1
            if op < 0:
                op = i
        if c == ')':
            clc += 1
            if opc == clc:
                return op, i+1
    return 0, len(l_)


def evaluate(l_, simple=True):
    while l_.find('(') > -1:
        i = match_par(l_)
        sl = l_[i[0]:i[1]]
        res = evaluate(sl[1:-1], simple)
        l_ = l_.replace(sl, str(res))

    parts = l_.split(' ')

    if not simple:
        while '+' in parts:
            k = parts.index('+')
            parts = parts[:k-1] + [str(int(parts[k-1]) + int(parts[k+1]))] + parts[k+2:]

    res = int(parts[0])
    while len(parts) > 1:
        if parts[1] == '*':
            res = res * int(parts[2])
        else:
            res = res + int(parts[2])
        if len(parts) > 3:
            parts = [str(res)] + parts[3:]
        else:
            parts = []
    return res


print("Puzzle 18.1: ", sum(evaluate(line, simple=True) for line in lines))
print("Puzzle 18.2: ", sum(evaluate(line, simple=False) for line in lines))
