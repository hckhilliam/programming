from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        a = defaultdict(int)
        for nn in range(1, n + 1):
            s = 0
            while nn:
                nn, r = divmod(nn, 10)
                s += r
            a[s] += 1
        m = max(a.values())
        c = 0
        for b in a.values():
            if b == m:
                c += 1
        return c
