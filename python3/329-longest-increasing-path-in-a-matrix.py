class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mem = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        def rec(i, j):
            dirs = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]
            if mem[i][j] != None:
                return mem[i][j]
            res = 1
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j]:
                    res = max(res, rec(x, y) + 1)
            mem[i][j] = res
            return res
        
        res = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, rec(i, j))
        return res