def part1(data):
    rows = parse_data(data)
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # E S W N
    currD = 0
    dx = 0
    dy = 0
    for r in rows:
        d = r[0]
        n = int(r[1:])
        if d == 'N':
            dy += n
        elif d == 'E':
            dx += n
        elif d == 'S':
            dy -= n
        elif d == 'W':
            dx -= n
        elif d == 'F':
            dx += dirs[currD][0] * n
            dy += dirs[currD][1] * n
        elif d == 'L':
            currD = int((currD - (n / 90)) % 4)
        elif d == 'R':
            currD = int((currD + (n / 90)) % 4)
    return abs(dx) + abs(dy)


def part2(data):
    rows = parse_data(data)
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # E S W N
    wayX = 10
    wayY = 1
    dx = 0
    dy = 0
    for r in rows:
        d = r[0]
        n = int(r[1:])
        if d == 'N':
            wayY += n
        elif d == 'E':
            wayX += n
        elif d == 'S':
            wayY -= n
        elif d == 'W':
            wayX -= n
        elif d == 'F':
            dx += wayX * n
            dy += wayY * n
        elif d == 'L':
            for i in range(int((n / 90))):
                t = wayX
                wayX = -wayY
                wayY = t
        elif d == 'R':
            for i in range(int((n / 90))):
                t = wayX
                wayX = wayY
                wayY = -t
    return abs(dx) + abs(dy)


def parse_data(data):
    rows = data.split('\n')
    return rows
