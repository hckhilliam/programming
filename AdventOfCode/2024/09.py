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
    data = rows[0]

    id = 0
    ind = 0
    files = []
    spaces = []
    for i, d in enumerate(data):
        n = int(d)
        if i % 2 == 0:
            files.append((id, ind, n))
            id += 1
        else:
            spaces.append((ind, n))
        ind += n

    s = 0
    f = len(files) - 1
    compacted = []
    while s < len(spaces):
        space_ind, space_size = spaces[s]
        file_id, file_ind, file_size = files[f]
        if file_ind < space_ind:
            break

        if space_size > file_size:
            compacted.append((file_id, space_ind, file_size))
            spaces[s] = (space_ind + file_size, space_size - file_size)
            f -= 1
        elif file_size > space_size:
            compacted.append((file_id, space_ind, space_size))
            files[f] = (file_id, file_ind, file_size - space_size)
            s += 1
        else:
            compacted.append((file_id, space_ind, space_size))
            s += 1
            f -= 1

    while f >= 0:
        compacted.append(files[f])
        f -= 1

    checksum = 0
    for c in compacted:
        checksum += c[0] * sum([c[1] + i for i in range(c[2])])
    return checksum


def part2(data):
    rows = parse_data(data)
    data = rows[0]

    id = 0
    ind = 0
    files = []
    spaces = []
    for i, d in enumerate(data):
        n = int(d)
        if i % 2 == 0:
            files.append((id, ind, n))
            id += 1
        else:
            spaces.append((ind, n))
        ind += n

    space_heaps = defaultdict(list)
    for i, size in spaces:
        heapq.heappush(space_heaps[size], i)

    compacted = []
    for f in range(len(files) - 1, -1, -1):
        file_id, file_ind, file_size = files[f]
        min_ind = sys.maxsize
        space_size = 0
        for s in range(file_size, 10):
            h = space_heaps[s]
            if len(h) and h[0] < min_ind:
                min_ind = h[0]
                space_size = s
        if min_ind < sys.maxsize and min_ind < file_ind:
            heapq.heappop(space_heaps[space_size])
            compacted.append((file_id, min_ind, file_size))
            heapq.heappush(space_heaps[space_size - file_size], min_ind + file_size)
        else:
            compacted.append((file_id, file_ind, file_size))

    checksum = 0
    for c in compacted:
        checksum += c[0] * sum([c[1] + i for i in range(c[2])])
    return checksum


def parse_data(data):
    rows = data.split('\n')
    return rows
