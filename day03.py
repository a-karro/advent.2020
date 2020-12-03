def count_trees(deltas, forest):
    counter = forest[0][0]
    x = y = 0
    while True:
        x += deltas[0]
        y += deltas[1]
        if y >= len(forest):
            break
        counter += forest[y][x % len(forest[0])]
    return counter


with open('data/day03.txt', 'r') as f:
    trees = [[1 if ch == "#" else 0 for ch in line.strip()] for line in f.readlines()]


m = count_trees((3, 1), trees)
print("Puzzle 3.1: ", m)

variants = [(1, 1), (5, 1), (7, 1), (1, 2)]

for v in variants:
    m = m * count_trees(v, trees)

print("Puzzle 3.2: ", m)
