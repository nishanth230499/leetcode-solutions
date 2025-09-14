import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        n = len(moveTime)
        m = len(moveTime[0])

        q = [(0, 1, (0, 0))]
        vis = set()

        while q:
            t, dt, (ux, uy) = heapq.heappop(q)
            if (ux, uy) not in vis:
                vis.add((ux, uy))
                if ux == n-1 and uy == m-1:
                    return t
                
                for dx, dy in dirs:
                    vx, vy = ux + dx, uy + dy
                    if 0 <= vx < n and 0 <= vy < m:
                        heapq.heappush(q, (max(t, moveTime[vx][vy]) + dt, 3 - dt, (vx, vy)))
