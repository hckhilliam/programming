from collections import defaultdict


def part1(data):
    allergen_map, count = parse_data(data)
    total = 0
    for ingredient, cnt in count.items():
        total += cnt
        for allergen, potentials in allergen_map.items():
            if ingredient in potentials:
                total -= cnt
                break
    return total


def part2(data):
    allergen_map, count = parse_data(data)
    reverse = defaultdict(set)
    final = {}
    q = []
    for allergen, ingredients in allergen_map.items():
        for ingredient in ingredients:
            reverse[ingredient].add(allergen)

        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            final[allergen] = ingredient
            q.append(ingredient)

    while q:
        ingredient = q.pop()
        for allergen in reverse[ingredient]:
            allergen_map[allergen].remove(ingredient)
            if len(allergen_map[allergen]) == 1:
                newI = list(allergen_map[allergen])[0]
                final[allergen] = newI
                q.append(newI)

    return ','.join([final[i] for i in sorted(final.keys())])


def parse_data(data):
    rows = data.split('\n')
    count = defaultdict(int)
    allergen_map = {}
    for r in rows:
        parts = r.split('(')
        ingredients = set(parts[0].strip().split(' '))
        allergens = set(parts[1][9:-1].split(', '))
        for i in ingredients:
            count[i] += 1
        for a in allergens:
            if a not in allergen_map:
                allergen_map[a] = ingredients
            else:
                allergen_map[a] = allergen_map[a].intersection(ingredients)
    return allergen_map, count
