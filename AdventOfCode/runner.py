"""Advent of code puzzle runner
Author: Scoder12"""

import time
import math
from typing import Any
import importlib


def format_filename(day, year):
    # You can customize this to your liking.
    return "{}/{}".format(year, str(day).zfill(2))


def format_runtime(ms):
    # You can customize this to your liking

    # Microseconds
    if ms <= 1:
        return f"{round(ms * 1000)}µs"
    # Milliseconds
    if ms < 1000:
        whole_ms = math.floor(ms)
        rem_ms = ms - whole_ms
        return f"{whole_ms}ms " + format_runtime(rem_ms)
    sec = ms / 1000
    # Seconds
    if sec < 60:
      whole_sec = math.floor(sec)
      rem_ms = ms - whole_sec * 1000
      return f'{whole_sec}s ' + format_runtime(rem_ms)
    # Minutes (hopefully it doesn't get to this point lol)
    return f"{math.floor(sec / 60)}m " + format_runtime((sec % 60)* 1000)


def run_part(part: str, mod: Any, data: str):
    funcname = f'part{part}'

    f = getattr(mod, funcname, None)
    if callable(f):
        print(f"Running Part {part}")

        start = time.perf_counter()
        val = f(data)
        end = time.perf_counter()

        print(f"Output: {val}")
        rtime = (end - start) * 1000 # sec -> ms
        print(f"Took {format_runtime(rtime)}\n")
        return rtime
    else:
        print(f"No {funcname} function")
        return 0

    return rtime


def get_data(day, year, is_test):
    # Try to find the filename
    if is_test:
        fname = "{}-test.txt".format(format_filename(day, year))
    else:
        fname = "{}.txt".format(format_filename(day, year))
    print(fname)
    try:
        with open(fname, "r") as f:
            data = f.read()
    except Exception as e:
        raise ValueError(f"Unable to read file {fname}") from e

    print(f"Loaded puzzle input from {fname}\n")
    return data


def run(day, year=2020, part=None, is_test=False):
    print(f"AOC {year} Day {day}")
    mod = importlib.import_module(format_filename(day, year).replace('/', '.'))
    data = get_data(day, year, is_test)

    part1Time = 0
    part2Time = 0
    if not part or part == 1:
        part1Time = run_part(1, mod, data)
    if not part or part == 2:
        part2Time = run_part(2, mod, data)
    print(f"Total runtime: {format_runtime(part1Time + part2Time)}")


def get_day(max_day=None):
    while True:
        prompt = f"Enter day" + f" (max {max_day})" if max_day else ''
        inp = input(prompt + ": ")
        try:
            day = int(inp)
        except ValueError:
            print("Invalid day")
            continue

        if max_day and day <= max_day:
            return day
        else:
            print(f"Must be at most {max_day}")
