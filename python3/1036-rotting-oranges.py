class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0
        while q:
            found = False
            for _ in range(len(q)):
                (x, y) = q.popleft()
                for (dx, dy) in directions:
                    i, j = x+dx, y+dy
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        found = True
                        q.append((i, j))
            if found:
                time += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time