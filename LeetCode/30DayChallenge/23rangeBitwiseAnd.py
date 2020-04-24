class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bm = bin(m)
        bn = bin(n)

        if len(bm) != len(bn):
            return 0

        r = []
        zeroes = 0
        for i in range(2, len(bm)):
            if bm[i] == bn[i]:
                r.append(bm[i])
            else:
                zeroes = len(bm) - i
                break
        return int(''.join(r) + '0' * zeroes, 2)
