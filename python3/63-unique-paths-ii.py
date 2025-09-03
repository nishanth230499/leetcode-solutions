class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mem = [[None for _ in range(n)] for _ in range(m)]
        mem[0][0] = 1
        def rec(i, j):
            if obstacleGrid[i][j]:
                return 0
            if mem[i][j]!= None:
                return mem[i][j]
            res = 0
            if i > 0:
                res += rec(i-1, j)
            if j > 0:
                res += rec(i, j-1)
            mem[i][j] = res
            return res
        return rec(m-1, n-1)