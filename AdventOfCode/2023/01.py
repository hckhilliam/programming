from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    sum = 0
    for row in rows:
        total = ''
        for c in row:
            if '0' <= c <= '9':
                total += c
                break
        for c in row[::-1]:
            if '0' <= c <= '9':
                total += c
                break
        sum += int(total)
    return sum



def part2(data):
    rows = parse_data(data)

    number_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    sum = 0
    for row in rows:
        total = ''
        for i, c in enumerate(row):
            if '0' <= c <= '9':
                total += c
                break
            found = False
            for k, v in number_map.items():
                if (row[i:].startswith(k)):
                    total += v
                    found = True
                    break
            if found:
                break
        for i in range(len(row) - 1, -1, -1):
            c = row[i]
            if '0' <= c <= '9':
                total += c
                break
            found = False
            for k, v in number_map.items():
                if (row[i:].startswith(k)):
                    total += v
                    found = True
                    break
            if found:
                break
        sum += int(total)
    return sum

def parse_data(data):
    rows = data.split('\n')
    return rows
