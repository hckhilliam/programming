import re

parser = r'\d+|\+|\*|\(|\)'


def part1(data):
    rows = parse_data(data)
    total = 0
    for row in rows:
        args = re.findall(parser, row)
        eqn = []
        for a in args:
            currArg = None
            if a.isnumeric():
                currArg = int(a)
            elif a == ')':
                currArg = eqn.pop()
                eqn.pop()  # Should be (
            else:
                currArg = a

            if eqn and eqn[-1] in ['+', '*'] and isinstance(currArg, int):
                op = eqn.pop()
                other = eqn.pop()
                if op == '+':
                    eqn.append(other + currArg)
                else:
                    eqn.append(other * currArg)
            else:
                eqn.append(currArg)
        total += eqn[0]
    return total


def part2(data):
    rows = parse_data(data)
    total = 0
    for row in rows:
        args = re.findall(parser, row)
        eqn = []
        for a in args:
            currArg = None
            if a.isnumeric():
                currArg = int(a)
            elif a == ')':
                currArg = eqn.pop()
                while eqn[-1] != '(':
                    # Only multiplications should be left.
                    eqn.pop()
                    currArg = eqn.pop() * currArg
                eqn.pop()
            else:
                currArg = a

            # Do addition first.
            if eqn and eqn[-1] in ['+'] and isinstance(currArg, int):
                op = eqn.pop()
                other = eqn.pop()
                if op == '+':
                    eqn.append(other + currArg)
                else:
                    eqn.append(other * currArg)
            else:
                eqn.append(currArg)

        prod = 1
        for arg in eqn:
            if isinstance(arg, int):
                prod *= arg
        total += prod
    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
