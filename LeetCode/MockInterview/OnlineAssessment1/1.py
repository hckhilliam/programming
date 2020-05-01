class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

#         d = [False for i in range(n)]
#         d[-1] = True
#         d[-2] = True
#         d[-3] = True
#         for i in range(n - 4, -1, -1):
#             d[i] = not d[i + 1] or not d[i + 2] or not d[i + 3]
#         return d[0]
