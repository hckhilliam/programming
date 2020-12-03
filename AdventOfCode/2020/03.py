def part1(data):
    rows = parse_data(data)
    return solve_1(rows, 3, 1)


def part2(data):
    rows = parse_data(data)
    params = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for jx, jy in params:
        total *= solve_1(rows, jx, jy)
    return total


def solve_1(rows, jump_x, jump_y):
    num_trees = 0
    x = 0
    y = 0
    while y < len(rows):
        y += jump_y
        x = (x + jump_x) % len(rows[0])
        if y < len(rows) and rows[y][x] == '#':
            num_trees += 1
    return num_trees


def parse_data(data):
    rows = data.split('\n')
    return rows
