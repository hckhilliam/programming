from collections import defaultdict

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        odds = 0
        for c in counts.values():
            if c % 2 == 1:
                odds += 1
        return odds <= k and len(s) >= k
