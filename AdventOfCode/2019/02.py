def part1(data):
    rows = parse_data(data)
    codes = [int(c) for c in rows[0].split(',')]
    codes[1] = 12
    codes[2] = 2
    i = 0
    while True:
        f = codes[i]
        if f == 99:
            break
        n = codes[codes[i + 1]]
        n2 = codes[codes[i + 2]]
        if f == 1:
            codes[codes[i + 3]] = n + n2
        elif f == 2:
            codes[codes[i + 3]] = n * n2
        i += 4
    return codes[0]


def part2(data):
    rows = parse_data(data)


def parse_data(data):
    rows = data.split('\n')
    return rows
