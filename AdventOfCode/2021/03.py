from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    gamma = []
    epsilon = []
    curr_bit = 0
    while curr_bit < len(rows[0]):
        zeros = 0
        ones = 0
        for r in rows:
            if r[curr_bit] == '0':
                zeros += 1
            elif r[curr_bit] == '1':
                ones += 1
        if zeros > ones:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
        curr_bit += 1
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part2(data):
    rows = parse_data(data)

    curr_bit = 0
    survived_rows = rows

    o_rating = None
    while curr_bit < len(rows[0]):
        zero_nums = []
        one_nums = []
        zeros = 0
        ones = 0
        for r in survived_rows:
            if r[curr_bit] == '0':
                zeros += 1
                zero_nums.append(r)
            elif r[curr_bit] == '1':
                ones += 1
                one_nums.append(r)
        if zeros > ones:
            survived_rows = zero_nums
        else:
            survived_rows = one_nums
        if len(survived_rows) == 1:
            o_rating = survived_rows[0]
            break
        curr_bit += 1

    curr_bit = 0
    survived_rows = rows
    scrubber_rating = None
    while curr_bit < len(rows[0]):
        zero_nums = []
        one_nums = []
        zeros = 0
        ones = 0
        for r in survived_rows:
            if r[curr_bit] == '0':
                zeros += 1
                zero_nums.append(r)
            elif r[curr_bit] == '1':
                ones += 1
                one_nums.append(r)
        if ones < zeros:
            survived_rows = one_nums
        else:
            survived_rows = zero_nums
        if len(survived_rows) == 1:
            scrubber_rating = survived_rows[0]
            break
        curr_bit += 1

    return int(o_rating, 2) * int(scrubber_rating, 2)


def parse_data(data):
    rows = data.split('\n')
    return rows
