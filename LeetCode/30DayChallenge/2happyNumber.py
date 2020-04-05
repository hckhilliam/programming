class Solution:
    def isHappy(self, n: int) -> bool:
        v = set()
        nn = n
        while nn not in v:
          v.add(nn)
          s = 0
          while nn > 0:
            q, r = divmod(nn, 10)
            s += r ** 2
            nn = q
          nn = s
          if nn == 1:
            return True
        return False

print(Solution().isHappy(1))
