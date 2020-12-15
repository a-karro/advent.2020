lines = open('data/day13.txt', 'r').read().splitlines()

now = int(lines[0])
buses = [(int(x), pos) for pos, x in enumerate(lines[1].split(',')) if x.isdecimal()]


n_furthest = now + max([b[0] for b in buses])

bus = -1
then = now

for x in range(now, n_furthest):
    for b, p in buses:
        if x % b == 0:
            bus = b
            then = x
            break
    if bus > -1:
        break

print("Puzzle 13.1: ", bus*(then - now))
