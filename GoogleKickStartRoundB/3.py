from sys import stdin, stdout

c = 1000000000
p = None


def solve(tc):
    p = stdin.readline().strip() + ')'
    x, y, _ = getDirections(0, p)
    stdout.write('Case #{}: {} {}\n'.format(tc, x % c + 1, y % c + 1))


def getDirections(s, p):
    x = 0
    y = 0
    ch = p[s]
    while ch != ')':
        if ch == 'W':
            x -= 1
        elif ch == 'E':
            x += 1
        elif ch == 'N':
            y -= 1
        elif ch == 'S':
            y += 1
        else:
            n = int(ch)
            x2, y2, s = getDirections(s + 2, p)
            x += n * x2
            y += n * y2
        s += 1
        ch = p[s]
    return x, y, s


t = int(stdin.readline().strip())

for i in range(t):
    solve(i + 1)
