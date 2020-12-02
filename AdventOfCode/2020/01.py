
from collections import defaultdict

def part1(data):
    return two_sum(2020, data)


def part2(data):
    return three_sum(2020, data)


def two_sum(target, inp=None, hashed=None):
    if not hashed:
        hashed = build_dict(inp)
    for k in hashed:
        other = target - k
        if (other == k and hashed[k] > 1) or hashed.get(other):
            return other * k
    return -1


def three_sum(target, inp):
    hashed = build_dict(inp)
    for k in hashed:
        hashed[k] -= 1
        res = two_sum(target - k, hashed=hashed)
        if res > 0:
            return res * k
    return -1


def build_dict(inp):
    hashed = defaultdict(int)
    for i in inp.split('\n'):
        hashed[int(i)] += 1
    return hashed
