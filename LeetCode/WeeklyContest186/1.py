class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == '1':
                ones += 1

        score = ones
        m = 0
        for i, c in enumerate(s):
            if c == '1':
                score -= 1
            elif c == '0' and i != len(s) - 1:
                score += 1
            m = max(m, score)
        return m
