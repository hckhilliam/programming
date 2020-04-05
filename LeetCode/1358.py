from queue import Queue

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
      q = Queue()
      c = {
        'a': 0,
        'b': 0,
        'c': 0
      }
      movingBound = -1
      num = 0
      for i, ch in enumerate(s):
        q.put((i, ch))
        c[ch] += 1
        while all(c.values()):
          t = q.get()
          firstInd = t[0]
          c[t[1]] -= 1
          num += (firstInd - movingBound) * (len(s) - i - 1) + 1
          movingBound = firstInd
      return num


print(Solution().numberOfSubstrings('ababbbc'))
print(Solution().numberOfSubstrings('abcabc'))
print(Solution().numberOfSubstrings('aaacb'))
print(Solution().numberOfSubstrings('abc'))