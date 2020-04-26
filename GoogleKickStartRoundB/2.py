from sys import stdin, stdout


def solve(tc):
    n, d = (int(inp) for inp in stdin.readline().strip().split(' '))
    x = [int(inp) for inp in stdin.readline().strip().split(' ')]


    for i in range(n - 1, -1, -1):
        d -= d % x[i]

    stdout.write('Case #{}: {}\n'.format(tc, d))


t = int(stdin.readline().strip())

for i in range(t):
    solve(i + 1)
