from sys import stdin, stdout

def getBase(w, h):
    smaller = min(w, h)
    larger = max(w, h)
    totalPaths = 1
    for i in range(larger+1, smaller+larger+1):
        totalPaths *= i
    for j in range(1, smaller+1):
        totalPaths //= j
    return totalPaths

def pp(tag, p, xy):
    print('{} added {} for {}'.format(tag, p, xy))

def solve(tc):
    w, h, l, u, r, d = (int(inp) for inp in stdin.readline().strip().split(' '))
    x = l - 2 if l - 1 > 0 else l - 1
    y = u - 2 if u - 1 > 0 else u - 1

    base = getBase(x, y) / (2 ** (x + y))

    missed = 0.0
    if u != 1:
        if r == w:
            cp = base
            if l - 1 == 0:
                missed = 1.0
            else:
                missed += cp / 2
                # pp('[gocols]', cp/2, (x + 1, y + 2))
                for rowNum in range(y, 0, -1):
                    cp = cp * 2 * rowNum / (rowNum + x)
                    missed += cp / 2
                    # pp('[gocols]', cp/2, (x + 1, rowNum))
            # if l - 1 == 0:
            #     missed = 1.0
            # else:
            #     b = 1 / (2 ** (x))
            #     missed += b / 2
            #     for k in range (2, y + 2):
            #         b = b * (x + k) / (k * 2)
            #         missed += b / 2
        else:
            copyBase = base
            # calculate for the row
            for columnNum in range(l - 1, r):
                if columnNum == 0:
                    copyBase = base
                else:
                    copyBase = copyBase * (y + columnNum) / (columnNum * 2)
                missed += copyBase / 2
                # pp('[defaultcols]', copyBase/2, (columnNum + 1, y + 2))
    if l != 1:
        if d == h:
            cp = base
            if u - 1 == 0:
                missed = 1.0
            else:
                missed += cp / 2
                # pp('[gorows]', cp/2, (x + 1, y + 2))
                for columnNum in range(x, 0, -1):
                    cp = cp * 2 * columnNum / (columnNum + y)
                    missed += cp / 2
                    # pp('[gorows]', cp/2, (columnNum, y + 1))
            # if u - 1 == 0:
            #     missed = 1.0
            # else:
            #     b = 1 / (2 ** (y))
            #     missed += b / 2
            #     for k in range (2, x + 2):
            #         b = b * (y + k) / (k * 2)
            #         missed += b / 2

        else:
            # calculate for the column
            for rowNum in range(u - 1, d):
                if rowNum != 0:
                    base = base * (x + rowNum) / (rowNum * 2)
                missed += base / 2
                # pp('[defaultcols]', base/2, (x + 2, rowNum + 1))

    stdout.write('Case #{}: {}\n'.format(tc, 1 - missed))


t = int(stdin.readline().strip())

for i in range(t):
    solve(i + 1)
