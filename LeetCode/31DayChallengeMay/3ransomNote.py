from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = defaultdict(int)
        for ch in ransomNote:
            c[ch] -= 1

        for ch in magazine:
            c[ch] += 1

        return all(x >= 0 for x in c.values())
