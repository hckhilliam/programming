# Repl.it AOC Python Runner
import runner
import sys

part = None
if len(sys.argv) > 1:
    part = int(sys.argv[1])

is_test = 0
if len(sys.argv) > 2:
    is_test = int(sys.argv[2])


runner.run(day=17, year=2023, part=part, is_test=is_test)
