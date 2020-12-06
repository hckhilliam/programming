import math


def part1(data):
    rows = parse_data(data)
    m = 0
    for r in rows:
        m = max(findV(r), m)
    return m


def part2(data):
    rows = parse_data(data)
    ids = set()
    for r in rows:
        ids.add(findV(r))
    i = 0
    while i not in ids:
        i += 1
    while i in ids:
        i += 1
    return i


def findV(r):
    rs = r[:-3]
    cs = r[-3:]
    pz = 0
    p = 127
    for rr in rs:
        if rr == 'F':
            p = int((p + pz) / 2)
        elif rr == 'B':
            pz = math.ceil((p + pz) / 2)
    fr = p
    pz = 0
    p = 7
    for cc in cs:
        if cc == 'L':
            p = int((p + pz) / 2)
        elif cc == 'R':
            pz = math.ceil((p + pz) / 2)
    fc = p
    return fr * 8 + fc


def parse_data(data):
    rows = data.split('\n')
    return rows
