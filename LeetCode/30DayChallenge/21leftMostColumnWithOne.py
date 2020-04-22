# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        m = dim[1] - 1
        found = False
        for y in range(dim[0]):
            if binaryMatrix.get(y, 0) == 1:
                return 0

            l = 0
            h = dim[1]
            c = h // 2
            while c != l:
                n = binaryMatrix.get(y, c)
                if n == 1:
                    h = c
                    c = (c + l) // 2
                    found = True
                else:
                    l = c
                    c = (c + h) // 2
            m = min(m, c + 1)
        return m if found else -1
