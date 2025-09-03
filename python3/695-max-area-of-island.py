class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
            grid[x][y] = 0
            soln = 1
            for (dx, dy) in directions:
                i, j = x+dx, y+dy
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    soln += dfs(i, j)
            return soln


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res