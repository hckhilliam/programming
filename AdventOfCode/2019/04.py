from collections import defaultdict
import functools
import math


def part1(data):
    valid = 0
    for i in range(172930, 683082):
        double = False
        p = str(i)
        c1 = p[0]
        v = True
        for j in range(1, len(p)):
            if p[j] == c1:
                double = True
            elif p[j] < c1:
                v = False
                break
            c1 = p[j]
        if double and v:
            valid += 1
    return valid


def part2(data):
    valid = 0
    for i in range(172930, 683082):
        double = False
        dcnt = 1
        p = str(i)
        c1 = p[0]
        v = True
        for j in range(1, len(p)):
            if p[j] == c1:
                dcnt += 1
            elif p[j] < c1:
                v = False
                break
            else:
                if dcnt == 2:
                    double = True
                dcnt = 1
            c1 = p[j]
        if dcnt == 2:
            double = True
        if double and v:
            valid += 1
    return valid
