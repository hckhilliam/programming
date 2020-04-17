class Solution:
    def numSteps(self, s: str) -> int:
        a = [int(c) for c in s]
        t = 0
        while a:
            if len(a) == 1:
                return t
            if not a[-1]:
                a.pop()
            else:
                n = len(a) - 1
                while n >= 0 and a[n] != 0:
                    a[n] = 0
                    n -= 1
                if n >= 0:
                    a[n] = 1
                else:
                    a = [1] + a
            t += 1
        return t
