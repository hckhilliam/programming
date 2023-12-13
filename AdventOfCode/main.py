# Repl.it AOC Python Runner
import runner
import sys

is_test = 0
if len(sys.argv) > 1:
    is_test = int(sys.argv[1])

runner.run(day=13, year=2023, is_test=is_test)
