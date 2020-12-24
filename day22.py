from collections import deque


def score(qs):
    w = qs[qs[2]]
    cnt = 0
    r = 0
    while len(w) > 0:
        cnt += 1
        r += w.pop() * cnt
    return r


def part1(p1, p2):
    while True:
        pc1 = p1.popleft()
        pc2 = p2.popleft()
        win = p1 if pc1 > pc2 else p2
        win.append(max(pc1, pc2))
        win.append(min(pc1, pc2))
        if len(p1) == 0 or len(p2) == 0:
            break

    return p1, p2, 0 if len(p1) > 0 else 1


def dq_slice(q, size):
    r = deque()
    for i in range(size):
        r.append(q[i])
    return r


def norm_slice(sl):
    r = 1
    for i, c in enumerate(sl):
        r += c * pow(10, i)
    return r


def part2(p1, p2):
    rounds_p1 = []
    rounds_p2 = []
    rc = 0
    while True:
        rc += 1
        ns1 = norm_slice(p1)
        ns2 = norm_slice(p2)
        if ns1 in rounds_p1 and ns2 in rounds_p2:
            return p1, p2, 0
        pc1 = p1.popleft()
        pc2 = p2.popleft()
        rounds_p1.append(ns1)
        rounds_p2.append(ns2)
        if len(p1) >= pc1 and len(p2) >= pc2:
            a1 = dq_slice(p1, pc1)
            a2 = dq_slice(p2, pc2)
            res = part2(a1, a2)
            if res[2] == 0:
                p1.append(pc1)
                p1.append(pc2)
            else:
                p2.append(pc2)
                p2.append(pc1)
        else:
            w = p1 if pc1 > pc2 else p2
            w.append(max(pc1, pc2))
            w.append(min(pc1, pc2))

        if len(p1) == 0 or len(p2) == 0:
            break
    return p1, p2, 0 if len(p1) > 0 else 1


data = open('data/day22.txt', 'r').read().split('\n\n')

p1 = deque(map(int, data[0].split('\n')[1:]))
p2 = deque(map(int, data[1].split('\n')[1:]))
print("Puzzle 22.1: ", score(part1(p1, p2)))

p1 = deque(map(int, data[0].split('\n')[1:]))
p2 = deque(map(int, data[1].split('\n')[1:]))
print("Puzzle 22.2: ", score(part2(p1, p2)))
