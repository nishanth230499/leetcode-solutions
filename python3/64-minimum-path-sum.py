class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        mem = [[None for _ in range(n)] for _ in range(m)]
        mem[0][0] = grid[0][0]
        def rec(i, j):
            if mem[i][j] != None:
                return mem[i][j]
            res = float("INF")
            if i > 0:
                res = min(res, rec(i-1, j) + grid[i][j])
            if j > 0:
                res = min(res, rec(i, j-1) + grid[i][j])
            mem[i][j] = res
            return res
        
        return rec(m-1, n-1)