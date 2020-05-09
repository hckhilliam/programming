from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ccs = defaultdict(int)
        fi = -1
        for ch in s:
            ccs[ch] += 1
        for i, ch in enumerate(s):
            if ccs[ch] == 1:
                return i
        return -1
