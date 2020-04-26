from sys import stdin, stdout


def solve(tc):
    n = int(stdin.readline().strip())
    h = [int(inp) for inp in stdin.readline().strip().split(' ')]
    s = 0
    for i in range(1, len(h) - 1):
        if h[i - 1] < h[i] and h[i + 1] < h[i]:
            s += 1
    stdout.write('Case #{}: {}\n'.format(tc, s))


t = int(stdin.readline().strip())

for i in range(t):
    solve(i + 1)
