class P(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return str(self.x) + ', ' + str(self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError


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


O_DIRS = [P(1, 0), P(0, 1), P(-1, 0), P(0, -1)]
DIRS = [P(-1, -1), P(-1, 0), P(-1, 1), P(0, -1), P(0, 1), P(1, -1), P(1, 0), P(1, 1)]
