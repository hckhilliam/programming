def part1(data):
    rows = parse_data(data)
    # Each cycle adds 2 layers
    h = len(rows) + 12
    l = len(rows[0]) + 12
    d = 1 + 12
    midz = 6

    box = []
    for i in range(d):
        grid = []
        for j in range(h):
            grid.append(['.' for k in range(l)])
        box.append(grid)

    # Fill grid with input.
    for i, row in enumerate(rows):
        for j, ch in enumerate(rows[i]):
            box[midz][i + 6][j + 6] = ch

    for cycle in range(6):
        clone_box = []
        for i in range(d):
            clone_grid = []
            for j in range(h):
                clone_row = []
                for k in range(l):
                    active_neighbours = get_active_neighbours(box, i, j, k)
                    if (
                        (box[i][j][k] == '#' and 2 <= active_neighbours <= 3)
                        or (box[i][j][k] == '.' and active_neighbours == 3)
                    ):
                        clone_row.append('#')
                    else:
                        clone_row.append('.')
                clone_grid.append(clone_row)
            clone_box.append(clone_grid)
        box = clone_box

    num_active = 0
    for i in range(d):
        for j in range(h):
            for k in range(l):
                if box[i][j][k] == '#':
                    num_active += 1

    return num_active


def get_active_neighbours(box, i, j, k):
    active_neighbours = 0
    for z in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                newI = i + z
                newJ = j + y
                newK = k + x
                if (
                    (z == 0 and y == 0 and x == 0)
                    or newI < 0 or newI >= len(box)
                    or newJ < 0 or newJ >= len(box[newI])
                    or newK < 0 or newK >= len(box[newI][newJ])
                ):
                    continue
                elif box[newI][newJ][newK] == '#':
                    active_neighbours += 1
    return active_neighbours


def part2(data):
    rows = parse_data(data)
    # Each cycle adds 2 layers
    h = len(rows) + 12
    l = len(rows[0]) + 12
    d = 1 + 12
    fth = 1 + 12
    midz = 6
    midfth = 6

    box = []
    for t in range(fth):
        b = []
        for i in range(d):
            grid = []
            for j in range(h):
                grid.append(['.' for k in range(l)])
            b.append(grid)
        box.append(b)

    # Fill grid with input.
    for i, row in enumerate(rows):
        for j, ch in enumerate(rows[i]):
            box[midfth][midz][i + 6][j + 6] = ch

    for cycle in range(6):
        clone_cont = []
        for t in range(fth):
            clone_box = []
            for i in range(d):
                clone_grid = []
                for j in range(h):
                    clone_row = []
                    for k in range(l):
                        active_neighbours = get_active_neighbours2(box, t, i, j, k)
                        if (
                            (box[t][i][j][k] == '#' and 2 <= active_neighbours <= 3)
                            or (box[t][i][j][k] == '.' and active_neighbours == 3)
                        ):
                            clone_row.append('#')
                        else:
                            clone_row.append('.')
                    clone_grid.append(clone_row)
                clone_box.append(clone_grid)
            clone_cont.append(clone_box)
        box = clone_cont

    num_active = 0
    for t in range(fth):
        for i in range(d):
            for j in range(h):
                for k in range(l):
                    if box[t][i][j][k] == '#':
                        num_active += 1

    return num_active


def get_active_neighbours2(box, t, i, j, k):
    active_neighbours = 0
    for n in range(-1, 2, 1):
        for z in range(-1, 2, 1):
            for y in range(-1, 2, 1):
                for x in range(-1, 2, 1):
                    newT = t + n
                    newI = i + z
                    newJ = j + y
                    newK = k + x
                    if (
                        (n == 0 and z == 0 and y == 0 and x == 0)
                        or newT < 0 or newT >= len(box)
                        or newI < 0 or newI >= len(box[newT])
                        or newJ < 0 or newJ >= len(box[newT][newI])
                        or newK < 0 or newK >= len(box[newT][newI][newJ])
                    ):
                        continue
                    elif box[newT][newI][newJ][newK] == '#':
                        active_neighbours += 1
    return active_neighbours


def parse_data(data):
    rows = data.split('\n')
    return rows
