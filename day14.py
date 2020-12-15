import re

lines = open('data/day14.txt', 'r').read().splitlines()


def apply_mask(number, mask):
    n = format(number, 'b').zfill(len(mask))
    r = ''
    for i, c in enumerate(mask):
        r += n[i] if mask[i] == 'X' else mask[i]
    return int(r, 2)


def flipper(a_, m, number):
    try:
        idx = a_.index('X')
    except ValueError:
        m[int(''.join(a_), 2)] = number
        return

    a = a_.copy()
    a[idx] = '1'
    flipper(a, m, number)
    a[idx] = '0'
    flipper(a, m, number)


def build_addresses(mem, addr, value, mask):
    a = list(format(addr, 'b').zfill(len(mask)))
    for i, c in enumerate(mask):
        if c == 'X':
            a[i] = 'X'
        elif c == '1':
            a[i] = '1'
    flipper(a, mem, value)


mem = dict()
mem2 = dict()

mask = ""
for line in lines:
    if line.startswith('mask = '):
        mask = line[7:]
    else:
        addr, value = [int(x) for x in re.findall(r'mem\[(\d+)] = (\d+)', line)[0]]
        mem[addr] = apply_mask(value, mask)
        build_addresses(mem2, addr, value, mask)

print("Puzzle 14.1: ", sum(mem.values()))
print("Puzzle 14.2: ", sum(mem2.values()))
