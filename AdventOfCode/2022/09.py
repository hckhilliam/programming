from collections import defaultdict, deque
import functools
import math
import re
import numpy as np


def parse(r):
    command, n = r.split(' ')
    if command == 'L':
        return (-1, 0), int(n)
    elif command == 'U':
        return (0, 1), int(n)
    elif command == 'D':
        return (0, -1), int(n)
    else:
        return (1, 0), int(n)


def move_tail(h, t):
    x_diff = h[0] - t[0]
    y_diff = h[1] - t[1]
    new_x = t[0]
    new_y = t[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        new_x += np.sign(x_diff)
        new_y += np.sign(y_diff)

    return (new_x, new_y)


def part1(data):
    rows = parse_data(data)

    init = (0, 0)
    visited = {init}

    h = init
    t = init
    for r in rows:
        d, n = parse(r)

        for _ in range(n):
            h = (h[0] + d[0], h[1] + d[1])
            t = move_tail(h, t)
            if t not in visited:
                visited.add(t)

    return len(visited)



def part2(data):
    rows = parse_data(data)

    init = (0, 0)
    visited = {init}

    h = init
    ts = [init for _ in range(9)]
    for r in rows:
        d, n = parse(r)

        for _ in range(n):
            h = (h[0] + d[0], h[1] + d[1])
            curr_h = h
            for i, t in enumerate(ts):
                ts[i] = move_tail(curr_h, t)
                curr_h = ts[i]
            if curr_h not in visited:
                visited.add(curr_h)

    return len(visited)


def parse_data(data):
    rows = data.split('\n')
    return rows
