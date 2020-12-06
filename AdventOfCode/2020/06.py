from collections import defaultdict


def part1(data):
    rows = parse_data(data)
    total = 0
    l = set()
    for r in rows:
        if r == '':
            total += len(l)
            l = set()
        else:
            for c in r:
                l.add(c)
    total += len(l)
    return total


def part2(data):
    rows = parse_data(data)
    total = 0
    l = defaultdict(int)
    cg = 0
    for r in rows:
        if r == '':
            for v in l.values():
                if v == cg:
                    total += 1
            l = defaultdict(int)
            cg = 0
        else:
            for c in r:
                l[c] += 1
            cg += 1
    for v in l.values():
        if v == cg:
            total += 1
    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
