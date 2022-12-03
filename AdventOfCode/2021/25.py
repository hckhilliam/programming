from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    sea = parse_data(data)
    step = 0
    still_moving = True
    while still_moving:
        print(step)
        still_moving = False
        new_sea = []
        for i, r in enumerate(sea):
            new_r = [c for c in r]
            for j, c in enumerate(r):
                if c == '>':
                    next_loc = (j + 1) % len(r)
                    if sea[i][next_loc] == '.':
                        new_r[next_loc] = '>'
                        new_r[j] = '.'
                        still_moving = True
            new_sea.append(new_r)

        sea = new_sea
        new_sea = []
        for r in sea:
            new_sea.append([c for c in r])
        for i, r in enumerate(sea):
            for j, c in enumerate(r):
                if c == 'v':
                    next_loc = (i + 1) % len(sea)
                    if sea[next_loc][j] == '.':
                        new_sea[next_loc][j] = 'v'
                        new_sea[i][j] = '.'
                        still_moving = True
        sea = new_sea
        step += 1
    return step


def print_sea(sea):
    for r in sea:
        print(''.join(r))


def part2(data):
    rows = parse_data(data)


def parse_data(data):
    rows = data.split('\n')
    sea = []
    for r in rows:
        sea.append([c for c in r])
    return sea
