from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, in_bounds
import sys

debug = False


def part1(data):
    rows = parse_data(data)
    rows = [[int(c) for c in r] for r in rows]

    return find_min_heat_loss(rows, min_steps=0, max_steps=3)


def print_map(rows):
    for x in range(len(rows[0])):
        print(f'\t{x}', end='')
    print()
    for y in range(len(rows)):
        st = f'{y}\t'
        for x in range(len(rows[y])):
            st += f'{rows[y][x]}\t'
        print(st)
    print()


def find_min_heat_loss(rows, min_steps, max_steps):
    cache = {}
    lastX = len(rows[0]) - 1
    lastY = len(rows) - 1
    pq = [
        ((rows[lastY][lastX], (lastX, lastY), (-1, 0), max_steps)),
        ((rows[lastY][lastX], (lastX, lastY), (0, -1), max_steps))
    ]

    while pq:
        heat_loss, start, dir, steps = heapq.heappop(pq)
        if start == (0, 0):
            if debug:
                print_map(rows)
            return heat_loss - rows[0][0]

        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            newX = start[0] + d[0]
            newY = start[1] + d[1]
            p = (newX, newY)
            if not in_bounds(p, rows) or d == (-dir[0], -dir[1]):
                continue

            newSteps = 1
            if d == dir:
                if steps >= max_steps:
                    continue
                newSteps = steps + 1
                newHeatLoss = heat_loss + rows[newY][newX]
            else:
                newSteps = min_steps
                newHeatLoss = heat_loss
                newHeatLoss += rows[newY][newX]
                failed = False
                for _ in range(min_steps - 1):
                    newX = newX + d[0]
                    newY = newY + d[1]
                    p = (newX, newY)
                    if not in_bounds(p, rows):
                        failed = True
                        break
                    newHeatLoss += rows[newY][newX]
                if failed:
                    continue

            if (p, d, newSteps) in cache:
                continue

            # Guaranteed min from PQ.
            cache[(p, d, newSteps)] = newHeatLoss
            heapq.heappush(pq, (newHeatLoss, p, d, newSteps))
    return sys.maxsize


def part2(data):
    rows = parse_data(data)
    rows = [[int(c) for c in r] for r in rows]

    return find_min_heat_loss(rows, min_steps=4, max_steps=10)


def parse_data(data):
    rows = data.split('\n')
    return rows
