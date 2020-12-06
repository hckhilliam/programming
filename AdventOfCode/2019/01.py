def part1(data):
    rows = parse_data(data)
    s = 0
    for r in rows:
        s += int(int(r) / 3) - 2
    return s


def part2(data):
    rows = parse_data(data)
    s = 0
    for r in rows:
        v = int(int(r) / 3) - 2
        while v > 0:
            s += v
            v = int(int(v) / 3) - 2
    return s


def parse_data(data):
    rows = data.split('\n')
    return rows
