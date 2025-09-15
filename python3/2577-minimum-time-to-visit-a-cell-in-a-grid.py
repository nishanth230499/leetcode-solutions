import math
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        m = len(grid)
        n = len(grid[0])
        q = [(0, (0, 0))]
        vis = set()

        while q:
            t, (ux, uy) = heapq.heappop(q)
            if ux == m-1 and uy == n-1:
                return t
            for dx, dy in dirs:
                vx, vy = ux + dx, uy + dy
                if 0 <= vx < m and 0 <= vy < n:
                    if (vx , vy) not in vis:
                        vis.add((vx, vy))
                        if t + 1 >= grid[vx][vy]:
                            heapq.heappush(q, (t + 1, (vx, vy)))
                        else:
                            diff = grid[vx][vy] - (t + 1)
                            diff = math.ceil(diff / 2) * 2
                            heapq.heappush(q, (t + diff + 1, (vx, vy)))
        
        return -1