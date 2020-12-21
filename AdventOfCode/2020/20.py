from collections import defaultdict

TOP = 'top'
RIGHT = 'right'
BOT = 'bot'
LEFT = 'left'

TOP_LEFT = (0, 0)
TOP_RIGHT = (0, -1)
BOT_RIGHT = (-1, -1)
BOT_LEFT = (-1, 0)

LR = (0, 1)
RL = (0, -1)
UB = (1, 0)
BU = (-1, 0)


class ST(object):
    def __init__(self, side, start, delta):
        self.side = side
        self.start = start
        self.delta = delta


dirs = {
    ST(TOP, TOP_LEFT, LR),
    ST(RIGHT, TOP_RIGHT, UB),
    ST(BOT, BOT_LEFT, LR),
    ST(LEFT, TOP_LEFT, UB)
}

COMPARES = [
    ST(TOP, TOP_LEFT, LR),
    ST(TOP, TOP_RIGHT, RL),
    ST(RIGHT, TOP_RIGHT, UB),
    ST(RIGHT, BOT_RIGHT, BU),
    ST(BOT, BOT_LEFT, LR),
    ST(BOT, BOT_RIGHT, RL),
    ST(LEFT, TOP_LEFT, UB),
    ST(LEFT, BOT_LEFT, BU),
]


def part1(data):
    rows = parse_data(data)
    tiles = {}
    dim = len(rows[1])
    i = 0
    while i < len(rows):
        tile = int(rows[i].split(' ')[1][:-1])
        tiles[tile] = rows[i + 1: i + 1 + dim]
        i += 2 + dim

    matches = defaultdict(dict)
    for t, tile in tiles.items():
        for t2, tile2 in tiles.items():
            if t == t2:
                continue

            for d in dirs:
                for c in COMPARES:
                    m = True
                    st1 = d.start
                    st2 = c.start
                    for i in range(dim):
                        if tile[st1[0]][st1[1]] != tile2[st2[0]][st2[1]]:
                            m = False
                            break
                        st1 = (st1[0] + d.delta[0], st1[1] + d.delta[1])
                        st2 = (st2[0] + c.delta[0], st2[1] + c.delta[1])
                    if m:
                        matches[t][d.side] = matches[t].get(d.side, 0) + 1

    ret = 1
    for k, v in matches.items():
        if len(v) == 2:
            ret *= k
    return ret


def part2(data):
    rows = parse_data(data)


def parse_data(data):
    rows = data.split('\n')
    return rows
