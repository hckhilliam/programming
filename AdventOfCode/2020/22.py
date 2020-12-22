from collections import deque


def part1(data):
    rows = parse_data(data)
    p1 = deque()
    p2 = deque()
    i = 1
    while rows[i] != '':
        p1.append(int(rows[i]))
        i += 1
    i += 2
    while i < len(rows):
        p2.append(int(rows[i]))
        i += 1

    while p1 and p2:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    f = p1 if p1 else p2
    total = 0
    multiplier = 1
    while f:
        total += multiplier * f.pop()
        multiplier += 1
    return total


def part2(data):
    rows = parse_data(data)
    p1 = deque()
    p2 = deque()
    i = 1
    while rows[i] != '':
        p1.append(int(rows[i]))
        i += 1
    i += 2
    while i < len(rows):
        p2.append(int(rows[i]))
        i += 1

    winner = recurse(p1, p2)
    if winner:
        f = p1
    else:
        f = p2
    total = 0
    multiplier = 1
    while f:
        total += multiplier * f.pop()
        multiplier += 1
    return total


def recurse(p1, p2):
    comps = set()
    while p1 and p2:
        t1 = tuple(p1)
        t2 = tuple(p2)
        if (t1, t2) in comps:
            return True
        comps.add((t1, t2))

        c1 = p1.popleft()
        c2 = p2.popleft()

        if len(p1) >= c1 and len(p2) >= c2:
            winner = recurse(deque(list(p1)[:c1]), deque(list(p2)[:c2]))
        else:
            winner = c1 > c2
        if winner:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return bool(p1)


def parse_data(data):
    rows = data.split('\n')
    return rows
