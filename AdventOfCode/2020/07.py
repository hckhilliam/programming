from collections import defaultdict


def part1(data):
    rows = parse_data(data)
    bags = defaultdict(set)
    for r in rows:
        p1s = r.split(' contain ')
        source = p1s[0].replace(' bags', '')
        vals = p1s[1].split(', ')
        if vals[0] == 'no other bags.':
            continue
        for v in vals:
            v = v.replace(' bags', '').replace(' bag', '').replace('.', '')
            # skip the number
            i = 0
            while i < len(v):
                if v[i] == ' ':
                    break
                i += 1
            v = v[i + 1:]
            bags[v].add(source)
    a = set()
    q = ['shiny gold']
    while q:
        curr = q.pop()
        for s in bags[curr]:
            if s in a:
                continue
            a.add(s)
            q.append(s)
    return len(a)


def part2(data):
    rows = parse_data(data)
    bags = defaultdict(dict)
    for r in rows:
        p1s = r.split(' contain ')
        source = p1s[0].replace(' bags', '')
        vals = p1s[1].split(', ')
        if vals[0] == 'no other bags.':
            continue
        for v in vals:
            v = v.replace(' bags', '').replace(' bag', '').replace('.', '')
            # skip the number
            i = 0
            while i < len(v):
                if v[i] == ' ':
                    break
                i += 1
            bags[source][v[i + 1:]] = int(v[:i])
    total = find_total('shiny gold', bags) - 1
    return total


def find_total(s, bags):
    total = 1
    for b, c in bags[s].items():
        total += c * find_total(b, bags)
    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
