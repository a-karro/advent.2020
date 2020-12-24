import helpers

data = open('data/day21.txt', 'r').read().splitlines()

allergens = list()
ingredients = list()

for d in data:
    ingredients.append([x.strip() for x in d[:d.find('(')-1].split()])
    allergens.append([x.strip() for x in d[d.find('contains ')+9:-1].split(',')])


probables = dict()
for a in helpers.flatten(allergens):
    p = list()
    for c, x in enumerate(allergens):
        if a in x:
            p.append(ingredients[c])
        if p:
            probables[a] = set(p[0])
            for s in p[1:]:
                probables[a].intersection_update(s)

while True:
    unique = list()
    for k in probables.keys():
        if len(probables[k]) == 1:
            unique.extend(list(probables[k]))
    if len(unique) == len(probables.keys()):
        break
    for k, v in probables.items():
        if len(v) > 1:
            for u in unique:
                if u in v:
                    v.remove(u)

for k, v in probables.items():
    probables[k] = list(v)[0]

flat_i = list(helpers.flatten(ingredients))
uniques = set(flat_i).difference(helpers.flatten(probables.values()))

print("Puzzle 21.1: ", (sum(flat_i.count(x) for x in uniques)))
print("Puzzle 22.2: ", ','.join(probables[k] for k in sorted(probables)))
