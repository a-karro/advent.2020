def search(bags, current):
    seen = list()
    for b in bags:
        if current in [e['c'] for e in b[1]]:
            seen.append(b[0])
            seen.extend(search(bags, b[0]))
    return seen


def count(bags, current):
    cnt = 1
    for b in bags:
        if current == b[0]:
            for s in b[1]:
                cnt += count(bags, s['c']) * s['v']
    return cnt


lines = open('data/day07.txt', 'r').read().splitlines()

g = list()
for line in lines:
    lp = line.split(' bags contain ')
    r = line.split(' bags contain ')[0]
    ch = []
    if lp[1] != "no other bags.":
        cont = lp[1][:-1].split(', ')
        for c in cont:
            p = c.split()
            ch.append({'c': ' '.join(p[1:3]), 'v': int(p[0])})
    g.append([r, ch])


cc = 'shiny gold'

print("Puzzle 7.1: ", len(set(search(g, cc))))
print("Puzzle 7.1: ", count(g, cc) - 1)
