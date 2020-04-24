from collections import defaultdict
from sys import stdout

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m:
            return 0

        # m p n combinations
        # must be ascending only k times

        # m = 4, n = 3,
        # k = 3
        # 4
        #
        # k = 2
        #
        #
        # k = 1
        # 3 P 2 because we have to choose max on #1
        #
        # {1,2,3}, {1,3,2}, {1,2,4}, {1,4,2}, {1,3,4}, {1,4,3}, {2,1,3}, {2,3,1},
        # {2,1,4}, {2,4,1}, {2,3,4}, {2,4,3}, {3,1,2}, {3,2,1}, {3,1,4}, {3,4,1},
        # {3,2,4}, {3,4,2}, {4,1,2}, {4,2,1}, {4,1,3}, {4,3,1}, {4,2,3}, {4,3,2}

        # [1, 1], [1, 2], [1, 3], [1, 4]
        # [2, 1], [2, 2], [2, 3], [2, 4]
        # [3, 1], [3, 2], [3, 3], [3, 4]
        # [4, 1], [4, 2], [4, 3], [4, 4]

    def generator(self, n, m):
        if n == 0:
            return [[[]]]

        a = []
        for i in range(m):
            b = []
            for r in self.generator(n - 1, m):
                for p in r:
                    b.append([i] + p)
            a.append(b)
        return a


x = Solution().generator(3, 4)
c = 0
for y in x:
    c += len(y)
    print(y)
print(c)
