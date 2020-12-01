from itertools import combinations

with open('data/day01.txt', 'r') as f:
    items = [int(i) for i in f.readlines()]

twos = [t[0] * t[1] for t in combinations(items, 2) if sum(t) == 2020]
threes = [t[0] * t[1] * t[2] for t in combinations(items, 3) if sum(t) == 2020]
print("Puzzle 1.1: ", twos[0])
print("Puzzle 1.2: ", threes[0])
