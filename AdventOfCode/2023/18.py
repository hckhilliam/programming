from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array
import sys

debug = False


def part1(data):
    rows = parse_data(data)
    minX = sys.maxsize
    minY = sys.maxsize
    maxX = 0
    maxY = 0
    dug = set()
    currX = 0
    currY = 0
    for r in rows:
        dir, n, _ = r.split(' ')
        n = int(n)

        d = None
        if dir == 'R':
            d = (1, 0)
        elif dir == 'L':
            d = (-1, 0)
        elif dir == 'U':
            d = (0, -1)
        elif dir == 'D':
            d = (0, 1)

        for _ in range(n):
            currX += d[0]
            currY += d[1]
            dug.add((currX, currY))
        maxX = max(maxX, currX)
        maxY = max(maxY, currY)
        minX = min(minX, currX)
        minY = min(minY, currY)
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) not in dug:
                success = dig((x, y), dug, minX, minY, maxX, maxY)
                if success:
                    return len(dug)
    print('bad')
    return 0


def dig(p, dug, minX, minY, maxX, maxY):
    copy_dug = dug.copy()
    q = deque([p])
    while q:
        curr = q.popleft()
        if curr in copy_dug:
            continue
        copy_dug.add(curr)

        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = curr[0] + d[0]
            new_y = curr[1] + d[1]
            if not in_bounds(new_x, new_y, minX, minY, maxX, maxY):
                return False

            if (new_x, new_y) not in copy_dug:
                q.append((new_x, new_y))

    for k in copy_dug:
        dug.add(k)
    return True


def in_bounds(x, y, minX, minY, maxX, maxY):
    return x >= minX and x <= maxX and y >= minY and y <= maxY


def part2(data):
    rows = parse_data(data)
    curr_corner = (0, 0)
    points = [curr_corner]
    for r in rows:
        _, _, hex = r.split(' ')

        dir = hex[-2]
        d = None
        if dir == '0':
            d = (1, 0)
        elif dir == '2':
            d = (-1, 0)
        elif dir == '3':
            d = (0, -1)
        elif dir == '1':
            d = (0, 1)
        hex = hex[1:-2].replace('#', '0x')
        n = int(hex, 16)
        curr_corner = (curr_corner[0] + d[0] * n, curr_corner[1] + d[1] * n)
        points.append(curr_corner)

    points.append((0, 0))
    return get_lava(points)


# Shoelace + Pick's theorem.
def get_lava(points):
    total_area = 0
    total_perimeter = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        total_area += x1 * y2 - x2 * y1
        total_perimeter += abs(x2 - x1) + abs(y2 - y1)
    return total_area // 2 + total_perimeter // 2 + 1


def parse_data(data):
    rows = data.split('\n')
    return rows
