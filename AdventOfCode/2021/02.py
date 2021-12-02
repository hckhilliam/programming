def part1(data):
    rows = parse_data(data)
    curr_depth = 0
    curr_h = 0
    for r in rows:
        if r[0] == 'forward':
            curr_h += int(r[1])
        elif r[0] == 'down':
            curr_depth += int(r[1])
        elif r[0] == 'up':
            curr_depth -= int(r[1])
    return curr_depth * curr_h


def part2(data):
    rows = parse_data(data)
    rows = parse_data(data)
    curr_depth = 0
    curr_h = 0
    aim = 0
    for r in rows:
        if r[0] == 'forward':
            curr_h += int(r[1])
            curr_depth += aim * int(r[1])
        elif r[0] == 'down':
            aim += int(r[1])
        elif r[0] == 'up':
            aim -= int(r[1])
    return curr_depth * curr_h


def parse_data(data):
    rows = data.split('\n')
    return [row.split(' ') for row in rows]
