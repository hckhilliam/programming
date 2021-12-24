from collections import defaultdict, deque
import functools
import math
import re


class Cube(object):
    def __init__(self, on, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.volume = (
            (self.x2 - self.x1 + 1) *
            (self.y2 - self.y1 + 1) *
            (self.z2 - self.z1 + 1)
        )
        self.on = on


def part1(data):
    cubes = parse_data(data)
    cubes_in_range = []
    for c in cubes:
        if (
            c.x2 < -50 or c.x1 > 50 or
            c.y2 < -50 or c.y2 > 50 or
            c.z2 < -50 or c.z2 > 50
        ):
            continue
        c.x1 = clip(c.x1)
        c.x2 = clip(c.x2)
        c.y1 = clip(c.y1)
        c.y2 = clip(c.y2)
        c.z1 = clip(c.z1)
        c.z2 = clip(c.z2)
        cubes_in_range.append(c)
    return find_deduped_volume(cubes_in_range)


def clip(p):
    if p < -50:
        return -50
    elif p > 50:
        return 50
    return p


def part2(data):
    cubes = parse_data(data)
    return find_deduped_volume(cubes)


def find_deduped_volume(cubes):
    done_cubes = []
    volume = 0
    for i in range(len(cubes) - 1, -1, -1):
        if cubes[i].on:
            volume += get_new_volume(cubes[i], done_cubes)
        done_cubes.append(cubes[i])
    return volume


def get_new_volume(cube, done_cubes):
    volume = cube.volume

    overlaps = []
    for c in done_cubes:
        overlap = find_overlap(cube, c)
        if overlap:
            overlaps.append(overlap)
    return volume - find_deduped_volume(overlaps)


def find_overlap(cube1, cube2):
    x1, x2 = get_range(cube1.x1, cube1.x2, cube2.x1, cube2.x2)
    if not is_valid(x1, x2):
        return None
    y1, y2 = get_range(cube1.y1, cube1.y2, cube2.y1, cube2.y2)
    if not is_valid(y1, y2):
        return None
    z1, z2 = get_range(cube1.z1, cube1.z2, cube2.z1, cube2.z2)
    if not is_valid(z1, z2):
        return None
    return Cube(on=True, x1=x1, x2=x2, y1=y1, y2=y2, z1=z1, z2=z2)


def get_range(x11, x12, x21, x22):
    return max(x11, x21), min(x12, x22)


def is_valid(p1, p2):
    return p1 <= p2


def parse_data(data):
    rows = data.split('\n')
    actions = []
    for r in rows:
        action, ranges = r.split(' ')
        x, y, z = ranges.split(',')
        x1, x2 = [int(xx) for xx in x[2:].split('..')]
        y1, y2 = [int(yy) for yy in y[2:].split('..')]
        z1, z2 = [int(zz) for zz in z[2:].split('..')]
        actions.append(
            Cube(
                on=action == 'on',
                x1=x1, x2=x2, y1=y1, y2=y2, z1=z1, z2=z2,
            )
        )
    return actions
