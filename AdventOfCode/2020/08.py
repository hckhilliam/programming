from collections import defaultdict
import functools
import math


def part1(data):
    rows = parse_data(data)
    return test(rows)[0]


def part2(data):
    rows = parse_data(data)
    for i in range(len(rows)):
        dupe = list(rows)
        p = rows[i].split(' ')
        op = p[0]
        if op == 'jmp':
            dupe[i] = ' '.join(['nop', p[1]])
        elif op == 'nop':
            dupe[i] = ' '.join(['jmp', p[1]])
        v, terminate = test(dupe)
        if terminate:
            return v
    return None


def test(rows):
    v = set()
    i = 0
    total = 0
    while i not in v and i < len(rows):
        v.add(i)
        p = rows[i].split(' ')
        op = p[0]
        num = p[1]
        s = num[0]
        num = int(num[1:])
        if s == '-':
            num *= -1
        if op == 'acc':
            total += num

        elif op == 'jmp':
            i += num
            continue
        i += 1
    return total, i >= len(rows)


def parse_data(data):
    rows = data.split('\n')
    return rows
