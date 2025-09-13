from collections import defaultdict
import heapq

class Solution:
    def cost(self, u, v):
        return abs(u[0] - v[0]) + abs(u[1] - v[1])

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        g = defaultdict(lambda: defaultdict(lambda: float("inf")))

        for x1, y1, x2, y2, w in specialRoads:
            u = (x1, y1)
            v = (x2, y2)
            g[u][v] = min(g[u][v], w)
        
        start = (start[0], start[1])
        target = (target[0], target[1])

        q = [(0, start)]
        vis = set()

        while q:
            d, u = heapq.heappop(q)
            if u == target:
                return d
            if u not in vis:
                vis.add(u)
                heapq.heappush(q, (d + self.cost(u, target), target))
                for v in g:
                    if v not in vis:
                        heapq.heappush(q, (d + self.cost(u, v), v))
                for v in g[u]:
                    print(u, v, g[u][v])
                    if v not in vis:
                        heapq.heappush(q, (d + g[u][v], v))

