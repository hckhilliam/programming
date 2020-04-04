import numpy as np

class Solution(object):
    def numTeams(self, rating):
        # d[i][j] = max possibilities if this is the jth number
        # d[i][2] = sum(d[j][1] for j in 0..i-1 if rating[j] < rating[i])
        # d[i][1] = sum[d[j][0] for j in 0..i-1 if rating[j] < rating[i])
        # d[i][0] = 1
        # return sum(d[i][2])
        l = len(rating)
        dg = np.zeros((l, 3), dtype=int)
        dl = np.zeros((l, 3), dtype=int)
        for i in range(l):
          dg[i][0] = 1
          dl[i][0] = 1
          for j in range(i):
            if rating[j] < rating[i]:
              dg[i][1] += dg[j][0]
              dg[i][2] += dg[j][1]
            elif rating[j] > rating[i]:
              dl[i][1] += dl[j][0]
              dl[i][2] += dl[j][1]
        return sum(dg[:, 2]) + sum(dl[:, 2])

print(Solution().numTeams([1, 2, 3, 4]))