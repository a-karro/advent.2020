lines = open('data/day05.txt', 'r').read().splitlines()

x = {int(a.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for a in lines}

mx = max(x)
print("Puzzle 5.1: ", mx)
print("Puzzle 5:2: ", next(s for s in range(mx+1) if s-1 in x and s+1 in x and s not in x))
