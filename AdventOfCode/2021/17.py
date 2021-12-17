from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    _, y_range = parse_data(data)
    max_yv = abs(y_range[0]) - 1
    return max_yv * (max_yv + 1) / 2


def part2(data):
    x_range, y_range = parse_data(data)
    min_x_v = math.ceil((-1 + math.sqrt(1 - 4 * x_range[0] * (-2))) / 2)

    total = 0
    for x in range(min_x_v, x_range[1] + 1):
        for y in range(y_range[0], abs(y_range[0])):
            if hits_box(x, y, x_range, y_range):
                total += 1
    return total


def hits_box(x, y, x_range, y_range):
    curr_x = x
    curr_y = y
    while curr_x <= x_range[1] and curr_y >= y_range[0]:
        if x_range[0] <= curr_x <= x_range[1] and y_range[0] <= curr_y <= y_range[1]:
            return True
        if x > 0:
            x -= 1
        y -= 1
        curr_x += x
        curr_y += y
    return False


def parse_data(data):
    xy_range = data[data.find('x='):].split(', ')
    x_range = ([int(p) for p in xy_range[0][2:].split('..')])
    y_range = ([int(p) for p in xy_range[1][2:].split('..')])
    return (x_range, y_range)
