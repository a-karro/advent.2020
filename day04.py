import string

fields2 = sorted({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})

with open('data/day04.txt', 'r') as f:
    passports = [a.split() for a in "&".join(f.read().splitlines()).replace('&&', '^^').replace('&', ' ').split('^^')]

valid = []
for passport in passports:
    psp = {}
    for x in passport:
        k, v = x.split(':')
        psp[k] = v
    psp.pop('cid', None)
    if sorted(psp.keys()) == fields2:
        valid.append(psp)

print("Puzzle 4.1: ", len(valid))

cnt = 0
for p in valid:
    v = True
    v = v and 1920 <= int(p['byr']) <= 2002
    v = v and 2010 <= int(p['iyr']) <= 2020
    v = v and 2020 <= int(p['eyr']) <= 2030
    hgt = p['hgt']
    good = False
    if hgt[:-2].isdigit():
        if hgt[-2:] == 'cm':
            good = 150 <= int(hgt[:-2]) <= 193
        elif hgt[-2:] == 'in':
            good = 59 <= int(hgt[:-2]) <= 76
    v = v and good
    v = v and p['hcl'][0] == '#' and len([c for c in p['hcl'][1:] if c in string.hexdigits]) == 6
    v = v and p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    v = v and p['pid'].isdigit() and len(p['pid']) == 9
    cnt += v

print("Puzzle 4.2: ", cnt)
