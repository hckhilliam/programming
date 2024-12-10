def to_array(rows):
    return [list(r) for r in rows]


def to_int_array(rows):
    return [[int(d) for d in list(r)] for r in rows]


def p_rows(rows):
    for r in rows:
        print(''.join(r))
    print()


def in_bounds(p, rows):
    x, y = p
    return y >= 0 and y < len(rows) and x >= 0 and x < len(rows[y])
