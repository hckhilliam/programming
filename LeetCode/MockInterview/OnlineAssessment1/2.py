class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
#         xb = bin(x)[2:]
#         yb = bin(y)[2:]

#         i = len(xb) - 1
#         j = len(yb) - 1
#         d = 0
#         while i >= 0 and j >= 0:
#             if xb[i] != yb[i]
        d = 0
        while x > 0 and y > 0:
            x, xr = divmod(x, 2)
            y, yr = divmod(y, 2)
            if xr != yr:
                d += 1
        while x > 0:
            x, xr = divmod(x, 2)
            if xr == 1:
                d += 1
        while y > 0:
            y, yr = divmod(y, 2)
            if yr == 1:
                d += 1
        return d
