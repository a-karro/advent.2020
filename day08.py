def run(mem, store):
    acc = 0
    pointer = 0
    seen = []
    while pointer < len(mem) and pointer not in seen:
        seen.append(pointer)
        if mem[pointer][0] == 'nop':
            if store:
                to_change.append((('jmp', mem[pointer][1]), pointer))
        if mem[pointer][0] == 'acc':
            acc += mem[pointer][1]
        if mem[pointer][0] == 'jmp':
            if store:
                to_change.append((('nop', mem[pointer][1]), pointer))
            pointer += mem[pointer][1] - 1
        pointer += 1
    return acc, True if pointer >= len(mem) else False


ops = [(x[0], int(x[1])) for n in open('data/day08.txt', 'r').read().splitlines() for x in [n.split()]]
to_change = []

print("Puzzle 8.1: ", run(ops, True)[0])

n = 0
jmp_out = False
for x in to_change:
    orig = ops[x[1]]
    ops[x[1]] = x[0]
    n, jmp_out = run(ops, False)
    if jmp_out:
        break
    else:
        ops[x[1]] = orig

print("Puzzle 8.2: ", n)
