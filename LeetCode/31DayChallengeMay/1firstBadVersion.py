# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l = 0
        h = n
        c = h // 2
        while c != l:
            if isBadVersion(c):
                h = c
                c = (c + l) // 2
            else:
                l = c
                c = (c + h) // 2
        return c + 1
