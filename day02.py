import re
with open('data/day02.txt', 'r') as f:
    lines = f.readlines()

good_one, good_two = 0, 0
for line in lines:
    parts = re.findall(r'(\d+)-(\d+) (.): (.+)', line)[0]
    chmin, chmax, letter, pwd = int(parts[0]), int(parts[1]), parts[2], parts[3]
    good_one += 1 if chmin <= pwd.count(letter) <= chmax else 0
    if pwd[chmin-1] == letter and pwd[chmax-1] != letter or \
        pwd[chmin-1] != letter and pwd[chmax-1] == letter:
        good_two += 1

print("Puzzle 2.1: ", good_one)
print("Puzzle 2.2: ", good_two)
