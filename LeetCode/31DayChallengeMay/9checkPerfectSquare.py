class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.gallopSearch(num)

    def gallopSearch(self, num):
        if not num:
            return False

        h = 1
        while h * h < num:
            h *= 2

        # Returns lower of value if cannot be found.
        l = 0
        while l <= h:
            m = (l + h) // 2
            s = m * m
            if s == num:
                return True

            # Go lower case.
            elif s > num:
                h = m - 1
            # Go higher case.
            else:
                l = m + 1
        return False


for i in range(0, 101):
    print(i, Solution().isPerfectSquare(i))
