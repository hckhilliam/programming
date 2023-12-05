from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    seed_str = rows[0].split(': ')[-1]
    seeds = [int(s) for s in seed_str.strip().split(' ')]

    global seed_to_soil
    global soils
    global soil_to_fert
    global ferts
    global fert_to_water
    global waters
    global water_to_light
    global lights
    global light_to_temp
    global temps
    global temp_to_humid
    global humids
    global humid_to_location
    global locations

    seed_to_soil, i = get_map(3, rows)
    soils = sorted(seed_to_soil.keys())
    soil_to_fert, i = get_map(i + 1, rows)
    ferts = sorted(soil_to_fert.keys())
    fert_to_water, i = get_map(i + 1, rows)
    waters = sorted(fert_to_water.keys())
    water_to_light, i = get_map(i + 1, rows)
    lights = sorted(water_to_light.keys())
    light_to_temp, i = get_map(i + 1, rows)
    temps = sorted(light_to_temp.keys())
    temp_to_humid, i = get_map(i + 1, rows)
    humids = sorted(temp_to_humid.keys())
    humid_to_location, i = get_map(i + 1, rows)
    locations = sorted(humid_to_location.keys())

    min_location = max(locations)
    for s in seeds:
        min_location = min(get_location(s), min_location)
    return min_location


def get_location(s):
    v = get_next_dest(s, soils, seed_to_soil)
    v = get_next_dest(v, ferts, soil_to_fert)
    v = get_next_dest(v, waters, fert_to_water)
    v = get_next_dest(v, lights, water_to_light)
    v = get_next_dest(v, temps, light_to_temp)
    v = get_next_dest(v, humids, temp_to_humid)
    v = get_next_dest(v, locations, humid_to_location)
    return v


def get_next_dest(s, arr, m):
    idx = binarySearch(arr, s)
    closest = arr[idx]
    dest, l = m[closest]
    if closest <= s <= closest + l:
        return dest + (s - closest)
    else:
        return s


def get_map(i, rows):
    m = {}
    while i < len(rows):
        r = rows[i]
        i += 1
        if not r.strip():
            break
        dest, source, l = (int(s) for s in r.split(' '))
        m[source] = (dest, l)
    return m, i


def part2(data):
    rows = parse_data(data)
    seed_ranges_l = rows[0].split(': ')[-1].split(' ')
    i = 0
    seed_ranges = []
    while i < len(seed_ranges_l):
        seed_ranges.append((int(seed_ranges_l[i]), int(seed_ranges_l[i + 1])))
        i += 2

    global seed_to_soil
    global soils
    global soil_to_fert
    global ferts
    global fert_to_water
    global waters
    global water_to_light
    global lights
    global light_to_temp
    global temps
    global temp_to_humid
    global humids
    global humid_to_location
    global locations

    seed_to_soil, i = get_map(3, rows)
    soils = sorted(seed_to_soil.keys())
    soil_to_fert, i = get_map(i + 1, rows)
    ferts = sorted(soil_to_fert.keys())
    fert_to_water, i = get_map(i + 1, rows)
    waters = sorted(fert_to_water.keys())
    water_to_light, i = get_map(i + 1, rows)
    lights = sorted(water_to_light.keys())
    light_to_temp, i = get_map(i + 1, rows)
    temps = sorted(light_to_temp.keys())
    temp_to_humid, i = get_map(i + 1, rows)
    humids = sorted(temp_to_humid.keys())
    humid_to_location, i = get_map(i + 1, rows)
    locations = sorted(humid_to_location.keys())

    soil_ranges = get_ranges(seed_ranges, soils, seed_to_soil)
    fert_ranges = get_ranges(soil_ranges, ferts, soil_to_fert)
    water_ranges = get_ranges(fert_ranges, waters, fert_to_water)
    light_ranges = get_ranges(water_ranges, lights, water_to_light)
    temp_ranges = get_ranges(light_ranges, temps, light_to_temp)
    humid_ranges = get_ranges(temp_ranges, humids, temp_to_humid)
    location_ranges = get_ranges(humid_ranges, locations, humid_to_location)
    min_location = 999999999999
    for r in location_ranges:
        min_location = min(min_location, r[0])
    return min_location


def get_ranges(curr_ranges, arr, m):
    ranges = []
    for (r, l) in curr_ranges:
        idx = binarySearch(arr, r)
        closest = arr[idx]
        while True:
            dest, dest_l = m[closest]
            # r is between range
            if closest <= r <= closest + dest_l:
                diff = r - closest
                l_fit = min(l, closest + dest_l - r)
                ranges.append((dest + diff, l_fit))
                # r range extends beyond range
                if l_fit < l:
                    r = r + l_fit
                    l = l - l_fit
                    idx += 1
                    if idx >= len(arr):
                        ranges.append((r, l))
                        break
                    closest = arr[idx]
                # r range is contained. done.
                else:
                    break
            # r preceeds closest and overlaps into it
            elif r < closest:
                fit = min(closest - r, l)
                ranges.append((r, fit))
                # r range extends beyond range.
                if fit < l:
                    r = r + fit
                    l = l - fit
                # r range is contained. done.
                else:
                    break
            # r is after entire range
            else:
                idx += 1
                if idx >= len(arr):
                    ranges.append((r, l))
                    break
                closest = arr[idx]
    return ranges


def parse_data(data):
    rows = data.split('\n')
    return rows


def binarySearch(a, target):
    # Returns lower of value if cannot be found.
    l = 0
    h = len(a)
    c = h // 2
    while c != l:
        n = a[c]
        # Go lower case.
        if n > target:
            h = c
            c = (c + l) // 2
        # Go higher case.
        else:
            l = c
            c = (c + h) // 2
    return c
