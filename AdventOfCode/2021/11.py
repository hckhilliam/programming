from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    total_flashes = 0
    for _ in range(100):
        for i, r in enumerate(rows):
            for j, e in enumerate(r):
                if e >= 10:
                    continue

                rows[i][j] += 1
                if rows[i][j] == 10:
                    flash_around(i, j, rows)

        for i, r in enumerate(rows):
            for j, e in enumerate(r):
                if e >= 10:
                    rows[i][j] = 0
                    total_flashes += 1
    return total_flashes


def flash_around(i, j, rows):
    for i2 in range(i - 1, i + 2):
        for j2 in range(j - 1, j + 2):
            if i2 == i and j2 == j:
                continue
            if in_bounds(i2, j2, rows):
                rows[i2][j2] += 1
                if rows[i2][j2] == 10:
                    flash_around(i2, j2, rows)


def in_bounds(i, j, rows):
    return i >= 0 and j >= 0 and i < len(rows) and j < len(rows[0]) and rows[i][j] < 10


def part2(data):
    rows = parse_data(data)

    s = 1
    while True:
        for i, r in enumerate(rows):
            for j, e in enumerate(r):
                if e >= 10:
                    continue

                rows[i][j] += 1
                if rows[i][j] == 10:
                    flash_around(i, j, rows)
        all_flash = True
        for i, r in enumerate(rows):
            for j, e in enumerate(r):
                if e >= 10:
                    rows[i][j] = 0
                else:
                    all_flash = False
        if all_flash:
            return s
        s += 1


def parse_data(data):
    rows = data.split('\n')
    energies = []
    for r in rows:
        energies.append([int(e) for e in r])
    return energies
