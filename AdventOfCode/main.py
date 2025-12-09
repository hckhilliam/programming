# Repl.it AOC Python Runner
import runner
import sys

day = 1
if len(sys.argv) > 1:
    day = int(sys.argv[1])

part = None
if len(sys.argv) > 2:
    part = int(sys.argv[2])

is_test = 0
if len(sys.argv) > 3:
    is_test = int(sys.argv[3])


runner.run(day=day, year=2025, part=part, is_test=is_test)
