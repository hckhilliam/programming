from collections import defaultdict
import functools
import math


def part1(data):
    rows = parse_data(data)
    t = []
    for r in rows:
        t.append([c for c in r])
    change = True
    occ = 0
    while change:
        change = False
        dupe = [list(r) for r in t]
        occ = 0
        for i in range(len(t)):
            for j in range(len(t[i])):
                c = t[i][j]
                num_occ = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (
                            not (k == 0 and l == 0)
                            and i + k >= 0
                            and i + k < len(t)
                            and j + l >= 0
                            and j + l < len(t[i + k])
                            and t[i + k][j + l] == '#'
                        ):
                            num_occ += 1
                if c == '#' and num_occ >= 4:
                    dupe[i][j] = 'L'
                    change = True
                elif c == 'L' and num_occ == 0:
                    dupe[i][j] = '#'
                    change = True
                if c == '#':
                    occ += 1
        t = dupe
    return occ


def part2(data):
    rows = parse_data(data)
    t = []
    for r in rows:
        t.append([c for c in r])
    change = True
    occ = 0
    while change:
        change = False
        dupe = [list(r) for r in t]
        occ = 0
        for i in range(len(t)):
            for j in range(len(t[i])):
                c = t[i][j]
                num_occ = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if not (k == 0 and l == 0):
                            num_occ += find_seat(t, i, j, k, l)
                if c == '#' and num_occ >= 5:
                    dupe[i][j] = 'L'
                    change = True
                elif c == 'L' and num_occ == 0:
                    dupe[i][j] = '#'
                    change = True
                if c == '#':
                    occ += 1
        t = dupe
    return occ


def find_seat(t, i, j, dx, dy):
    k = dx
    l = dy
    while i + k >= 0 and i + k < len(t) and j + l >= 0 and j + l < len(t[i + k]):
        if t[i + k][j + l] == '#':
            return 1
        elif t[i + k][j + l] == 'L':
            return 0
        k += dx
        l += dy
    return 0


def parse_data(data):
    rows = data.split('\n')
    return rows
