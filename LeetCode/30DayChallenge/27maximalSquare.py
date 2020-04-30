class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    m = max(m, self.findMax(i, j, matrix))
        return m ** 2

    def findMax(self, i, j, matrix):
        m = 1
        while True:
            c = m + 1
            anchor = j + c - 1
            for a in range(i, i + c):
                if a >= len(matrix) or anchor >= len(matrix[a]) or matrix[a][anchor] != '1':
                    return m

            anchor = i + c - 1
            if anchor >= len(matrix):
                return m

            for a in range(j, j + c):
                if a >= len(matrix[anchor]) or matrix[anchor][a] != '1':
                    return m
            m = c
