def part1(data):
    rows = parse_data(data)

    dm = {
        's': (0, -1),
        'n': (0, 1),
        'e': (1, 0),
        'w': (-1, 0)
    }

    flips = set()
    for r in rows:
        i = 0
        p = (0, 0)
        while i < len(r):
            move = dm[r[i]]
            p = (p[0] + move[0], p[1] + move[1])
            if r[i] == 's' or r[i] == 'n':
                move2 = dm[r[i + 1]]
                p = (p[0] + move2[0] * 0.5, p[1] + move2[1] * 0.5)
                i += 1
            i += 1
        if p in flips:
            flips.remove(p)
        else:
            flips.add(p)
    return len(flips)


DIRS = [(1, 0), (-1, 0), (0.5, 1), (0.5, -1), (-0.5, 1), (-0.5, -1)]


def part2(data):
    rows = parse_data(data)

    dm = {
        's': (0, -1),
        'n': (0, 1),
        'e': (1, 0),
        'w': (-1, 0)
    }

    flips = set()
    for r in rows:
        i = 0
        p = (0, 0)
        while i < len(r):
            move = dm[r[i]]
            p = (p[0] + move[0], p[1] + move[1])
            if r[i] == 's' or r[i] == 'n':
                move2 = dm[r[i + 1]]
                p = (p[0] + move2[0] * 0.5, p[1] + move2[1] * 0.5)
                i += 1
            i += 1
        if p in flips:
            flips.remove(p)
        else:
            flips.add(p)

    for i in range(100):
        new_flips = set()
        v = set()
        for f in flips:
            maybe_flip(f, flips, new_flips, is_black=True)
            for d in DIRS:
                p = (f[0] + d[0], f[1] + d[1])
                if p not in flips and p not in v:
                    maybe_flip(p, flips, new_flips, is_black=False)
                    v.add(p)
        flips = new_flips

    return len(flips)


def maybe_flip(p, flips, new_flips, is_black):
    blacks = 0
    for d in DIRS:
        if (p[0] + d[0], p[1] + d[1]) in flips:
            blacks += 1

    if is_black and not (blacks == 0 or blacks > 2):
        new_flips.add(p)
    elif not is_black and blacks == 2:
        new_flips.add(p)


def parse_data(data):
    rows = data.split('\n')
    return rows
