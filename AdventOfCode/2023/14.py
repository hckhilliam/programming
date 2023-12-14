from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    rows = [list(r) for r in rows]

    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c == 'O':
                rows[y][x] = '.'
                yy = y - 1
                while yy >= 0:
                    if rows[yy][x] in {'O', '#'}:
                        break
                    yy -= 1
                rows[yy + 1][x] = 'O'

    total_points = 0
    m = len(rows)
    for y, r in enumerate(rows):
        for c in r:
            if c == 'O':
                total_points += m - y
    return total_points


def part2(data):
    rows = parse_data(data)
    rows = [list(r) for r in rows]

    cache = {}
    cycle = None
    offset = None
    i = 1
    while True:
        run_cycle(rows)
        key = tuple(''.join(r) for r in rows)
        if key in cache:
            cycle = i - cache[key]
            offset = cache[key]
            break
        else:
            cache[key] = i
        i += 1

    final_key = ((1000000000 - offset) % cycle) + offset
    for k, v in cache.items():
        if v == final_key:
            rows = k
            break

    total_points = 0
    m = len(rows)
    for y, r in enumerate(rows):
        for c in r:
            if c == 'O':
                total_points += m - y
    return total_points


def run_cycle(rows):
    # North
    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c == 'O':
                rows[y][x] = '.'
                yy = y - 1
                while yy >= 0:
                    if rows[yy][x] in {'O', '#'}:
                        break
                    yy -= 1
                rows[yy + 1][x] = 'O'

    # West
    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c == 'O':
                rows[y][x] = '.'
                xx = x - 1
                while xx >= 0:
                    if rows[y][xx] in {'O', '#'}:
                        break
                    xx -= 1
                rows[y][xx + 1] = 'O'

    # South
    for y in range(len(rows) - 1, -1, -1):
        r = rows[y]
        for x, c in enumerate(r):
            if c == 'O':
                rows[y][x] = '.'
                yy = y + 1
                while yy < len(rows):
                    if rows[yy][x] in {'O', '#'}:
                        break
                    yy += 1
                rows[yy - 1][x] = 'O'

    # East
    for y, r in enumerate(rows):
        for x in range(len(r) - 1, -1, -1):
            c = r[x]
            if c == 'O':
                rows[y][x] = '.'
                xx = x + 1
                while xx < len(r):
                    if rows[y][xx] in {'O', '#'}:
                        break
                    xx += 1
                rows[y][xx - 1] = 'O'


def parse_data(data):
    rows = data.split('\n')
    return rows
