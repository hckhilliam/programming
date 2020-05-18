from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        c = defaultdict(int)
        m = set()
        t = set()
        for p in trust:
            t.add(p[0])
            c[p[1]] += 1
            if c[p[1]] == N - 1:
                m.add(p[1])
        j = [mm for mm in m if mm not in t]
        return j[-1] if j else - 1
