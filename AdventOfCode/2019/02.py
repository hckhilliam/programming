def part1(data):
    rows = parse_data(data)
    codes = [int(c) for c in rows[0].split(',')]
    codes[1] = 12
    codes[2] = 2
    return find_value(codes)


def part2(data):
    rows = parse_data(data)
    target = 19690720
    codes = [int(c) for c in rows[0].split(',')]
    for i in range(100):
        for j in range(100):
            inp = list(codes)
            inp[1] = i
            inp[2] = j
            if find_value(inp) == target:
                return 100 * i + j
    return -1


def find_value(codes):
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


def parse_data(data):
    rows = data.split('\n')
    return rows
