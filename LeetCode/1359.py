class Solution:
    def countOrders(self, n: int) -> int:
        m = 1000000007
        c = 1
        cc = 0
        for i in range(2, (2 * n) + 1):
            c *= i
            while cc < n and c % 2 == 0:
              c //= 2
              cc += 1
        return int(c % m)

print(Solution().countOrders(91))
# print(Solution().countOrders(2))
# print(Solution().countOrders(3))

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2

# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# 2 4 3 1

#