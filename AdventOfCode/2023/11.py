from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    space = [list(r) for r in rows]
    new_space = []
    for r in space:
        if all_empty(r):
            new_space.append(['.' for _ in range(len(r))])
        new_space.append(r)
    space = new_space

    new_space = [[] for _ in range(len(space))]
    for x in range(len(space[0])):
        empty = True
        for y in range(len(space)):
            if space[y][x] != '.':
                empty = False
                break

        if empty:
            for y in range(len(space)):
                new_space[y].append(space[y][x])
                new_space[y].append(space[y][x])
        else:
            for y in range(len(space)):
                new_space[y].append(space[y][x])

    space = new_space
    galaxies = list()
    for y in range(len(space)):
        for x in range(len(space[y])):
            c = space[y][x]
            if c == '#':
                galaxies.append((x, y))

    all_distances = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            all_distances += get_distance(galaxies[i], galaxies[j])
    return all_distances


def get_distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def all_empty(row):
    for r in row:
        if r != '.':
            return False
    return True


def part2(data):
    rows = parse_data(data)
    space = [list(r) for r in rows]
    for r in space:
        if all_empty(r):
            for x in range(len(r)):
                r[x] = 'E'

    for x in range(len(space[0])):
        empty = True
        for y in range(len(space)):
            if space[y][x] not in {'.', 'E'}:
                empty = False
                break

        if empty:
            for y in range(len(space)):
                space[y][x] = 'E'

    galaxies = list()
    for y in range(len(space)):
        for x in range(len(space[y])):
            c = space[y][x]
            if c == '#':
                galaxies.append((x, y))

    all_distances = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            all_distances += get_distance2(galaxies[i], galaxies[j], space)
    return all_distances


def get_distance2(g1, g2, space):
    stepX = 1 if g1[0] < g2[0] else -1
    stepY = 1 if g1[1] < g2[1] else -1

    steps = 0
    while g1[0] != g2[0]:
        g1 = (g1[0] + stepX, g1[1])
        if space[g1[1]][g1[0]] == 'E':
            steps += 1000000
        else:
            steps += 1
    while g1[1] != g2[1]:
        g1 = (g1[0], g1[1] + stepY)
        if space[g1[1]][g1[0]] == 'E':
            steps += 1000000
        else:
            steps += 1
    return steps


def parse_data(data):
    rows = data.split('\n')
    return rows
