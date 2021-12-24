from collections import defaultdict, deque
import functools
import math
import re
import sys


# Can stop here.
ALLOWED_HALLWAY_POS = {
    (1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 11)
}

KEY_TO_ENERGY = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}


def part1(data):
    grid, grids = parse_data(data)
    available_pos = get_available_pos(grid)
    next_homes = {
        'A': [(3, 3), (2, 3)],
        'B': [(3, 5), (2, 5)],
        'C': [(3, 7), (2, 7)],
        'D': [(3, 9), (2, 9)]
    }
    nexts = [
        {'key': 'A', 'value': 0},
        {'key': 'B', 'value': 0},
        {'key': 'C', 'value': 0},
        {'key': 'D', 'value': 0},
    ]
    for n in nexts:
        key = n['key']
        value = n['value']
        while value <= 1:
            p = next_homes[key][value]
            if grid[p[0]][p[1]] == key:
                value += 1
                n['value'] += value
            else:
                break

    return find_min_organization_energy(grid, nexts, available_pos, next_homes, dict(), grids)


def part2(data):
    grid, grids = parse_data(data)
    # Add the extra rows
    grid = (
        grid[:3] +
        [
            [c for c in '  #D#C#B#A#'],
            [c for c in '  #D#B#A#C#']
        ] +
        grid[3:]
    )

    available_pos = get_available_pos(grid)
    next_homes = {
        'A': [(5, 3), (4, 3), (3, 3), (2, 3)],
        'B': [(5, 5), (4, 5), (3, 5), (2, 5)],
        'C': [(5, 7), (4, 7), (3, 7), (2, 7)],
        'D': [(5, 9), (4, 9), (3, 9), (2, 9)]
    }
    nexts = [
        {'key': 'A', 'value': 0},
        {'key': 'B', 'value': 0},
        {'key': 'C', 'value': 0},
        {'key': 'D', 'value': 0},
    ]
    for n in nexts:
        key = n['key']
        value = n['value']
        while value <= 1:
            p = next_homes[key][value]
            if grid[p[0]][p[1]] == key:
                value += 1
                n['value'] += value
            else:
                break

    return find_min_organization_energy(grid, nexts, available_pos, next_homes, dict(), grids)


def get_available_pos(grid):
    available_pos = set()
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c in {'.', 'A', 'B', 'C', 'D'}:
                available_pos.add((i, j))
    return available_pos


def find_min_organization_energy(grid, nexts, available_pos, next_homes, cache, grids):
    cache_key = get_cache_key(grid)
    if cache_key in cache:
        return cache[cache_key]

    grid = [r[:] for r in grid]
    nexts = [n.copy() for n in nexts]
    energy_used = 0
    positions = get_positions(grid, available_pos, next_homes)

    # See if we can go to any available home.
    for i in range(len(nexts) - 1, -1, -1):
        n = nexts[i]
        key = n['key']
        value = n['value']
        to_remove = set()
        for p in positions[key]:
            home = next_homes[key][value]
            if grid[home[0]][home[1]] != '.':
                continue
            moves = get_moves(grid, p, home)
            if not moves:
                continue
            energy_used += moves * KEY_TO_ENERGY[key]
            grid[p[0]][p[1]] = '.'
            grid[home[0]][home[1]] = key
            value += 1
            n['value'] = value
            to_remove.add(p)
        positions[key] -= to_remove

    if energy_used:
        # If finished, return energy used
        if not any(positions.values()):
            cache[cache_key] = energy_used
            return energy_used

        completion_energy = find_min_organization_energy(
            grid, nexts, available_pos, next_homes, cache, grids
        )
        if completion_energy:
            energy_used += completion_energy
        else:
            energy_used = 0
        cache[cache_key] = energy_used
        return energy_used

    # For each unfinished bug, find a hallway position to move to and compute
    # shortest energy with that move. Find min of all.
    energy_used = sys.maxsize
    for n in nexts:
        key = n['key']
        for p in positions[key]:
            if in_hallway(p):
                continue
            for dest in ALLOWED_HALLWAY_POS:
                if grid[dest[0]][dest[1]] != '.':
                    continue
                moves = get_moves(grid, p, dest)
                if not moves:
                    continue
                grid[p[0]][p[1]] = '.'
                grid[dest[0]][dest[1]] = key
                completion_energy = find_min_organization_energy(
                    grid, nexts, available_pos, next_homes, cache, grids
                )
                if completion_energy:
                    total_energy = moves * KEY_TO_ENERGY[key] + completion_energy
                    energy_used = min(energy_used, total_energy)
                grid[p[0]][p[1]] = key
                grid[dest[0]][dest[1]] = '.'

    # No moves
    if energy_used == sys.maxsize:
        cache[cache_key] = 0
        return 0

    cache[cache_key] = energy_used
    return energy_used


def get_positions(grid, available_pos, next_homes):
    positions = {
        'A': set(),
        'B': set(),
        'C': set(),
        'D': set()
    }
    for p in available_pos:
        type = grid[p[0]][p[1]]
        if type in positions:
            positions[type].add(p)

    # Get rid of finished positions
    for k, v in next_homes.items():
        for p in v:
            if p in positions[k]:
                positions[k].remove(p)
            else:
                break

    return positions


def get_moves(grid, start, end):
    distance_x = end[1] - start[1]
    step_x = 1 if distance_x > 0 else -1

    moves = 0
    curr = start
    while curr != end:
        if curr[1] != end[1]:
            if in_hallway(curr):
                curr = (curr[0], curr[1] + step_x)
                if grid[curr[0]][curr[1]] != '.':
                    return 0
            else:
                curr = (curr[0] - 1, curr[1])
                if grid[curr[0]][curr[1]] != '.':
                    return 0
        elif curr[0] != end[0]:
            curr = (curr[0] + 1, curr[1])
            if grid[curr[0]][curr[1]] != '.':
                return 0
        moves += 1
    return moves


def in_hallway(p):
    return p[0] == 1


def print_grid(grid):
    for r in grid:
        print(''.join(r))


def validate(grid):
    counts = defaultdict(int)
    for r in grid:
        for c in r:
            counts[c] += 1
    if counts['A'] != 2 or counts['B'] != 2 or counts['C'] != 2 or counts['D'] != 2:
        raise Exception()


def check_equal(grid, grids):
    if get_cache_key(grid) in grids:
        return True
    return False


def get_cache_key(grid):
    s = [''.join(r) for r in grid]
    return '\n'.join(s).strip()


def parse_data(data):
    grids = data.split('\n\n')

    rows = grids[0].split('\n')
    char_array = []
    for r in rows:
        chars = []
        for c in r:
            chars.append(c)
        char_array.append(chars)

    return char_array, set(grids[1:])
