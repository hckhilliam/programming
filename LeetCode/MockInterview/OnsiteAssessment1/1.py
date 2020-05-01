class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = '0' * (32 - len(b)) + b
        return int(b[::-1], 2)
