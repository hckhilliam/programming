def part1(data):
    data = [int(i) for i in parse_data(data)[0].split(',')]
    d = {k: i + 1 for i, k in enumerate(data[:-1])}
    num = data[-1]
    turn = len(data)

    while turn < 2020:
        if num not in d:
            d[num] = turn
            num = 0
        else:
            t = turn - d[num]
            d[num] = turn
            num = t
        turn += 1
    return num


def part2(data):
    data = [int(i) for i in parse_data(data)[0].split(',')]
    d = {k: i + 1 for i, k in enumerate(data[:-1])}
    num = data[-1]
    turn = len(data)

    while turn < 30000000:
        if num not in d:
            d[num] = turn
            num = 0
        else:
            t = turn - d[num]
            d[num] = turn
            num = t
        turn += 1
    return num


def parse_data(data):
    rows = data.split('\n')
    return rows
