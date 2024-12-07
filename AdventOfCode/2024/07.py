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

    total_calibration = 0
    for r in rows:
        test, nums = r.split(':')
        test = int(test)
        nums = [int(n) for n in nums.strip().split(' ')]
        if solveable(test, nums, 1, nums[0]):
            total_calibration += test
    return total_calibration


def solveable(test, nums, start, running_total):
    if running_total > test:
        return False

    if start == len(nums):
        return test == running_total

    return (solveable(test, nums, start + 1, running_total + nums[start]) or
            solveable(test, nums, start + 1, running_total * nums[start]))


def part2(data):
    rows = parse_data(data)

    total_calibration = 0
    for r in rows:
        test, nums = r.split(':')
        test = int(test)
        nums = [int(n) for n in nums.strip().split(' ')]
        if solveable2(test, nums, 1, nums[0]):
            total_calibration += test
    return total_calibration


def solveable2(test, nums, start, running_total):
    if running_total > test:
        return False

    if start == len(nums):
        return test == running_total

    return (solveable2(test, nums, start + 1, running_total + nums[start]) or
            solveable2(test, nums, start + 1, running_total * nums[start]) or
            solveable2(test, nums, start + 1, int(str(running_total) + str(nums[start]))))


def parse_data(data):
    rows = data.split('\n')
    return rows
