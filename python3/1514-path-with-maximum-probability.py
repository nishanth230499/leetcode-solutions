import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(dict)

        for (u, v), w in zip(edges, succProb):
            g[u][v] = w
            g[v][u] = w

        q = [(-1, start_node)]
        vis = set()
        
        while q:
            d, u = heapq.heappop(q)
            if u == end_node:
                return -d
            if u not in vis:
                vis.add(u)
                for v in g[u]:
                    if v not in vis:
                        heapq.heappush(q, (d * g[u][v], v))
        
        return 0
        