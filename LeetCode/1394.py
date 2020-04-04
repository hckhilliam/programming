from collections import defaultdict

class Solution:
    def findLucky(self, arr):
      counts = defaultdict(int)
      for a in arr:
        counts[a] += 1
      keys = counts.keys()
      keys.sort(reverse=True)
      for c in keys:
        if counts[c] == c:
          return c
      return -1

print(Solution().findLucky([2,2,3,4]))