from itertools import combinations

with open('data/day01.txt', 'r') as f:
    items = set([int(i) for i in f.readlines()])

twos = next(a * b for a, b in combinations(items, 2) if a + b == 2020)
threes = next(a * b * c for a, b, c in combinations(items, 3) if a + b + c == 2020)
print("Puzzle 1.1: ", twos)
print("Puzzle 1.2: ", threes)
