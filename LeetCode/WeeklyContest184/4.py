class Solution:
    def numOfWays(self, n: int) -> int:
        d = [0 for i in range(n)]
        dd = [0 for i in range(n)]
        d[0] = 1
        dd[0] = 1
        # d[i] = # of combinations if d[i] is unique
        # dd[i] = # of combinations if d[i] is not unique

        # d[i] = 2 * d[i-1] + 2 * dd[i-1]
        # dd[i] = 2 * d[i-1] + 3 * dd[i-1]

        for i in range(1, n):
            d[i] = 2 * d[i - 1] + 2 * dd[i - 1]
            dd[i] = 2 * d[i - 1] + 3 * dd[i - 1]
        return (d[-1] * 6 + dd[-1] * 6) % 1000000007


print(Solution().numOfWays(2))
print(Solution().numOfWays(3))
print(Solution().numOfWays(7))
print(Solution().numOfWays(5000))
