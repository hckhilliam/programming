class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0

        ee = sorted(events, key=lambda e: e[1])
        c = 1
        d = set([ee[0][0]])
        for i in range(1, len(ee)):
            e = ee[i]
            s = e[0]
            while s in d and s < e[1]:
                s += 1
            if s not in d:
                d.add(s)
                c += 1
        return c
