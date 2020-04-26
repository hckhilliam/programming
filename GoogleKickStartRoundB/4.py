from sys import stdin, stdout


def getBase(w, h):
    smaller = min(w, h)
    larger = max(w, h)
    total = smaller + larger
    totalPaths = 1
    for i in range(smaller):
        totalPaths *= total - i
        totalPaths //= i + 1
    return totalPaths


def solve(tc):
    w, h, l, u, r, d = (int(inp) for inp in stdin.readline().strip().split(' '))
    x = l - 2 if l - 1 > 0 else l - 1
    y = u - 2 if u - 1 > 0 else u - 1

    base = getBase(x, y) / (2 ** (x + y))

    missed = 0.0
    if u != 1:
        if r == w:
            p = base
            if l - 1 == 0:
                missed = 1.0
            else:
                missed += p / 2
                for rowNum in range(y, 0, -1):
                    p = p * 2 * rowNum / (rowNum + x)
                    missed += p / 2
        else:
            p = base
            for columnNum in range(l - 1, r):
                if columnNum != 0:
                    p = p * (y + columnNum) / (columnNum * 2)
                missed += p / 2
    if l != 1:
        if d == h:
            p = base
            if u - 1 == 0:
                missed = 1.0
            else:
                missed += p / 2
                for columnNum in range(x, 0, -1):
                    p = p * 2 * columnNum / (columnNum + y)
                    missed += p / 2
        else:
            p = base
            for rowNum in range(u - 1, d):
                if rowNum != 0:
                    p = p * (x + rowNum) / (rowNum * 2)
                missed += p / 2

    stdout.write('Case #{}: {}\n'.format(tc, 1 - missed))


t = int(stdin.readline().strip())

for i in range(t):
    solve(i + 1)
