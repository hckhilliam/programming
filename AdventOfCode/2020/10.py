def part1(data):
    rows = [int(r) for r in parse_data(data)]
    rows.sort()
    diffOne = 0
    diffThree = 1
    if rows[0] == 1:
        diffOne += 1
    elif rows[0] == 3:
        diffThree += 1
    for i in range(1, len(rows)):
        d = rows[i] - rows[i - 1]
        if d == 1:
            diffOne += 1
        elif d == 3:
            diffThree += 1
    return diffOne * diffThree


def part2(data):
    rows = [int(r) for r in parse_data(data)]
    rows.sort()
    d = [0 for i in range(len(rows))]
    d[-1] = 1
    for i in range(len(rows) - 2, -1, -1):
        j = i + 1
        while j < len(rows) and rows[j] - rows[i] <= 3:
            d[i] += d[j]
            j += 1
    total = 0
    i = 0
    while rows[i] <= 3:
        total += d[i]
        i += 1
    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
