class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        m = sum(cardPoints[i] for i in range(k))
        s = m
        for i in range(k):
            s -= cardPoints[k - i - 1]
            s += cardPoints[-(i + 1)]
            m = max(s, m)
        return m
