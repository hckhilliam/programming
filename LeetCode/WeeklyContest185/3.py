from collections import defaultdict

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        t = defaultdict(int)

        m = 0
        frogs = 0
        for c in croakOfFrogs:
            if c == 'c':
                frogs += 1
                t['r'] += 1
            elif c == 'r':
                t['r'] -= 1
                t['o'] += 1
            elif c == 'o':
                t['o'] -= 1
                t['a'] += 1
            elif c == 'a':
                t['a'] -= 1
                t['k'] += 1
            elif c == 'k':
                t['k'] -= 1
                frogs -= 1
            if any(v < 0 for v in t.values()):
                return -1
            m = max(m, frogs)

        if any(v > 0 for v in t.values()):
                return -1
        return m


print(Solution().minNumberOfFrogs('croakcroak'))
print(Solution().minNumberOfFrogs('crcoakroak'))
print(Solution().minNumberOfFrogs('croakcrook'))
print(Solution().minNumberOfFrogs('croakcroa'))
