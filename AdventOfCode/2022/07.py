from collections import defaultdict, deque
import functools
import math
import re


class Directory(object):
    def __init__(self, name, parent, total_size=0):
        self.name = name
        self.parent = parent
        self.children = {}
        self.total_size = total_size


def calculate_total_sizes(root):
    for v in root.children.values():
        calculate_total_sizes(v)
        root.total_size += v.total_size


def parse_tree(rows):
    root = Directory('/', None)
    curr_dir = root
    i = 1
    while i < len(rows):
        r = rows[i]
        if r == '$ ls':
            i += 1
            while i < len(rows) and not rows[i].startswith('$'):
                p1, p2 = rows[i].split(' ')
                if p1 == 'dir':
                    curr_dir.children[p2] = Directory(p2, curr_dir)
                else:
                    curr_dir.children[p2] = Directory(p2, curr_dir, int(p1))
                i += 1
        else:
            move = r.split(' ')[-1]
            if move == '..':
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.children[move]
            i += 1

    calculate_total_sizes(root)
    return root


def part1(data):
    rows = parse_data(data)
    root = parse_tree(rows)

    total_sizes = 0
    q = [root]
    while q:
        d = q.pop()
        if d.total_size <= 100000:
            total_sizes += d.total_size

        for c in d.children.values():
            if c.children:
                q.append(c)
    return total_sizes


def part2(data):
    rows = parse_data(data)
    root = parse_tree(rows)

    free = 70000000 - root.total_size
    needed = 30000000 - free

    min_d = 70000000
    q = [root]
    while q:
        d = q.pop()
        if d.total_size >= needed:
            min_d = min(d.total_size, min_d)

        for c in d.children.values():
            if c.children:
                q.append(c)

    return min_d


def parse_data(data):
    rows = data.split('\n')
    return rows
