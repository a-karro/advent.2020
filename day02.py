import re
with open('data/day02.txt', 'r') as f:
    lines = f.readlines()

good_one, good_two = 0, 0
for line in lines:
    parts = re.findall(r'(\d+)-(\d+) (.): (.+)', line)[0]
    chmin, chmax, letter, pwd = int(parts[0]), int(parts[1]), parts[2], parts[3]
    good_one += chmin <= pwd.count(letter) <= chmax
    good_two += (pwd[chmin-1] == letter) ^ (pwd[chmax-1] == letter)

print("Puzzle 2.1: ", good_one)
print("Puzzle 2.2: ", good_two)
