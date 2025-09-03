class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        q = [(grid[0][0], (0, 0))]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        max_height = 0

        while q:
            height, (x, y) = heapq.heappop(q)
            if (x, y) not in visited:
                visited.add((x, y))
                max_height = max(max_height, height)
                if x == n-1 and y == n-1:
                    break
                for (dx, dy) in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny <n and (nx, ny) not in visited:
                        heapq.heappush(q, (grid[nx][ny], (nx, ny)))
        
        return max_height