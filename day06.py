groups = [a.split('\n') for a in open('data/day06.txt', 'r').read().split('\n\n')]

print("Puzzle 6.1: ", sum(len(set(''.join(g))) for g in groups))
print("Puzzle 6.2: ", sum(len(set.intersection(*[set(x) for x in g])) for g in groups))
