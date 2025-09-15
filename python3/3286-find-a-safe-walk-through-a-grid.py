import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        m = len(grid)
        n = len(grid[0])
        q = [(-health + grid[0][0], (0, 0))]
        vis = set()

        while q:
            h, (ux, uy) = heapq.heappop(q)
            if h >= 0:
                return False
            if ux == m - 1 and uy == n - 1:
                return True
            if (ux, uy) not in vis:
                vis.add((ux, uy))
                for dx, dy in dirs:
                    vx, vy = ux + dx, uy + dy
                    if 0 <= vx < m and 0 <= vy < n:
                        heapq.heappush(q, (h + grid[vx][vy], (vx, vy)))
        return False
