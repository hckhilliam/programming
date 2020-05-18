import numpy as np

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # d[i][0] = max subarray including i
        # d[i][1] = how many used
        # d[i][0] = max(A[i] + d[i - 1] - d[i - d[i - 1][1], A[i])
        # d[i][1] = 1 + d[i + 1][1] if used
        dl = np.zeros(len(A), dtype=int)
        dr = np.zeros(len(A), dtype=int)

        pm = A[0]
        m = pm
        dl[0] = A[0]
        dr[-1] = A[-1]

        l = A[0]
        r = A[-1]
        ri = len(A) - 2
        for i in range(1, len(A)):
            l += A[i]
            r += A[ri]
            dl[i] = max(l, dl[i - 1])
            dr[ri] = max(r, dr[ri + 1])
            pm = max(pm + A[i], A[i])
            m = max(pm, m)
            ri -= 1

        for i in range(0, len(A) - 2):
            m = max(m, dl[i] + dr[i + 2])

        return m

#         d = np.zeros((len(A) * 2, 2), dtype=int)
#         m = A[0]
#         d[0][0] = A[0]
#         d[0][1] = 1
#         for i in range(1, len(d)):
#             o = d[i - 1][0]
#             n = d[i - 1][1]
#             d[i][0] = A[i % len(A)]
#             d[i][1] = 1
#             if n == len(A):
#                 o -= A[i - n]
#                 n -= 1
#             if o > 0:
#                 d[i][0] += o
#                 d[i][1] += n
#             m = max(m, d[i][0])

#         return m

    # 5 -3 5 5 -3 5
    # 5  2 7

        #  1  2    3    -4  5   6   7   8    1       2        3     4      5   6     7    8
        #  28 27   25   22  26  21  15  8
        #  1  3    6     2  7   13  20  28   28     28
