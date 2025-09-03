class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[-1] * n for _ in range(m)]
        def dp(i, j):
            if mem[i][j] != -1:
                return mem[i][j]
            if(i == 0 or j == 0):
                mem[i][j] = 1
                return mem[i][j]
            mem[i][j] = dp(i-1, j) + dp(i, j-1)
            return mem[i][j]
        return dp(m-1, n-1)