# https://www.python.org/doc/essays/graphs/
def find_all_paths(gg, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in gg.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(gg, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


numbers = sorted([int(x) for x in open('data/day10.txt', 'r').readlines()])

ones = threes = 1
deltas = list()
for c, number in enumerate(numbers):
    if c < len(numbers)-1:
        ones += numbers[c+1] - number == 1
        threes += numbers[c+1] - number == 3


print("Puzzle 10.1: ", ones * threes)


partitions = []
numbers.append(numbers[len(numbers)-1]+3)
numbers.insert(0, 0)
s = 0
e = 0
while e < len(numbers)-1:
    if numbers[e + 1] - numbers[e] >= 3:
        if e - s > 1:
            partitions.append((s, e+1))
        s = e + 1
    e += 1

k = 1
for p in partitions:
    graph = dict()
    for n in numbers[p[0]: p[1]+1]:
        graph[n] = []
    for c, n in enumerate(graph.keys()):
        for x in numbers[p[0]+c:p[1]+1]:
            if x != n and x - n <= 3:
                graph[n].append(x)

    m = find_all_paths(graph, numbers[p[0]], numbers[p[1]])
    k = k * len(m)

print("Puzzle 10.2: ", k)
