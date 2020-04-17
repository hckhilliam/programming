class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        a = sum(satisfaction)
        m = 0
        for i, s in enumerate(satisfaction):
            m += (i + 1) * s

        mm = m
        for s in satisfaction:
            if s >= 0:
                return mm
            a -= s
            m = m - s - a
            mm = max(m, mm)
        return mm
