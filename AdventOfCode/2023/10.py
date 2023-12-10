from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    x, y = None, None
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == 'S':
                y = i
                x = j
                break
        if y:
            break

    loop_size = 0
    if in_bounds(x + 1, y, rows) and rows[y][x + 1] in {'-', 'J', '7'}:
        loop_size = get_loop_size(rows, (x + 1, y), (x, y))
    elif in_bounds(x - 1, y, rows) and rows[y][x - 1] in {'-', 'L', 'F'}:
        loop_size = get_loop_size(rows, (x - 1, y), (x, y))
    elif in_bounds(x, y + 1, rows) and rows[y + 1][x] in {'|', 'L', 'J'}:
        loop_size = get_loop_size(rows, (x, y + 1), (x, y))
    elif in_bounds(x, y - 1, rows) and rows[y - 1][x] in {'|', '7', 'F'}:
        loop_size = get_loop_size(rows, (x, y - 1), (x, y))
    return math.ceil(loop_size / 2)


def in_bounds(x, y, rows):
    return x >= 0 and x < len(rows[0]) and y >= 0 and y < len(rows)


def get_loop_size(rows, curr, prev):
    steps = 1
    while True:
        p = rows[curr[1]][curr[0]]
        if p == 'S':
            return steps
        next = None
        if p == '|':
            if prev[1] > curr[1]:
                next = (curr[0], curr[1] - 1)
            else:
                next = (curr[0], curr[1] + 1)
        elif p == '-':
            if prev[0] > curr[0]:
                next = (curr[0] - 1, curr[1])
            else:
                next = (curr[0] + 1, curr[1])
        elif p == 'L':
            if prev[1] < curr[1]:
                next = (curr[0] + 1, curr[1])
            else:
                next = (curr[0], curr[1] - 1)
        elif p == 'J':
            if prev[1] < curr[1]:
                next = (curr[0] - 1, curr[1])
            else:
                next = (curr[0], curr[1] - 1)
        elif p == '7':
            if prev[1] > curr[1]:
                next = (curr[0] - 1, curr[1])
            else:
                next = (curr[0], curr[1] + 1)
        elif p == 'F':
            if prev[1] > curr[1]:
                next = (curr[0] + 1, curr[1])
            else:
                next = (curr[0], curr[1] + 1)
        prev = curr
        curr = next
        steps += 1


def part2(data):
    rows = parse_data(data)
    array_rows = []
    for r in rows:
        new_row = [r[0]]
        for c in r[1:]:
            new_row.append(c)
            new_row.append('o')
        new_row.pop()
        array_rows.append(new_row)
        array_rows.append(['o' for _ in range(len(new_row))])
    array_rows.pop()

    x, y = None, None
    for i in range(len(rows)):
        for j in range(len(array_rows[i])):
            if array_rows[i][j] == 'S':
                y = i
                x = j
                break
        if y:
            break

    if in_bounds(x + 2, y, array_rows) and array_rows[y][x + 2] in {'-', 'J', '7'}:
        array_rows[y][x + 1] = 'X'
        enclose_loop(array_rows, (x + 2, y), (x, y))
    elif in_bounds(x - 2, y, array_rows) and array_rows[y][x - 2] in {'-', 'L', 'F'}:
        array_rows[y][x - 1] = 'X'
        enclose_loop(array_rows, (x - 2, y), (x, y))
    elif in_bounds(x, y + 2, array_rows) and array_rows[y + 2][x] in {'|', 'L', 'J'}:
        array_rows[y + 1][x] = 'X'
        enclose_loop(array_rows, (x, y + 2), (x, y))
    elif in_bounds(x, y - 2, array_rows) and array_rows[y - 2][x] in {'|', '7', 'F'}:
        array_rows[y - 1][x] = 'X'
        enclose_loop(array_rows, (x, y - 2), (x, y))

    total_enclosed = count_islands(array_rows)
    return total_enclosed


def count_islands(rows):
    total_enclosed = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] not in {'X', 'I', 'O'}:
                total_enclosed += count_island(rows, (x, y))
    return total_enclosed


def count_island(rows, curr):
    copy_rows = [list(r) for r in rows]
    total_enclosed = 0
    q = deque([curr])
    while q:
        curr = q.popleft()
        p = copy_rows[curr[1]][curr[0]]
        if p in {'X', 'I', 'O'}:
            continue
        if p != 'o':
            copy_rows[curr[1]][curr[0]] = 'I'
            total_enclosed += 1
        else:
            copy_rows[curr[1]][curr[0]] = 'O'
        for (y, x) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = curr[0] + x
            new_y = curr[1] + y
            if not in_bounds(new_x, new_y, copy_rows):
                return 0
            if copy_rows[new_y][new_x] not in {'X', 'I', 'O'}:
                q.append((new_x, new_y))
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            rows[y][x] = copy_rows[y][x]
    return total_enclosed


def enclose_loop(rows, curr, prev):
    while True:
        p = rows[curr[1]][curr[0]]
        rows[curr[1]][curr[0]] = 'X'
        if p == 'S':
            return
        next = None
        if p == '|':
            if prev[1] > curr[1]:
                rows[curr[1] - 1][curr[0]] = 'X'
                next = (curr[0], curr[1] - 2)
            else:
                rows[curr[1] + 1][curr[0]] = 'X'
                next = (curr[0], curr[1] + 2)
        elif p == '-':
            if prev[0] > curr[0]:
                rows[curr[1]][curr[0] - 1] = 'X'
                next = (curr[0] - 2, curr[1])
            else:
                rows[curr[1]][curr[0] + 1] = 'X'
                next = (curr[0] + 2, curr[1])
        elif p == 'L':
            if prev[1] < curr[1]:
                rows[curr[1]][curr[0] + 1] = 'X'
                next = (curr[0] + 2, curr[1])
            else:
                rows[curr[1] - 1][curr[0]] = 'X'
                next = (curr[0], curr[1] - 2)
        elif p == 'J':
            if prev[1] < curr[1]:
                rows[curr[1]][curr[0] - 1] = 'X'
                next = (curr[0] - 2, curr[1])
            else:
                rows[curr[1] - 1][curr[0]] = 'X'
                next = (curr[0], curr[1] - 2)
        elif p == '7':
            if prev[1] > curr[1]:
                rows[curr[1]][curr[0] - 1] = 'X'
                next = (curr[0] - 2, curr[1])
            else:
                rows[curr[1] + 1][curr[0]] = 'X'
                next = (curr[0], curr[1] + 2)
        elif p == 'F':
            if prev[1] > curr[1]:
                rows[curr[1]][curr[0] + 1] = 'X'
                next = (curr[0] + 2, curr[1])
            else:
                rows[curr[1] + 1][curr[0]] = 'X'
                next = (curr[0], curr[1] + 2)
        prev = curr
        curr = next


def parse_data(data):
    rows = data.split('\n')
    return rows
