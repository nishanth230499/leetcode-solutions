class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.gold = 0
        vis = set()
        self.max_gold = 0

        m = len(grid)
        n = len(grid[0])
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        def rec(i, j):
            if grid[i][j] and (i, j) not in vis:
                vis.add((i, j))
                self.gold += grid[i][j]
                self.max_gold = max(self.max_gold, self.gold)
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        rec(x, y)
                self.gold -= grid[i][j]
                vis.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                rec(i, j)
        
        return self.max_gold