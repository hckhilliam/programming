from collections import defaultdict
import functools
import math
import re
import heapq


def part1(data):
    grid = parse_data(data)
    return find_min_risk(grid)


def find_min_risk(grid):
    d = {}
    end = (len(grid) - 1, len(grid[0]) - 1)
    d[end] = 0
    risk = grid[-1][-1]
    q = []
    heapq.heappush(q, (risk, (end[0], end[1] - 1)))
    heapq.heappush(q, (risk, (end[0] - 1, end[1])))
    while q:
        risk, p = heapq.heappop(q)

        if p not in d:
            d[p] = risk
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_p = (p[0] + i, p[1] + j)
                if new_p not in d and in_bounds(new_p, grid):
                    heapq.heappush(q, (d[p] + grid[p[0]][p[1]], new_p))
    return d[(0, 0)]


def in_bounds(point, grid):
    return point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[0])


def part2(data):
    grid = parse_data(data)
    grid = multiply_grid(grid)
    return find_min_risk(grid)

def find_min_risk(grid):
    d = {}
    end = (len(grid) - 1, len(grid[0]) - 1)
    d[end] = 0
    risk = grid[-1][-1]
    q = []
    heapq.heappush(q, (risk, (end[0], end[1] - 1)))
    heapq.heappush(q, (risk, (end[0] - 1, end[1])))
    while q:
        risk, p = heapq.heappop(q)

        if p not in d:
            d[p] = risk
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_p = (p[0] + i, p[1] + j)
                if new_p not in d and in_bounds(new_p, grid):
                    heapq.heappush(q, (d[p] + grid[p[0]][p[1]], new_p))
    return d[(0, 0)]


def in_bounds(point, grid):
    return point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[0])


def multiply_grid(grid):
    rows = []
    for i in range(5):
        for x in range(len(grid)):
            row = []
            for j in range(5):
                for y in range(len(grid[0])):
                    new_val = grid[x][y] + i + j
                    if new_val >= 10:
                        new_val -= 9
                    row.append(new_val)
            rows.append(row)
    return rows


def parse_data(data):
    rows = data.split('\n')
    grid = []
    for r in rows:
        grid.append([int(i) for i in r])
    return grid
