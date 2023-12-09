from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    total = 0
    for row in rows:
        values = [int(r) for r in row.split(' ')]
        last_nums = [values[-1]]
        while not all_zeroes(values):
            new_arr = []
            left = values[0]
            for v in values[1:]:
                new_arr.append(v - left)
                left = v
            last_nums.append(new_arr[-1])
            values = new_arr
        new_val = last_nums[-1]
        for i in range(len(last_nums) - 2, -1, -1):
            new_val = new_val + last_nums[i]
        total += new_val
    return total


def all_zeroes(values):
    for v in values:
        if v != 0:
            return False
    return True


def part2(data):
    rows = parse_data(data)
    total = 0
    for row in rows:
        values = [int(r) for r in row.split(' ')]
        first_nums = [values[0]]
        while not all_zeroes(values):
            new_arr = []
            left = values[0]
            for v in values[1:]:
                new_arr.append(v - left)
                left = v
            first_nums.append(new_arr[0])
            values = new_arr
        new_val = first_nums[-1]
        for i in range(len(first_nums) - 2, -1, -1):
            new_val = first_nums[i] - new_val
        total += new_val
    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
